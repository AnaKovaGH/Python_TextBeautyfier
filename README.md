Text editing program Version 1.0 01/08/2017


GENERAL USAGE NOTES
----------------------------------------------------------------------
Input:

- Text with unicode symbols which are not supported within LaTeX.  

Output:

- Text split in 80-char lines. 

- Between paragraphs two empty lines. 

- All quotes are replaced by a double apostrophe and double back normal. 

- Before the symbols "$", "%", "[]" "()" put a slash. 

```bash
usage: latex_beautify.py [-h] [-i INPUT] [-d DESTINATON]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        A file which to translate
  -d DESTINATON, --destinaton DESTINATON
                        Output file, where to write beautified text.If not
                        specified, text is printed to STDOUT
```


======================================================================

Text editing program can be reached at:

Github: https://github.com/AnnieKey/LaTeX-text-beutifier
