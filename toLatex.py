import sys

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
    print("Input:$ python toLatex.py [nameOfFileToConvert].[extension]")
    print("      $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt")
    print("      $ python toLatex.py [nameOfFileToConvert].[extension] -p")
    print("      $ python toLatex.py [nameOfFileToConvert].[extension] [customOutputFile].txt -p")
    print()
    print("It will convert any (raw text based) file extension to a .txt (at least, I think so,")
    print("I tried it with .jl, .py, and of course, .txt), which you can just open up and copy")
    print("and paste into whatever .tex document you're working on. the -p command means you")
    print("don't have the packages and custom commands in your .tex file, so it includes them")
    print("at the top of the .tex, before the \\begin{document}. It's pretty janky and not")
    print("greatly tested, there are probably a ton more .replace()s that I need to do, but it's")
    print("great for simple pseudocode and everything I've been able to find. The outfile needs")
    print("to end in .txt.")


    sys.exit(0)


inFile = open(sys.argv[1], "r")

if len(sys.argv) == 3:
    if sys.argv[2].endswith(".txt"):
        outFile = open(sys.argv[2], "w")
    else:
        outFile = open("formattedLatex.txt", "w")

    if sys.argv[2] == "-p":
        outFile.write("\\usepackage[breakable]{tcolorbox}" + "\n")
        outFile.write("\\def\code#1{\\texttt{#1}}" + "\n")
else:
   outFile = open("formattedLatex.txt", "w")

if len(sys.argv) == 4:
    if sys.argv[3] == "-p":
        outFile.write("\\usepackage[breakable]{tcolorbox}" + "\n")
        outFile.write("\\def\code#1{\\texttt{#1}}" + "\n")

outFile.write("\\begin{tcolorbox}[width=\\linewidth, breakable]" + "\n")

for line in inFile:
    writeLine = line.replace("{", "\\{").replace("}", "\\}").replace("\\", "{\\textbackslash}").replace(" ", "\\ ")
    writeLine = writeLine.replace("\n", "").replace("^", "\\^").replace("&", "\\&").replace("$", "\\$")
    writeLine = writeLine.replace("#", "\\#").replace("%", "\\%").replace("\t", "\\ \\ \\ \\ ")

    outFile.write("\\code{-")
    outFile.write(writeLine)
    outFile.write("}\\\\" + "\n")

outFile.write("\\code{-}\\\\" + "\n")

outFile.write("\\end{tcolorbox}" + "\n")

inFile.close()
outFile.close()
