#include <bits/stdc++.h> 
#include <string>
using namespace std; 

void swap(string* a, string* b) { 
	string t = *a; 
	*a = *b; 
	*b = t; 
} 

bool compare(string A, string B){ // return true if |A|>|B|
	if (A.length() == B.length()){ // |A| = |B|
		int n = A.length();
		for (int i = 0; i < A.length() ; i++){
			if (A[n-i-1] == B[n-i-1]) {
			}
			else {
				return (A[n-i-1] > B[n-i-1]);
			}
		}
	}else{
		return (A.length() > B.length())?true:false;
	}
}

int partition (string arr[], int low, int high) { 
	string pivot = arr[high]; 
	int i = (low - 1); 
	for (int j = low; j <= high - 1; j++)
		if (!compare(arr[j], pivot)) { 
			i++;
			swap(&arr[i], &arr[j]); 
		}
	swap(&arr[i + 1], &arr[high]); 
	return (i + 1);  
}  

int randomized_partition(string arr[], int low, int high){
    srand(time(NULL));
    int random = low + rand() % (high - low);
    swap(arr[random], arr[high]);
    return partition(arr, low, high);
}

void quickSort(string arr[], int low, int high) { 
	if (low < high) { 
		int p = randomized_partition(arr, low, high); 
		quickSort(arr, low, p - 1); 
		quickSort(arr, p + 1, high); 
	} 
} 

void print_result(string arr[], int size) { 
	int i; 
	for (i = 0; i < size; i++) 
		cout << arr[i] << endl; 
} 

int main() { 
	int count;
	cin >> count;
	string arr[count]; 
	for (int i = 0; i < count; i++)
		cin >> arr[i];
	int n = sizeof(arr) / sizeof(arr[0]); 
	quickSort(arr, 0, n - 1); 
	print_result(arr, n); 
	return 0; 
} 

