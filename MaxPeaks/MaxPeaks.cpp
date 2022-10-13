#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    vector<int>peaks(n,0);
    int peak=0;
    for(int i=1;i<n-1;i++){
    if(arr[i]>arr[i-1]&&arr[i]>arr[i+1]){
        peak++;
    }
    peaks[i]=peak;
    }
    peaks[n-1]=peak;
    int k;
    cin>>k;
    int m=arr[k-1];
    int l=0;
    for(int i=k;i<n;i++){
    m=max(peaks[i]-peaks[l],m);
    }
    cout<<m;
}