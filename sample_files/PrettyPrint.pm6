use v6;
unit module PrettyPrint;

# This takes in an array of tokens, splits on the :, and then constructs a code block from it.
# This returns as a string, which has been "prettified"

sub prettyPrint (@data) is export {
    my $prettyPrintedOutput = "";
    my $inBraces = False;
    my $printedTabLine = False;
    my $tabCount = 0;

    for @data -> $token {
        my @vars;

        # Handling the binding operator. Couldn't get the split to work properly. Kinda dirty to handle it alone, but oh well
        if $token ~~ / \:\:\= / {
            @vars = ["ASSIGNOP", "\:\="]
        } else {
            @vars = split(/ \: /, $token);
        }


        if $inBraces and (@vars[0] !~~ / RBRACE / or $tabCount > 1) and not $printedTabLine {
            if @vars[0] ~~ / RBRACE / {
                loop (my $i = 1; $i < $tabCount; $i++) {
                    $prettyPrintedOutput ~= "\t";
                }
            } else {
                loop (my $i = 0; $i < $tabCount; $i++) {
                    $prettyPrintedOutput ~= "\t";
                }
            }
            $printedTabLine = True;
        }

        if @vars[0] ~~ / COMMENT | EOS | RBRACE | LBRACE / {
            if @vars[0] ~~ / LBRACE / {
                $inBraces = True;
                $tabCount += 1;
            } elsif @vars[0] ~~ / RBRACE / {
                $inBraces = False;
                $tabCount -= 1;
            }
            if $inBraces {
                $prettyPrintedOutput = $prettyPrintedOutput ~ @vars[1] ~ "\n";
                $printedTabLine = False;
            } else {
                $prettyPrintedOutput = $prettyPrintedOutput ~ @vars[1] ~ "\n";
            }
        }

        if @vars[0] ~~ / KEYWORD | VAR | ASSIGNOP | INTEGER | COMPOP | STRING | LPAREN | MATHOP / {
            if $prettyPrintedOutput.ends-with("\(") {
                $prettyPrintedOutput = $prettyPrintedOutput ~ @vars[1]
            } else {
                if $prettyPrintedOutput.ends-with("\n") or $prettyPrintedOutput.ends-with("\t") or $prettyPrintedOutput ~~ "" {
                    $prettyPrintedOutput = $prettyPrintedOutput ~ @vars[1];
                } else {
                    $prettyPrintedOutput = $prettyPrintedOutput ~ " " ~ @vars[1];
                }
            }
        }
        if @vars[0] ~~ / RPAREN / {
            $prettyPrintedOutput = $prettyPrintedOutput ~ @vars[1] ~ " ";
        }

    }

    return $prettyPrintedOutput;


}