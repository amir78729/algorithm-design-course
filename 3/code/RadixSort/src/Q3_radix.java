import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
public class Q3_radix {
    private static final int RANGE = 255;
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        ArrayList<String> arr = new ArrayList<>();
        int max = 0;
        int n = 0;
        String fileName = "filename.txt";
        try {

            File myObj = new File(fileName);
            Scanner myReader = new Scanner(myObj);
            boolean firstLine = true;

            while (myReader.hasNextLine()) {
                if(firstLine){
                    String data = myReader.nextLine();
                    n = Integer.parseInt(data);
                    firstLine = false;
                }else{
                    String string = myReader.nextLine();
                    if (max < string.length())
                        max = string.length();
                    arr.add(string);
                }
            }
            radixSort(arr, n, max);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        long endTime   = System.currentTimeMillis();
        long totalTime = endTime - startTime;
        System.out.println("");
        System.out.println("(Radix)" + fileName+ " : n=" + n + ", max=" + max + ", time=" + totalTime + "ms");
    }
    private static void countingSort(ArrayList<String> arr, int n, int i){
        ArrayList<String> output = new ArrayList<>();
        int[] count = new int[RANGE + 1];
        Arrays.fill(count, 0);
        for (int j = 0; j < n; j++)
            output.add(arr.get(j));
        for (int j = 0; j < n; j++) {
            try {
                count[arr.get(j).charAt(i)]++;
            } catch (Exception e) {
                count[0]++;
            }
        }
        for (int j = 1; j < RANGE; ++j)
            count[j] += count[j - 1];
        for (int j = n - 1; j >= 0; j--) {
            try {
                output.set(count[arr.get(j).charAt(i)] - 1, arr.get(j));
                count[arr.get(j).charAt(i)]--;
            } catch (Exception e) {
                output.set(count[0] - 1, arr.get(j));
                count[0]--;
            }
        }
        for (int j = 0; j < n; j++) {
            arr.set(j, output.get(j));
            System.out.print(output.get(j) + " ");
        }
    }
    private static void radixSort(ArrayList<String> arr, int n, int maximumLength) {
        for (int i = 0; i < maximumLength; ++i) {
            countingSort(arr, n, i);
            if (i != maximumLength-1)
                System.out.println();
        }
    }

}