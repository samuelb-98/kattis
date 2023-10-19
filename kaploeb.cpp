#include <iostream>
#include <string.h>
#include <algorithm>
#include <numeric>
#include <iterator>

//using namespace std;


int INF = 10000,l,k,s;


int main(){
    std::cin >> l >> k >> s;
    int i, time[s],laps[s],r,tm,ts,ttot;
    for (i=0;i<s;i++){time[s] = 0; laps[s] = 0;}
    double t;
    for (i=0;i<l;i++){
        std::cin >> r >> t;
        r -=1;
        tm = t;
        ts = t*100-tm*100;
        ttot = 60*tm + ts;
        time[r] += ttot;
        laps[r] +=1;
        std::cout << tm << " " << ts << std::endl;
    }

    for (int i:time) std::cout << i << " ";

    // std::size_t indices[ sizeof(time) / sizeof(time[0]) ] ;
    // std::iota(std::begin(indices), std::end(indices), 0 ) ; 

    // std::sort( std::begin(indices), std::end(indices), [&time] ( std::size_t i, std::size_t j ) { return time[i] > time[j] ; } ) ;

    // for( std::size_t pos : indices ) std::cout << pos << ' ' ;
    // std::cout << '\n' ;
}