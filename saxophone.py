import sys

finger_map = {'c':[2,3,4,7,8,9,10],
            'd':[2,3,4,7,8,9],
            'e':[2,3,4,7,8],
            'f':[2,3,4,7],
            'g':[2,3,4],
            'a':[2,3],
            'b':[2],
            'C':[3],
            'D':[1,2,3,4,7,8,9],
            'E':[1,2,3,4,7,8],
            'F':[1,2,3,4,7],
            'G':[1,2,3,4],
            'A':[1,2,3],
            'B':[1,2]
            }



input_nr = 1
for line in sys.stdin:
    counter = [0,0,0,0,0,0,0,0,0,0]
    previous_fingers = [False for i in range(10)]
    if input_nr == 1:
        total_cases = int(line[0])
    if 1 < input_nr <= total_cases + 1:
        line = line.strip()
        for note in line:
            for finger in range(10):
                if finger+1 in finger_map[note]:
                    if previous_fingers[finger] == False:
                        counter[finger] += 1
                    previous_fingers[finger] = True
                else:
                    previous_fingers[finger] = False
                   
        print(' '.join(map(str, counter)))
    if input_nr == total_cases + 1:
        break
    input_nr += 1