import java.util.*;
public class RadixSort {
    private static final int RANGE = 255;
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
    public static void main(String[] args) {
        ArrayList<String> arr = new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        String str;
        int n = scan.nextInt();
        int max = 0;
        for (int i = 0; i < n; i++) {
            str = scan.nextLine();
            if (max < str.length())
                max = str.length();
            arr.add(str);
        }
        radixSort(arr, n, max);
    }
}