#include <bits/stdc++.h> 
using namespace std; 


bool activityCompare(pair<int,int> s1, pair<int,int> s2) 
{ 
	return (s1.second < s2.second); 
} 

void printMaxActivities(vector<pair<int,int>> arr, int n) 
{ 
    sort(arr.begin(), arr.end(), activityCompare);

	cout << "Following activities are selected :\n"; 

	int i = 0; 
	cout << "(" << arr[i].first << ", " << arr[i].second 
		<< ")"; 

	for (int j = 1; j < n; j++) { 
		if (arr[j].first >= arr[i].second) { 
			cout << ", (" << arr[j].first << ", "
				<< arr[j].second << ")"; 
			i = j; 
		} 
	} 
} 

int main() 
{ 
	vector<pair<int,int>> arr = { { 5, 9 }, { 1, 2 }, { 3, 4 }, 
						{ 0, 6 }, { 5, 7 }, { 8, 9 } }; 
	int n = arr.size(); 

	printMaxActivities(arr, n); 
	return 0; 
}


// (1, 2), (3, 4), (5, 7), (8, 9)