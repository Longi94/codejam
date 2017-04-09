package y2015.qual;

import java.io.*;

public class Ovation {

    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(args[0]));

            new File(args[1]).createNewFile();
            BufferedWriter bw = new BufferedWriter(new FileWriter(args[1]));

            int testCases = Integer.parseInt(br.readLine());

            for (int i = 1; i <= testCases; i++){
                String[] line = br.readLine().split(" ");

                int max = Integer.parseInt(line[0]);

                int standing = 0;
                int friendsNeeded = 0;

                for (int j = 0; j <= max; j++) {
                    if (standing < j) {
                        friendsNeeded += j - standing;
                        standing = j;
                    }

                    standing += line[1].charAt(j) - '0';
                }

                bw.write("Case #" + i + ": " + friendsNeeded);
                bw.newLine();

            }

            bw.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}