project:
  type: book
  output-dir: _book

book:
  title: "Principles of Constitutional Law"
  subtitle: "Cases, Statutes, and Commentary"
  author: "Your Name"
  date: today
  chapters:
    - index.qmd
    - chapter-1.qmd

format:
  html:
    theme: cosmo
    toc: true
    toc-depth: 3
    number-sections: true
  pdf:
    documentclass: scrreprt
    papersize: letter
    toc: true
    number-sections: true
    colorlinks: true
  epub:
    toc: true
    
