Scripts to convert to PDF my Hugo generated online lecture notes. It uses the [shortcodes library](https://pypi.org/project/shortcodes/) by [dmulholland](https://darrenmulholland.com/docs/shortcodes/).

The scripts work as follows:

1. We place ourselves in the Hugo folder `.` and clone this repo. This folder must contain the following two extra files (see [this repo](https://gitlab.com/edarfoc/estalg) as an example):
    * `tree.txt` a list of `.md` files in `contents/` to be converted to PDF, with path relative to that folder.
    * `latex.tex` a LaTeX file that will produce the PDF. For each `path-to-file/file.txt`in `tree.txt` include an `\input{hugotopdf/outputs/path-to-file/file.txt}`.
2. `cd hugoto pdf`
3. `./script.sh` (you have to allow execution as a program). This script does the following:
    * It tells the shortcodes library the list of shortcodes to be converted into LaTeX blocks. Those are read from the files `block_lists/name.txt` and `block_lists/no_name.txt`. The shorcodes in the first file will read and print a `name`key, e.g. a theorem title.
    * It generates a python script `generate.py` to process the `.md` files with the shortcodes library. It uses python3, as the library requires it.
    * It runs `generate.py`, then `pandoc` to translate LaTeX code, then it removes leftovers and corrects some `pandoc` conversion misunderstanding.
    * It runs `latexmk`with `lualatex` to produce the PDF.
    * It opens the pdf file with `gio`.