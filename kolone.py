import sys

input_nr = 0
for line in sys.stdin:
    if input_nr == 0:
        N1, N2 = [int(i) for i in line.split()]
    if input_nr == 1:
        left_row = list(line.split()[0])[::-1]
    if input_nr == 2:
        right_row = list(line.split()[0])
    if input_nr == 3:
        T = int(line.strip())
        break
    input_nr += 1

order = []
for ant in enumerate(left_row):
    index = 2 * ant[0] + T - (N1 - 1)
    if index < ant[0]:
        index = ant[0]
    order.append((index, ant[1]))

for ant in enumerate(right_row):
    index = N1 + 2 * ant[0] - T
    if index > N1 + ant[0]:
        index = N1 + ant[0]
    order.append((index, ant[1]))

order.sort(key=lambda x:x[0])
output = [i[1] for i in order]
output = "".join(output)
print(output)