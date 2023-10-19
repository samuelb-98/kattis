from re import T


tiles = [["bh","gh","yh","yt"],["bh","gt","yt","gt"],["bh","yt","rh","gh"],["yh","rt","bt","rh"],["gh","yt","gt","bt"],["yh","rh","gt","gh"],["rt","rt","bt","gh"],["bh","bt","rt","yt"],["bh","rh","rh","yt"]]

def rotate(list,n):
    return(list[n:]+list[:n])

def fits(placed,new):
    if len(placed) == 0:
        return(True)
    if len(placed) in [1,2]:
        if placed[-1][2][0] == new[0][0] and placed[-1][2][1] != new[0][1]:
            return(True)
        else:
            return(False)
    if len(placed) in [3,6]:
        if placed[-3][3][0] == new[1][0] and placed[-3][3][1] != new[1][1]:
            return(True)
        else:
            return(False)
    if len(placed) in [4,5,7,8]:
        if placed[-1][2][0] == new[0][0] and placed[-1][2][1] != new[0][1]:
            if placed[-3][3][0] == new[0][0] and placed[-3][3][1] != new[0][1]:
                return(True)
        return(False)

def find_pattern(tiles,placed):
    available = tiles.copy()
    placed = placed.copy()
    for tile in tiles:
        for r in [0,1,2,3]:
            if fits(placed,rotate(tile,r)):
                placed.append(rotate(tile,r))
                tiles.remove(tile)
                if len(placed) == 9:
                    return(placed)
                find_pattern(tiles,placed)


find_pattern(tiles,[])