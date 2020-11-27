#include <bits/stdc++.h> 
using namespace std; 

class Point { 
	public: 
	float x, y; 
}; 

int compare_x_axis(const void* a, const void* b) { 
	Point *p1 = (Point *)a, *p2 = (Point *)b; 
	return (p1->x - p2->x); 
} 

int compare_y_axis(const void* a, const void* b) { 
	Point *p1 = (Point *)a, *p2 = (Point *)b; 
	return (p1->y - p2->y); 
} 

float distance_between_2_points(Point p1, Point p2) { 
	return sqrt( (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y) ); 
} 

float brute_force(Point P[], int n) { 
	float min = FLT_MAX; 
	for (int i = 0; i < n; ++i) 
		for (int j = i+1; j < n; ++j) 
			if (distance_between_2_points(P[i], P[j]) < min) 
				min = distance_between_2_points(P[i], P[j]); 
	return min; 
} 


float minimum(float x, float y) { 
	return (x > y)? y : x; 
} 

float strip_closest(Point strip[], int size, float dist) { 
	float minimum = dist; 

	qsort(strip, size, sizeof(Point), compare_y_axis); 

	for (int i = 0; i < size; ++i) 
		for (int j = i+1; j < size && (strip[j].y - strip[i].y) < minimum; ++j) 
			if (distance_between_2_points(strip[i],strip[j]) < minimum) 
				minimum = distance_between_2_points(strip[i], strip[j]); 

	return minimum; 
} 

float closest_util(Point P[], int n) { 
	// base
	if (n <= 3) 
		return brute_force(P, n); 
	int middle_index = n/2; 
	Point middle_point = P[middle_index]; 
	float minimum_distance_left = closest_util(P, middle_index); 
	float minimum_distance_right = closest_util(P + middle_index, n - middle_index); 
	float dist = minimum(minimum_distance_left, minimum_distance_right); 
	Point strip[n]; 
	int j = 0; 
	for (int i = 0; i < n; i++) 
		if (abs(P[i].x - middle_point.x) < dist) 
			strip[j] = P[i], j++; 
	return minimum(dist, strip_closest(strip, j, dist) ); 
} 

float closest(Point P[], int n) { 
	qsort(P, n, sizeof(Point), compare_x_axis); 
	return closest_util(P, n); 
} 

int main() { 

  int n;
  float x, y;
  cin >> n;
  Point P[n];

  for (int i = 0 ; i < n; i++)  {
    cin >> x;
    cin >> y;
    P[i] = {x, y};
  }
	cout << closest(P, n); 
	return 0; 
} 