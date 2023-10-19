#include <iostream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <bits/stdc++.h>
using namespace std;

int cases;
int n;

class Point{
    public:
    int index;
    double dist;
    Point(double dist,int index){
        this->dist = dist;
        this->index = index;
    }
};



struct lidl_compare{bool operator()(Point p1 , Point p2){return p1.dist > p2.dist;}};

double distance(double x1, double x2, double y1, double y2)
{
    return sqrt(pow(x1-x2,2) + pow(y1-y2,2));
}

int main()
{
    cin >> cases;
    for (int c = 0; c < cases; c++) {
        cin >> n;
        double d, x[n], y[n], closest[n], dists[n][n];
        long double total = 0;
        int i, j, edge_counter = 0;
        bool visited[n];
        fill(visited,visited + n, false);
        fill(closest,closest + n, 0.0);
        priority_queue <Point, vector<Point>, lidl_compare> q;  
        set<int> remaining;

        for (i=1;i<n;i++){
            remaining.insert(i);
        };


        for (int i=0;i<n;i++) {cin >> x[i] >> y[i];}


        for (int i=0;i<n;i++) {
            for (int j=i;j<n;j++){
                d = distance(x[i],x[j],y[i],y[j]);
                dists[i][j] = d;
                dists[j][i] = d;
            }
        }


        visited[0] = true;
        int p;
        for (int p=1;p<n;p++){
            q.push(Point(dists[0][p],p));
            closest[p] = dists[0][p];
        }
        
        Point curr = Point(0,0);
        while (edge_counter < n-1){


            while (true){
                curr = q.top();
                q.pop();
                if (visited[curr.index]){continue;}
                break;
            }
            
            total += curr.dist;
            visited[curr.index] = true;
            edge_counter +=1;
            remaining.erase(curr.index);

            set<int>::iterator it = remaining.begin();
            while (it!=remaining.end()){
                if (dists[curr.index][*it] < closest[*it]){
                    closest[*it] = dists[curr.index][*it];
                    q.push(Point(dists[curr.index][*it],*it));
                }
                it++;
            }
        }    
        cout.precision(2);
        cout << fixed << total << endl;
    }
       
}


