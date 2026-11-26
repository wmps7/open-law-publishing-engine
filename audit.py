"""Read-only DOCX manuscript checks."""
import argparse
import collections
import json
import re
import zipfile
import xml.etree.ElementTree as ET

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"

def audit(path):
    with zipfile.ZipFile(path) as archive:
        document = ET.fromstring(archive.read("word/document.xml"))
        footnotes = (ET.fromstring(archive.read("word/footnotes.xml"))
                     if "word/footnotes.xml" in archive.namelist() else None)
    headings = collections.defaultdict(list)
    refs = set()
    for index, paragraph in enumerate(document.findall(".//w:p", NS), 1):
        style = paragraph.find("w:pPr/w:pStyle", NS)
        text = "".join(t.text or "" for t in paragraph.findall(".//w:t", NS))
        if style is not None and style.get(W + "val", "").lower().startswith("heading"):
            match = re.match(r"^\s*(\d+(?:\.\d+)*)(?:[.)])?\s+", text)
            if match:
                headings[match.group(1)].append(index)
        refs.update(n.get(W + "id") for n in paragraph.findall(".//w:footnoteReference", NS))
    ids = set() if footnotes is None else {
        n.get(W + "id") for n in footnotes.findall("w:footnote", NS)
    }
    return {
        "duplicate_numbered_headings": {k: v for k, v in headings.items() if len(v) > 1},
        "missing_footnotes": sorted(refs - ids),
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document")
    args = parser.parse_args()
    print(json.dumps(audit(args.document), indent=2))
