import sys



def bruh(l,r,c):
    global grid
    out = 0
    for i in range(l,r):
        out += grid[i,c]
    return(out)

def solve():
    global n,m,grid
    ans = n*n
    for i in range(n):
        for j in range(i+1,n):
            if m%(j-i): continue
            s = m/(j-i)
            rsum = 0

            if s < n: continue
            for k in range(s):
                rsum += bruh(i,j,k,grid)

            for k in range(s,n+1):
                if ans > m-rsum:
                    ans = m-rsum

                rsum -= bruh(i,j,k-s,grid)
                rsum += bruh(i,j,k,grid)
    return ans


innr = 0
for line in sys.stdin:
    if innr == 0:
        n,m = [int(i) for i in line.split()]
        grid = [[0]*n]*n
    if 0 < innr <= m:
        r,c = [int(i) for i in line.split()]
        grid[r-1][c-1] = 1
    if innr == m:
        print(solve())
        break

    innr +=1




# # # #include <cstdio>

# # # #define maxn 101

# int n, k, grid[maxn][maxn];

# void load() {
# 	scanf( "%d%d", &n, &k );
# 	for( int i = 0; i < k; ++i ) {
# 		int r, s;
# 		scanf( "%d%d", &r, &s );
# 		grid[r-1][s-1] = 1;
# 	}	
# }

# int sum( int l, int r, int c ) { // suma u stupcu c, izmedju redaka l i r
# 	int ret = 0;
# 	for( int i = l; i < r; ++i ) ret += grid[i][c];
# 	return ret;
# }
	
# int solve() {
# 	int ret = n*n;
# 	for( int i = 0; i < n; ++i )
# 		for( int j = i+1; j <= n; ++j ) {
# 			if( k%(j-i) ) continue; // povrsina pravokutnika mora biti jednaka broju kockica, zato stranica mora biti djeljiva sa k
# 			int s = k/(j-i), rsum = 0;
			
# 			if( s > n ) continue;
			
# 			for( int q = 0; q < s; ++q ) rsum += sum( i, j, q );
			
# 			// secemo pravokutnik s lijeva na desno, cijelo vrijeme je gornja stranica redak i, a donja redak j
# 			// rsum je trenutan broj obuhvacenih kockica
# 			for( int q = s; q <= n; ++q ) { 
# 				if( ret > k-rsum ) ret = k-rsum;
				
# 				rsum -= sum( i, j, q-s ); // micemo najljeviji stupac pravokutnika
# 				rsum += sum( i, j, q );   // i dodajemo novi
# 			}
# 		}
# 	return ret;
# }

# int main(void) {
# 	load();
# 	printf( "%d\n", solve() );
# 	return 0;
# }
