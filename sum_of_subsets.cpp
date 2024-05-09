#include <bits/stdc++.h>
using namespace std;
bool flag = 0;

void PrintSubsetSum(int i, vector<int>&set, int targetSum, vector<int>& subset){
	if (targetSum == 0) {
		flag = 1;
		cout << "[ ";
		for (int i = 0; i < subset.size(); i++) {
			cout << subset[i] << " ";
		}
		cout << "]";
		return;
	}

	if (i == set.size()) {
		return;
	}

	// exclude
	PrintSubsetSum(i + 1, set, targetSum, subset);

	// include
	if (set[i] <= targetSum) {

		subset.push_back(set[i]);

		PrintSubsetSum(i + 1, set, targetSum - set[i], subset);

		subset.pop_back();
	}
}

// Driver code
int main()
{
	// Test case 1
	vector<int>set = { 1, 2, 1 };
	int sum = 3;
	vector<int> subset;

	cout << "Output 1:" << endl;
	PrintSubsetSum(0,set, sum, subset);
    if (!flag) {
		cout << "There is no such subset";
	}
	cout << endl;
	flag = 0;


	// Test case 2
	vector<int>set2 = { 3, 34, 4, 12, 5, 2 };
	int sum2 = 30;
	vector<int> subset2;

	cout << "Output 2:" << endl;
	PrintSubsetSum(0, set2, sum2, subset2);
	if (!flag) {
		cout << "There is no such subset";
	}

	return 0;
}
