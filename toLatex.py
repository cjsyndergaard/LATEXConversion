import sys, math

reset = "\u001B[0m"
red = "\u001B[31m"
green = "\u001B[32m"
yellow = "\u001B[33m"
cyan = "\u001B[36m"

if len(sys.argv) == 1:
    print("Available Input:")
    print(
    "$ python toLatex.py [nameOfFileToConvert].[extension]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [tags: -f -p -c -n]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt [tags: -f -p -c -n]" + "\n" +
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
    outFile.write("\\begin{document}\n" + "\n")

if "-p" in sys.argv and "-f" not in sys.argv:
    outFile.write("-------Copy and Paste above \\begin{document}------------\n")
    outFile.write("\\usepackage[breakable]{tcolorbox}" + "\n")
    outFile.write("\\def\code#1{\\texttt{#1}}" + "\n")
    outFile.write("--------------------------------------------------------\n")

if "-c" in sys.argv:
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable, colback=black, coltext=green]" + "\n")

elif "-n" in sys.argv:
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable, colback=violet, coltext=white]" + "\n")
else:
    outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable]" + "\n")

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

    # Add the line to the document
    lineNumberSpacing = '{:>' + str(spaces) + '}'
    outFile.write("\\code{|" + lineNumberSpacing.format(str(i)).replace(" ", "\\ ") + "| ")
    outFile.write(writeLine)
    outFile.write("}\\\\" + "\n")

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
    print(cyan + "File Conversion Complete; See " + sys.argv[2] + " in cd for LATEX" + reset)
else:
    print(cyan + "File Conversion Complete; See formattedLatex.txt in cd for LATEX" + reset)
