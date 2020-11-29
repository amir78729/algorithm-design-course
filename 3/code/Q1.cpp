// C++ implementation of Radix Sort 
#include <iostream> 
#include <vector> 
#include <string>
#include <bits/stdc++.h>

using namespace std; 


#define RANGE 255

//    public static void main(String[] args) {
//
//        /
//    }

//    void radixSort(vector<char[]> strings, int n, int max) {
//        ArrayList<char[]> output = new ArrayList<>();
//        int[] count = new int[RANGE + 1];
//
//        for (int i = 0; i < max; ++i) { //Selecting indexes
//            Arrays.fill(count, 0);
//
//            System.out.println(count);
//
//            for (int j = 0; j < n; j++) {// Output = Strings
//                output.add(strings.get(j));
//            }
//
//            System.out.println(output);
//
//            for (int j = 0; j < n; j++) {//Counting the same letters then storing in count array.
//                try {
//                    ++count[strings.get(j)[i]];
//                } catch (Exception e) {//If it is null then add it to count[0].
//                    ++count[0];
//                }
//            }
//
//            System.out.println(count);
//
//            for (int j = 1; j < RANGE; ++j) {//Adding the previous element.
//                count[j] += count[j - 1];
//            }
//
//            System.out.println(count);
//
//            for (int j = n - 1; j >= 0; j--) {//Sorting elements with count array.
//                try {
//                    output.set(count[strings.get(j)[i]] - 1, strings.get(j));
//                    --count[strings.get(j)[i]];
//                } catch (Exception e) {
//                    output.set(count[0] - 1, strings.get(j));
//                    --count[0];
//                }
//            }
//
//            for (int j = 0; j < n; j++) {//Strings = Output
//                strings.set(j, output.get(j));
//                System.out.print(String.valueOf(output.get(j)) + " ");//Print the result
//            }
//            if (i != max-1)
//                System.out.println();//If it's not the last line then go next line.
//
//            output.clear();//Clear the output array for next round.
//        }
//    }
//}}

int main(){
//	/Initialization
    vector<char[]> strings;
//    Scanner scan = new Scanner(System.in);
    string str;
    int n ;
    cin >> n;
    int maxLen = 0;
//        str = scan.nextLine();

    //Get input
    for (int i = 0; i < n; i++) {
        cin >> str;
        if (maxLen < str.length())//Maximum size of all strings.
            maxLen = str.length();
    	char char_array[str.length()];
		strcpy(char_array, str.c_str());

        strings.push_back(char_array);// Arraylist of arrays
    }

//    radixSort(strings, n, maxLen);
}
