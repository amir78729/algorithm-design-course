import java.util.*;

import static java.util.Arrays.sort;

public class RadixSort {
    private int comparisons;
    private static final int RANGE = 255;


    private static void merge(String[] arr, int l, int m, int r)
    {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;

        /* Create temp arrays */
        String L[] = new String[n1];
        String R[] = new String[n2];

        /*Copy data to temp arrays*/
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        /* Merge the temp arrays */

        // Initial indexes of first and second subarrays
        int i = 0, j = 0;

        // Initial index of merged subarry array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i].compareTo(R[j]) != 1 ) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        /* Copy remaining elements of L[] if any */
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        /* Copy remaining elements of R[] if any */
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    private static void mergeSort(String arr[], int l, int r)
    {
        if (l < r) {
            // Find the middle point
            int m = (l + r) / 2;

            // Sort first and second halves
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
        }
    }

//    }
    private static void radixSort(String[] arr, int n, int maximumLength) {
        for (int i = 0; i < maximumLength; ++i) {
            mergeSort(arr, n, i);
            if (i != maximumLength-1)
                System.out.println();
        }
    }
    public static void main(String[] args) {
        ArrayList<String> arraylist = new ArrayList<>();
        Scanner scan = new Scanner(System.in);
        String string;
        int n = scan.nextInt();
        int max = 0;
        string = scan.nextLine();
        for (int i = 0; i < n; i++) {
            string = scan.nextLine();
            if (max < string.length())
                max = string.length();
            arraylist.add(string);
        }
        String[] arr = (String[]) arraylist.toArray();

        radixSort(arr, n, max);
    }
}