#include <iostream>
using namespace std;


// bool issorted(int s,int e,int arr[]){

//     if (s==e){
//         return true;
//     }
//     if(arr[s]>arr[s+1]){
//         return false;
//     }
//     return issorted(s+1,e,arr);

// }

// int sum_of_arr(int arr[],int n,int sum){
//     if (n==0)
//     {
//         return 0;
//     }
//     if(n==1)
//     {
//         return arr[0];
//     }
//     return arr[0] + sum_of_arr(arr+1,n-1,sum);
// }

// bool linearsearc(int arr[],int n , int key)
// {
//     if(n==0){
//         return false;
//     }
//     if(arr[0]==key)
//     {
//         return true;
//     }
//     return linearsearc(arr+1,n-1,key);
    
// }

bool binarysearch(int *arr,int s ,int e, int key){
    if (s>e)
        return false;

    int mid = s+ (e-s)/2;
    if(arr[mid]==key)
        return true;
    
    if(arr[mid]<key){
        
            return binarysearch(arr,mid+1,e,key);
    }
    else {
        return binarysearch(arr,s,mid-1,key);
    }
    
}
int main(){
int arr[] = {1,2,3,4,5,6,7,8};
int n = sizeof(arr)/sizeof(arr[0]);

// cout<<"is array sorted or not 1 for sorted and 0 for unsorted :"<<issorted(0,n-1,arr)<<endl;
// cout<<"some of the element of the array : "<<sum_of_arr(arr,n,0)<<endl;
// cout<<"searching a key is present in array or not : "<<linearsearc(arr,n,1)<<endl;
cout<<"bianrysearch searching a key is present in array or not : "<<binarysearch(arr, 0,n-1,2)<<endl;
}