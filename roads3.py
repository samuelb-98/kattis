import sys

nr_cities = ""
input_nr = 1
cities = []
edges = []

def clear_singels(cities,edges):
    for city in cities:
        count = 0
        last_road = ""
        for road in edges: 
            if city in road:
                count += 1
                last_road = road
        if count == 1:
            edges.remove(last_road)
            cities.remove(city)
            print(city, ([i for i in last_road if i!=city][0]))
    return(cities, edges)

def break_loop(cities,edges):
    for city in cities:
        for road in edges:
            if city in road:
                print(city, [i for i in road if i!=city][0])
                edges.remove(road)
                cities.remove(city)
                return(cities, edges)

for line in sys.stdin:
    
    if input_nr == 1:
        nr_cities = int(line.strip())
        cities = list(range(1,nr_cities+1))
    
    
    if 1 < input_nr <= nr_cities + 1:
        line = [int(i) for i in line.split()]
        if set(line) in edges:
            print(line[0], line[1])
            print(line[1], line[0])
            edges.remove(set(line))
        else:
            edges.append(set(line))
    
    
    if input_nr == nr_cities + 1:
        while edges != []:
            cities, edges = clear_singels(cities,edges)
            cities, edges = break_loop(cities, edges)
        break
    input_nr += 1
