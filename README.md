# Python-LaTeX

I used `python3.4` and `TeX Live 2013`.

## Setup

Add two lines to `.bashrc` file.

1. Declare system variable.
 `export PYTHON_LATEX=[/path/to/Python-LaTex]`
2. Add to PATH variable.
 `export PATH="$PATH:$PYTHON_LATEX/bin"`

## Basic usage

- .ptx file to .ltx file.
 `py2tex [.ptx file]`
- .ptx file to .pdf file.
 `py2pdf [.ptx file]`
- .ptx file to .pdf files with and without solutions.
 `py2pdf -s [.ptx file]`