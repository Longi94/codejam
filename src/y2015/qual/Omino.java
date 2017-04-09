package y2015.qual;

import java.io.*;

public class Omino {
    public static void main(String[] args) {
        BufferedReader br;
        BufferedWriter bw;

        try {
            br = new BufferedReader(new FileReader(args[0]));
            new File(args[1]).createNewFile();
            bw = new BufferedWriter(new FileWriter(args[1]));

            int tests = Integer.parseInt(br.readLine());

            for (int i = 1; i <= tests; i++) {
                String[] line =  br.readLine().split(" ");

                int X = Integer.parseInt(line[0]);
                int R = Integer.parseInt(line[1]);
                int C = Integer.parseInt(line[2]);

                int maxWidth = X % 2 == 0 ? X/2 : X/2 + 1;

                if (X == 4 && (C == 2 || R == 2)) {
                    bw.write("Case #" + i + ": RICHARD");
                } else if (R*C % X != 0){
                    bw.write("Case #" + i + ": RICHARD");
                } else if (X > 7){
                    bw.write("Case #" + i + ": RICHARD");
                } else if (maxWidth <= C && maxWidth <= R){
                    bw.write("Case #" + i + ": GABRIEL");
                } else {
                    bw.write("Case #" + i + ": RICHARD");
                }

                bw.newLine();
        }

            bw.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
