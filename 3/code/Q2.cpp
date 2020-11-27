#include <bits/stdc++.h> 
#include <string>
using namespace std; 

void swap(string* a, string* b) { 
	string t = *a; 
	*a = *b; 
	*b = t; 
} 

bool compare(string A, string B){ // return true if |A|>|B|
//	cout << A << " " << A.length() << " , " << B << " " << B.length() << "=>" << (A.length() == B.length()) << endl;
	if (A.length() == B.length()){ // |A| = |B|
		int n = A.length();
//		cout << "EQ"<<endl;
//		cout << A[A.length() - 1] << ","<< B[B.length() - 1] << endl;
//		cout << int(A[A.length() - 1]) << ","<< int(B[B.length() - 1]) << endl;
//		for (int i = A.length() - 1; i == 0; i--){
		for (int i = 0; i < A.length() ; i++){
//			cout <<"i="<<i << endl;
//			cout << A[n-i-1] << ","<< B[n-i-1] << endl;
//			cout << (A[i] == B[i]) << endl;
//			cout <<typeid(A[i]).name()<<endl;
			if (A[n-i-1] == B[n-i-1]) {
				cout<<"nothing"<<endl;
			}
			else {
//				cout<<"not eq"<<endl;
				return (A[n-i-1] > B[n-i-1]);
//				if (A[i] < B[i])
//					return true;
//				else
//					return false;
					
//				return (A[i] < B[i])?true:false;
			}
		}
	}else {
//		cout << A << ","<< B << endl;
		return (A.length() > B.length())?true:false;
	}
	
}



int partition (string arr[], int low, int high) { 
	string pivot = arr[high]; // pivot 
	int i = (low - 1); // Index of smaller element 

	for (int j = low; j <= high - 1; j++){ 
		// If current element is smaller than the pivot 
//		if (arr[j] < pivot) { 
		if (!compare(arr[j], pivot)) { 
			i++; // increment index of smaller element 
			swap(&arr[i], &arr[j]); 
		} 
	} 
	swap(&arr[i + 1], &arr[high]); 
	return (i + 1);  
}  

int partition_r(string arr[], int low, int high){
    // Generate a random number in between
    // low .. high
    srand(time(NULL));
    int random = low + rand() % (high - low);
 
    // Swap A[random] with A[high]
    swap(arr[random], arr[high]);
 
    return partition(arr, low, high);
}

void quickSort(string arr[], int low, int high) { 
	if (low < high) { 
		/* pi is partitioning index, arr[p] is now 
		at right place */
		int pi = partition_r(arr, low, high); 

		// Separately sort elements before 
		// partition and after partition 
		quickSort(arr, low, pi - 1); 
		quickSort(arr, pi + 1, high); 
	} 
} 

void printArray(string arr[], int size) { 
	int i; 
	for (i = 0; i < size; i++) 
		cout << arr[i] << endl; 
//	cout << endl; 
} 

int main() { 
	int count;
	cin >> count;
	string arr[count]; 
	for (int i = 0; i < count; i++){
		cin >> arr[i];
	}
//	string arr[] = {"zzzzz","aa","bb","bc"}; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	quickSort(arr, 0, n - 1); 
//	cout << "Sorted array: \n"; 
	printArray(arr, n); 
	return 0; 
} 

