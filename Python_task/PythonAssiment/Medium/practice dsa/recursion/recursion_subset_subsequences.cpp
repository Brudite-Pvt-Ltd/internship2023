#include<iostream>
#include<vector>
using namespace std;

void solve(vector<int> arr,vector<int>& output,vector<vector<int>>& ans, int i){
    if(i >= arr.size()){
        ans.push_back(output);
        return;
    }

    solve(arr,output,ans,i+1);

    int element = arr[i];
    output.push_back(element);
    solve(arr,output,ans,i+1);
    output.pop_back();
}

vector<vector<int>> subset(vector<int>& arr){

    vector<vector<int>> ans;
    vector<int> output;
    int index =0;
    solve(arr,output,ans,index);

    return ans;
}

int main(){
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    vector<vector<int>> vect = subset(arr);
     for (auto x : vect){
        cout<<"{";
        for(auto y :x)
            cout<<y;
         cout<<"}";
    }
   
    return 0;

}