mkdir lex-quarto && cd lex-quarto
git init
mkdir -p _extensions/lex-quarto cli/lex_cli
touch README.md LICENSE CONTRIBUTING.md template.qmd
touch _extensions/lex-quarto/_extension.yml
touch _extensions/lex-quarto/lex-filter.lua
touch _extensions/lex-quarto/legal-styles.tex
touch cli/pyproject.toml
touch cli/lex_cli/__init__.py cli/lex_cli/parser.py
