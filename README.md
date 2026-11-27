# Open Law Book Publishing Engine

An open-source publishing toolkit for legal authors, researchers and editors, with a particular focus on independent legal writing in Tanzania.

[![Build status](https://github.com/wmps7/Law-/actions/workflows/publish.yml/badge.svg)](https://github.com/wmps7/Law-/actions/workflows/publish.yml)

## What works today

- Local DOCX audit: detects repeated manually typed heading numbers and missing footnote references.
- Automated unit tests using synthetic documents.
- A practical publishing handbook in Quarto format.
- A CI workflow that tests the audit, renders HTML, PDF and EPUB and verifies output files before publication.

The project is an early-stage prototype. It does not verify legal authorities, automatically number Word headings or provide legal advice.

## Quick start

Requires Python 3.10+ for document auditing, and Quarto with TinyTeX for PDF publishing.

```sh
git clone https://github.com/wmps7/Law-.git
cd Law-
python audit.py manuscript.docx
python -m unittest discover -s tests -v
quarto render book.qmd --to all
```

The audit prints JSON only and never modifies or uploads a manuscript. Build outputs are placed in `_book/` locally and uploaded as artifacts by GitHub Actions when the build succeeds.

## Contributions

Open an issue describing the problem and expected result. Use synthetic documents, not client documents or unpublished books. Add a test for any improvement to the audit.

## Roadmap

- Heading hierarchy and cross-reference checks.
- Citation format linting for OSCOLA and Tanzanian legislation.
- Reports for editors and accessibility testing.
- Reusable legal publishing templates.

## Licence

Python software is provided under the MIT licence. Other materials retain their applicable licence terms.

## References

- [Quarto project documentation](https://quarto.org/docs/projects/quarto-projects.html)
- [Quarto publishing documentation](https://quarto.org/docs/publishing/)
- [GitHub Actions](https://docs.github.com/en/actions)
