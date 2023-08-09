// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
void sort(int *arr, int n,int j=1) {

    if(j>=n){
        return;
    }
for(int i =0;i<n;i++){
    cout<<arr[i]<<" ";
}cout<<endl;
    // for(int i = j+1;i<n;i++) {
    //     if(arr[i]<arr[j]){
    //         swap(arr[i],arr[j]);
    //     }
    //     // cout<<arr[i]<<" ";
    // }
    int i =j;
    while(arr[i]<arr[i-1]&&i>0){
        swap(arr[i],arr[i-1]);
        i--;
    }
    cout<<endl;
    sort(arr,n,j+1);
    
}

int main() {
  int arr[] = {2,5,3,7,1,0,8,4};
  int n = sizeof(arr)/sizeof(arr[0]);
//   cout<<n<<endl;
  sort(arr,n);

for(int i =0;i<n;i++){
    cout<<arr[i]<<" ";
}
    return 0;
}