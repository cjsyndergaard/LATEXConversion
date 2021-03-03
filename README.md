# LATEXConversion

## Description:

Converts text based files (.txt, .py, .jl, etc.) into code-like formatted LATEX; Useful for transcribing code into LATEX
The purpose of this .py file is to output well formatted LATEX code from some text based file.


## Use on the command line:

    $ python toLatex.py [nameOfFileToConvert].[extension]
    $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt
    $ python toLatex.py [nameOfFileToConvert].[extension] -p
    $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt -p

Without customOutputFile name, or if you try and output it to a file without the .txt extension,
the program will output the code to a file named "formattedLatex.txt"

The "-p" command provides the use with the needed packages at the top of the .txt file. Paste
those into the LATEX document before the \begin{document} line. Once those packages are already
part of your LATEX template, the -p command is unnecessary.
