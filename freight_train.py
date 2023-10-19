import sys

input_nr = 1

for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 1:
        total_inputs = line[0]


    if input_nr % 2 == 0 and input_nr > 1:
        N, W, L = line
        lower_bound = W // L - 1
        upper_bound = (N // L) + 2
    
    
    if input_nr % 2 == 1 and input_nr > 1:
        cargo_positions = line
        
        while lower_bound != upper_bound: 
            current_guess = (lower_bound + upper_bound)//2
            step, current_wagon, next_cargo = [0,1,0]
            
            while current_wagon <= cargo_positions[-1] and step <= L:
                
                if current_wagon + current_guess <= cargo_positions[next_cargo]:
                    current_wagon = cargo_positions[next_cargo]
                else:
                    current_wagon += current_guess
                    while current_wagon > cargo_positions[next_cargo] and current_wagon <= cargo_positions[-1]:
                        next_cargo += 1
                step += 1
            if current_wagon < N:
                step += 1
            if step <= L:    
               upper_bound = current_guess
            else:
                lower_bound = current_guess + 1
        print(lower_bound)
    input_nr += 1

    
    if input_nr == 2 * total_inputs + 2:
        break