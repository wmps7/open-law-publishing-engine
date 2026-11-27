import tempfile
import unittest
import zipfile
from pathlib import Path
from audit import audit

class AuditTests(unittest.TestCase):
    def test_duplicate_and_missing_reference(self):
        xml = '''<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>
        <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>1.0 First</w:t></w:r></w:p>
        <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>1.0 Second</w:t><w:footnoteReference w:id="4"/></w:r></w:p>
        </w:body></w:document>'''
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", xml)
            self.assertEqual(audit(path), {"duplicate_numbered_headings": {"1.0": [1, 2]}, "missing_footnotes": ["4"]})

    def test_valid_footnotes(self):
        ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "valid.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", f'<w:document xmlns:w="{ns}"><w:body><w:p><w:r><w:footnoteReference w:id="1"/></w:r></w:p></w:body></w:document>')
                archive.writestr("word/footnotes.xml", f'<w:footnotes xmlns:w="{ns}"><w:footnote w:id="1"/></w:footnotes>')
            self.assertEqual(audit(path), {"duplicate_numbered_headings": {}, "missing_footnotes": []})
