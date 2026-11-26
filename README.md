# ⚖️ Open Law Book Publishing Engine

[![License: CC BY 4.0](https://shields.io)](https://creativecommons.org)

An automated, open-source legal publishing pipeline built with **Quarto** and **GitHub Actions**. Write legal manuscripts in clean Markdown and automatically compile print-ready **PDFs**, e-reader **EPUBs**, and a searchable **Web Edition** on every save.

## Publication status

Publishing destinations have not yet been verified.

## ✨ Features Built for Legal Authors
* **Automated Case Brief Callouts:** Standardized formatting for Facts, Issues, Holdings, and Rules.
* **Statutory & Practice Notes:** Highlighted blocks for key Acts and practical courtroom guidance.
* **Multi-Format Output:** One source file generates HTML, PDF (LaTeX), and EPUB simultaneously.

## Manuscript audit utility

An early-stage open-source toolkit for authors, editors and legal researchers working with Word manuscripts, especially in Tanzania.

## Purpose

Long legal manuscripts need reliable editorial checks before publication. This project starts with a local, offline DOCX audit utility that flags repeated numbered headings and missing footnote references. It does not verify legal authorities or replace an editor.

## Getting started

Requires Python 3.10 or newer. No third-party dependencies.

```sh
python audit.py manuscript.docx
python -m unittest discover -s tests
```

The tool prints a JSON report. It never edits the manuscript or sends the contents over the network.

## Status

Initial prototype. No adoption or download figures have been established. Feedback and contributions are welcome.

## Roadmap

- Improve heading hierarchy checks and cross-reference diagnostics.
- Add citation formatting checks for Tanzanian legislation and OSCOLA.
- Build anonymised test fixtures and accessible documentation.
- Research integrations with open document-processing tools.

Do not publish confidential manuscripts or client documents in issues. Use synthetic examples only.

## Licence

The Python audit utility is supplied under the MIT licence. Other materials retain their existing licence terms.
