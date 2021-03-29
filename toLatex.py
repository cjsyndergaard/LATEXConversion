import sys, math

# Use on the command line
# Input:$ python toLatex.py [nameOfFileToConvert].[extension]
#       $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt
#       $ python toLatex.py [nameOfFileToConvert].[extension] -p
#       $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt -p
#
# It will convert any (raw text based) file extension to a .txt (at least, I think so,
# I tried it with .jl, .py, and of course, .txt), which you can just open up and copy
# and paste into whatever .tex document you're working on. the -p command means you
# don't have the packages and custom commands in your .tex file, so it includes them
# at the top of the .tex, before the \begin{document}. It's pretty janky and not
# greatly tested, there are probably a ton more .replace()s that I need to do, but it's
# great for simple pseudocode and everything I've been able to find. Outfile needs to
# end in .txt

if len(sys.argv) == 1:
    print("Available Input:")
    print(
    "$ python toLatex.py [nameOfFileToConvert].[extension]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [tags: -f -p -c -n]" + "\n" +
    "$ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt [tags: -f -p -c -n]" + "\n" +
    "\t For more information on tags, run the program with tag --help"
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

if len(sys.argv) > 2:
    if sys.argv[2].endswith(".txt"):
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

i = 1

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
    i += 1

outFile.write("\\end{tcolorbox}" + "\n")

if "-f" in sys.argv:
    outFile.write("\\end{document}")

inFile.close()
outFile.close()
