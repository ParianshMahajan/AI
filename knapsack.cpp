#include<bits/stdc++.h>
using namespace std;


int knapSack(int W, vector<int>weight, vector<int>profit, int i, vector<vector<int>> &dp)
{
    if (i >=profit.size() || W == 0) return 0;
    
    if(dp[i][W]!=-1) return dp[i][W];
    
    // Excluding
    if (weight[i] > W)
        return dp[i][W]=knapSack(W, weight, profit, i+1,dp);
    else
        return dp[i][W]=max((profit[i]+ knapSack(W - weight[i],weight, profit, i+1,dp)),knapSack(W, weight, profit, i+1,dp));
}


int main(){
    vector<int>profit = { 60, 100, 120 };
    vector<int>weight = { 10, 20, 30 };
    int W = 50;
    vector<vector<int>> dp(profit.size() + 1, vector<int>(W + 1, -1));
    cout << knapSack(W, weight, profit, 0,dp);
    return 0;
}