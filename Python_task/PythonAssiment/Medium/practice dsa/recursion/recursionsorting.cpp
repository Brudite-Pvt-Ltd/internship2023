#include <iostream>
using namespace std;

void bubbleorting(int arr[],int n){
if(n==0||n==1)
    return;
for(int i =0;i<n;i++){
    if(arr[i]> arr[i+1]){
        swap(arr[i],arr[i+1]);
    }
}
bubbleorting(arr,n-1);
}

void insertionsort(int arr[],int n ,int s){
    if(s==n)
    return; 

    for(int i=s;i>0;i--)
    {   
        if(arr[i]<arr[i-1])
            swap(arr[i],arr[i-1]); 
        else
            break;
    }
    // for(int i =0;i<n;i++){ 
    //     cout<<arr[i];
    // }
    // cout<<endl;
    insertionsort(arr,n,s+1);
}

void selectionsort(int arr[],int n ,int s){
    if(s==n){
        return;
    }
    for(int i = n-1;i>s;i--){
        if(arr[i]<arr[i-1]){
            swap(arr[i],arr[i-1]);
        }
     
    }
    selectionsort(arr,n,s+1);
}

void merge(int *arr,int s,int e){
    int mid = (s+e)/2;
    int len1 = mid - s +1;
    int len2 = e -mid;

    int *first = new int[len1];
    int *second = new int[len2];
    
    int k = s;
    for(int i =0;i<len1;i++){
        first[i] = arr[k++];
    }
    k = mid+1;
    for(int i =0;i<len2;i++){
        second[i] = arr[k++];
    }
    k =s;
    int i1 =0;
    int i2 =0;
    while(i1<len1 && i2 <len2){
        if(first[i1] < second[i2])
        { arr[k++] = first[i1++];}
        else
        {arr[k++] = second[i2++];}
    }
    while(i1<len1){
        arr[k++] = first[i1++];
    }
    
    while(i2<len2){
        arr[k++] = second[i2++];
    }
}
        
int partation(int arr[],int s ,int e){

    int pivot = arr[s];
    int cnt =0;
    for(int i = s+1;i<=e;i++){
        if(arr[i]<pivot){
            cnt++;
        }
    }
    int pivotindex = s+cnt;
    swap(arr[pivotindex],arr[s]);
    int i = s;
    int j =e;
    while(i<pivotindex && j> pivotindex){
        while(arr[i]<pivot){
            i++;
        }
        while(arr[j]>pivot){
            j--;
        }
        if(i<pivotindex && j> pivotindex)
        swap(arr[i++],arr[j--]);
    }

    return pivotindex;
}

void quicksort(int arr[],int s,int e){
    if (s>=e)
        return;
    int pivot = partation(arr,s,e);
    quicksort(arr,s,pivot-1);
    quicksort(arr,pivot+1,e);

}


void mergesort(int *arr,int s, int e){
    if(s>=e)
        return;
    int mid = (s+e)/2;
    mergesort(arr,s,mid);
    mergesort(arr,mid+1,e);
    merge(arr,s,e);
}

int main(){
    int arr[]= {0,3,8,2,24,4,7,66,5,1,11,98};
    int n = (sizeof(arr)/sizeof(arr[0]));
    // selectionsort(arr,n,0);
    // insertionsort(arr,n,1);
    // mergesort(arr,0,n-1);
    quicksort(arr,0,n-1);
    for(int i =0;i<n;i++){
        cout<<arr[i];
    }
}