#include<iostream>
#include <algorithm>
#include<vector>
using namespace std;

bool issafe(int x,int y, vector<vector<int>> m ,int n, vector<vector<int>> visited){
    if(visited[x][y]==0 && m[x][y] == 1 && (x >= 0 && x<n) && (y>= 0 && y<n))
        return true;
    return false;
}

void solve(vector<vector<int>> m,int n, int x,int y, vector<vector<int>> visited,vector<string> ans,string path){
    if(x==n-1 && y ==n-1)
    {
        ans.push_back(path);
        return;
    }
    visited[x][y] = 1;
    // Down (x+1,y)
    int newx = x+1;
    int newy = y;
     if( issafe(newx,newy,m ,n, visited) && x!=n-1)
     {
        path.push_back('D');
        solve(m,n,x+1,y,visited,ans,path);
        path.pop_back();
     }

    //up(x-1,y)
    int newx = x;
    int newy = y-1;
     if( issafe(newx,newy,m ,n, visited) && x!=0)
     {
        path.push_back('U');
        solve(m,n,x-1,y,visited,ans,path);
        path.pop_back();
     }


    //left(x,y-1)
    newx = x;
    newy = y-1;
     if( issafe(newx,newy,m ,n, visited) && y!=0)
     {
        path.push_back('L');
        solve(m,n,x,y-1,visited,ans,path);
        path.pop_back();
     }

    //right(x,y+1)
    newx = x;
    newy = y+1;
    if( issafe(newx,newy,m ,n, visited) && y!=n-1)
    {
        path.push_back('R');
        solve(m,n,x,y+1,visited,ans,path);
        path.pop_back();
    }
    visited[x][y] =0;

}

vector<string> ratinmaze(vector<vector<int>>& m,int n)
{
    vector<string> ans ;
    int x= 0;
    int y =0;
    string path= "";
    vector<vector<int>> visited = m;

    for(int i =0;i<n;i++){
        for(int j=0;j<n;j++)
        {
            visited[i][j] = 0;
        }
    }
    solve(m,n,x,y,visited,ans,path);
    sort(ans.begin(),ans.end());
    return ans;

}


int main(){

vector<vector<int>> m;



    return 0;
}