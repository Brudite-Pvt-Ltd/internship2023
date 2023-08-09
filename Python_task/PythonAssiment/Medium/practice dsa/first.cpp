// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
void sort(int *arr, int n,int j=0) {

    if(j==n){
        return;
    }
    for(int i = j;i<n-1;i++) {
        if(arr[i]>arr[i+1]){
            swap(arr[i],arr[i+1]);
        }
    }
    sort(arr,n,j++);
    
}

int main() {
  int arr[] = {2,5,3,7,8};
  int n = sizeof(arr)/sizeof(arr[0]);
  cout<<n<<endl;
  sort(arr,n-1);

for(int i =0;i<n;i++){
    cout<<arr[i]<<" ";
}
    return 0;
}