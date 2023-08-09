#include <iostream>
using namespace std;

void reversed(string& st,int s,int e){
    if(s>e)
    return ;
   
    swap(st[s],st[e]);
    reversed(st,s+1,e-1);

}
bool ispalidrome(string st,int s){
    int e = st.length()-s-1;
    if(s>e)
    return true;
    if(st[s]!=st[e])
    return false;
    return ispalidrome(st,s+1);

}
double powerofnumber(int num,int power){
    if(power == 0){
        return 1;
    }
    if(power ==1)
    return num;
    
    double ans =  powerofnumber(num,power/2);
    if(power%2==0)
     return ans*ans;
     else
     return ans * ans*num;
}



int main(){
    string s = "herrehp";
   
    // reversed(s,0,s.length()-1);     
    // cout<<ispalidrome(s,0)<<endl;
    cout<<powerofnumber(3,3);
}