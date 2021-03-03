import java.util.Scanner;


public class Driver {
    public static void main(String[] args) {
        boolean playAgain = true;

        while (playAgain) {
            GridMethods grid = startGame();

            grid.initGrids();

            System.out.println();
            playGame(grid);
            Scanner play = new Scanner(System.in);
            System.out.println();
            System.out.print("Play again? Y for yes, anything else for no");

            String again = play.next().toUpperCase();

            if (!again.equals("Y")) {
                playAgain = false;
            }
        }
    }

    private static GridMethods startGame() {
        makeLine();
        System.out.printf("%39s\n", "WELCOME to MINESWEEPER");
        makeLine();
        Scanner size = new Scanner(System.in);
        System.out.print("Enter the difficulty (1: Beginner, 2: Intermediate, 3: Expert, 4: Custom) : ");
        String diff = size.next();
        System.out.println();

        switch (diff) {
            case "1":
                return new GridMethods(4, 7, 20);
            case "2":
                return new GridMethods(8, 14, 20);
            case "3":
                return new GridMethods(15, 26, 25);
            case "4":
                Scanner custom = new Scanner(System.in);
                System.out.println("Enter the rows, columns, and % bombs, on separate lines: ");
                String newRow = custom.nextLine();
                String newColumn = custom.nextLine();
                String difficulty = custom.nextLine();

                int rows = Integer.parseInt(newRow);
                int columns = Integer.parseInt(newColumn);
                int difficultyLvl = Integer.parseInt(difficulty);

                return new GridMethods(rows, columns, difficultyLvl);
            default:
                System.out.println("Wow, you're not very good at following instructions. Good luck.");
                return new GridMethods(40, 40, 85);
        }
    }

    private static void makeLine() {
        System.out.println("--------------------------------------------------------"); //56
    }

    private static void playGame(GridMethods grid) {
        double time = java.lang.System.currentTimeMillis();
        grid.printOutGrid();
        Scanner uncover = new Scanner(System.in);
        System.out.println();
        System.out.print("Flag or uncover (F or U): ");
        String action = uncover.next().toUpperCase();
        Scanner square = new Scanner(System.in);

        if (action.equals("U")) {
            System.out.print("Which square to uncover? ");
            String tile = square.next().toUpperCase();

            int rowNum;
            int colNum;
            if (tile.length() == 2) {
                char row = tile.charAt(1);
                char col = tile.charAt(0);
                rowNum = (int) row - 49;
                colNum = (int) col - 65;
            }
            else {
                char row = tile.charAt(2);
                char col = tile.charAt(0);
                int tens = (int) (tile.charAt(1));
                rowNum = (int) row - 49 + 10 * (tens);
                colNum = (int) col - 65;
            }

            grid.setCoveredGrid(rowNum, colNum, 2);
            
            if (grid.getBomb(rowNum, colNum)) {
                grid.printFullGrid();
                System.out.println("YOU DIED!!! Loser.");
                return;
            }
            else {
                playGame(grid);
                System.out.println();
                System.out.println();
            }
        }
        else {
            System.out.print("Which square to flag? ");
            String tile = square.next().toUpperCase();

            int rowNum;
            int colNum;
            if (tile.length() == 2) {
                char col = tile.charAt(0);
                char row = tile.charAt(1);
                rowNum = (int) row - 49;
                colNum = (int) col - 65;
            }

            else {
                char row = tile.charAt(2);
                char col = tile.charAt(0);
                int tens = (int) (tile.charAt(1));
                rowNum = (int) row - 49 + 10 * (tens);
                colNum = (int) col - 65;
            }

            grid.setCoveredGrid(rowNum, colNum, 1);
            if (grid.checkBombs()) {
                grid.printFullGrid();
                System.out.println("Congratulations! You won!");
                int time2  =(int) ((java.lang.System.currentTimeMillis() - time) / 100);
                System.out.println("Your time was " + time2 + " seconds");
                return;
            }
            else {
                playGame(grid);
                System.out.println();
                System.out.println();
            }
        }
    }

}
