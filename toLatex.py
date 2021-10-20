import sys, math

reset = "\u001B[0m"
red = "\u001B[31m"
green = "\u001B[32m"
yellow = "\u001B[33m"
cyan = "\u001B[36m"

if len(sys.argv) == 1:
    print(cyan + "Available Input:" + reset + "\n")
    print(
    "If toLatex.py is a raw python file:" + "\n"
    "$ python toLatex.py [nameOfFileToConvert].[extension]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [tags: -f -p -c -n]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt [tags: -f -p -c -n]" + "\n" +
    "\n" +
    "If toLatex.py has alias 'totex':" + "\n" +
    "$ totex [nameOfFileToConvert].[extension]" + "\n" +
    "$ totex [nameOfFileToConvert].[extension] [customOutputFile].txt" + "\n" +
    "$ totex [nameOfFileToConvert].[extension] [tags: -f -p -c -n]" + "\n" +
    "$ totex [nameOfFileToConvert].[extension] [customOutputFile].txt [tags: -f -p -c -n]" + "\n" +
    "\n" +
    yellow + "For more information on tags, run the program with tag --help" + reset
    )
    sys.exit(0)

if "--help" in sys.argv:
    print(
    "-f: Writes a full Latex file with necessary packages to output file" + "\n" +
    "-p: Writes necessary packages to output file" + "\n" +
    "-c: Writes code box with 'hacker' color scheme" + "\n" +
    "-n: Writes code box with 'Nick' color scheme"
    )
    sys.exit(0)

inFile = open(sys.argv[1], "r")
num_lines = sum(1 for line in inFile)

spaces = math.floor(math.log(num_lines, 10)) + 2
if spaces == 2:
    spaces += 1

inFile.seek(0)

customOut = False
if len(sys.argv) > 2:
    if sys.argv[2].endswith(".txt"):
        customOut = True
        outFile = open(sys.argv[2], "w")
    else:
        outFile = open("formattedLatex.txt", "w")
else:
    outFile = open("formattedLatex.txt", "w")

if "-f" in sys.argv:
    outFile.write("\\documentclass{article}\n")
    outFile.write("\\usepackage[breakable]{tcolorbox}" + "\n")
    outFile.write("\\def\code#1{\\texttt{#1}}" + "\n")
    outFile.write("\\setlength{\\topmargin}{-.3 in}" + "\n")
    outFile.write("\\setlength{\\oddsidemargin}{-.25 in}" + "\n")
    outFile.write("\\setlength{\\evensidemargin}{0.25 in}" + "\n")
    outFile.write("\\setlength{\\textheight}{9. in}" + "\n")
    outFile.write("\\setlength{\\textwidth}{7 in}" + "\n")
    outFile.write("\definecolor{darkgrey}{rgb}{0.2, 0.2, 0.2}" + "\n")
    outFile.write("\\begin{document}\n" + "\n")

if "-p" in sys.argv and "-f" not in sys.argv:
    outFile.write("-------Copy and Paste above \\begin{document}------------\n\n")
    outFile.write("\\usepackage[breakable]{tcolorbox}" + "\n")
    outFile.write("\\def\code#1{\\texttt{#1}}" + "\n")
    outFile.write("\definecolor{darkgrey}{rgb}{0.2, 0.2, 0.2}" + "\n\n")
    outFile.write("--------------------------------------------------------\n")

# Themes
mainCol = ""
secCol = ""
thirdCol = ""
opCol = ""

if "-c" in sys.argv:
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable, colback=darkgrey, coltext=green]" + "\n")
    mainCol = "\color{green}"
    secCol = "\color{orange}"
    thirdCol = "\color{white}"
    opCol = "\color{cyan}"

elif "-n" in sys.argv:
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable, colback=violet, coltext=white]" + "\n")
    mainCol = "\color{white}"
    secCol = "\color{yellow}" # Nick Change This
    thirdCol = "\color{green}"
    opCol = "\color{cyan}"
else:
	mainCol = "\color{black}"
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable, colback=white]" + "\n")

# Give reassurance to user something is happening
i = 1
# loading = math.ceil(num_lines / 10)
print(yellow + "File Conversion Begun" + reset)
# print("Conversion: <" + red + ("-" * 10) + reset + ">", end="\r", flush=True)

for line in inFile:
    # Replace escape characters
    writeLine = line.replace("\\", "{\\textbackslash}")
    writeLine = writeLine.replace("{", "\\{")
    writeLine = writeLine.replace("}", "\\}")
    writeLine = writeLine.replace(" ", "\\ ")
    writeLine = writeLine.replace("\n", "")
    writeLine = writeLine.replace("^", "\\^")
    writeLine = writeLine.replace("&", "\\&")
    writeLine = writeLine.replace("$", "\\$")
    writeLine = writeLine.replace("_", "\\_")
    writeLine = writeLine.replace("#", "\\#")
    writeLine = writeLine.replace("%", "\\%")
    writeLine = writeLine.replace("\t", "\\ \\ \\ \\ ")

    # Add Color themes
    if writeLine.startswith("\\#") or writeLine.startswith("//"):
        # Comments
        writeLine = writeLine.replace(writeLine, thirdCol + writeLine + mainCol)
    else:
        # Key words
        writeLine = writeLine.replace("for", secCol + "for" + mainCol)
        writeLine = writeLine.replace("while", secCol + "while" + mainCol)
        writeLine = writeLine.replace(" in ", secCol + " in " + mainCol)
        writeLine = writeLine.replace("try", secCol + "try" + mainCol)
        writeLine = writeLine.replace("print", secCol + "print" + mainCol)
        writeLine = writeLine.replace("string", secCol + "string" + mainCol)
        writeLine = writeLine.replace("boolean", secCol + "boolean" + mainCol)
        writeLine = writeLine.replace("int", secCol + "int" + mainCol)
        writeLine = writeLine.replace("return", secCol + "return" + mainCol)
        writeLine = writeLine.replace("function", secCol + "function" + mainCol)
        writeLine = writeLine.replace("end", secCol + "end" + mainCol)
        writeLine = writeLine.replace("def", secCol + "def" + mainCol)
        writeLine = writeLine.replace("class", secCol + "class" + mainCol)
        writeLine = writeLine.replace("if", secCol + "if" + mainCol)
        writeLine = writeLine.replace("else", secCol + "else" + mainCol)
        writeLine = writeLine.replace("elif", secCol + "elif" + mainCol)
        writeLine = writeLine.replace("null", secCol + "null" + mainCol)

        # Operations
        writeLine = writeLine.replace("+", opCol + "+" + mainCol)
        writeLine = writeLine.replace("-", opCol + "-" + mainCol)
        writeLine = writeLine.replace("*", opCol + "*" + mainCol)
        writeLine = writeLine.replace("/", opCol + "/" + mainCol)
        writeLine = writeLine.replace("=", opCol + "=" + mainCol)
        writeLine = writeLine.replace("<", opCol + "<" + mainCol)
        writeLine = writeLine.replace(">", opCol + ">" + mainCol)
        writeLine = writeLine.replace("!", opCol + "!" + mainCol)
        # writeLine = writeLine.replace("^", opCol + "^" + mainCol)
        writeLine = writeLine.replace(":", opCol + ":" + mainCol)
        writeLine = writeLine.replace(",", opCol + "," + mainCol)
        writeLine = writeLine.replace("'", opCol + "'" + mainCol)

    if "\\#" in writeLine or "//" in writeLine:
        # Comments
        writeLine = writeLine.replace("\\#", thirdCol + "\\#")
        writeLine = writeLine.replace("//", thirdCol + "//")


    # Add the line to the document
    lineNumberSpacing = '{:>' + str(spaces) + '}'
    outFile.write("\\code{\color{gray}|" + lineNumberSpacing.format(str(i)).replace(" ", "\\ ") + "| " + mainCol)
    outFile.write(writeLine)
    outFile.write("}")
    if i != num_lines:
        outFile.write("\\\\")
    outFile.write("\n")
    # Give reassurance to user something is happening:
    # print("Conversion: <" + green + "=" * int(i / loading) + red + "-" * (10 - int(i / loading)) + reset + ">", end="\r", flush=True)
    i += 1

outFile.write("\\end{tcolorbox}" + "\n")
# print("Conversion: <" + green + "=" * 10 + reset + ">", flush=True)

if "-f" in sys.argv:
    outFile.write("\\end{document}")

inFile.close()
outFile.close()

if customOut:
    print(green + "File Conversion Complete; See " + cyan + sys.argv[2] + green + " in cd for LATEX" + reset)
else:
    print(green + "File Conversion Complete; See " + cyan + "formattedLatex.txt" + green + " in cd for LATEX" + reset)
