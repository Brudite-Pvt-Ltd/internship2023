#include<iostream>
#include<vector>
using namespace std;

void phone(string str,int i, vector<string>& ans,string output,string mapping[])
{
    if(i==str.length())
    {
        ans.push_back(output);
        return;
    }
    int number = str[i] - '0';
    string value = mapping[number];
    for(int j =0;j <value.length();j++)
    {
        output.push_back(value[j]);
        phone(str,i+1,ans,output,mapping);
        output.pop_back();
    }
}

vector<string> phonekey(string digit){
    vector<string> ans;
    string output;
    int index =0;
    cout<<"phonekey before calling phoen"<<endl;
    string mapping[10] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    phone(digit,index,ans,output ,mapping);
    cout<<"phonekey after calling phoen"<<endl;
    // for(auto x : ans){
    //     cout<<x;
    // }
    // cout<<ans.size();
    return ans;
}

int main(){
 string digit = "234";
 vector<string> ans = phonekey(digit);
for(auto x: ans){
    cout<<x<<" ";
}
   return 0;
}