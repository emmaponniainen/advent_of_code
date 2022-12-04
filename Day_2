
with open('input_files\input_day2.txt') as f:  #read the data
    data = (f.readlines())

strip_data = [x.strip() for x in data] #strip data from \n

#print(strip_data)


#make list into single strings

def parse_lists(l):
    ret_list = []
    for elt in l:
        
        for letter in elt.split():
            ret_list.append(letter)
    return ret_list
new_list = parse_lists(strip_data)




import numpy as np


data_array = np.array(new_list).reshape(-1, 2) #make array



total_points = 0



#This block below did not work

for elt in data_array:
    if elt[0] == "A": #Rock
        if elt[1]== "X": #rock
            total_points = total_points + 3 #draw
            total_points = total_points + 1
        elif elt[1]=="Y": #paper
            total_points = total_points + 6 #win
            total_points = total_points + 2
        elif elt[1] == "Z":
            total_point = total_points + 0
            total_points = total_points + 3
    if elt[0]=="B": #paper
        if elt[1]=="X":
            total_points = total_points + 0
            total_points = total_points + 1
        elif elt[1]=="Y":
            total_points = total_points + 3 # draw
            total_points = total_points + 2
        elif elt[1] == "Z":
            total_points = total_points + 6 # win
            total_points = total_points + 3
    else: #Scissor
        if elt[1]=="X":
            total_points = total_points + 6
            total_points = total_points + 1
        elif elt[1]=="Y":
            total_points= total_points + 0
            total_points = total_points + 2
        elif elt[1] == "Z":
            total_points= total_points + 3
            total_points = total_points + 3
            
print(data_array)

### new attempt

with open('input_files\input_day2.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]

part1 = sum({'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}[round] for round in data)
part2 = sum({'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}[round] for round in data)

print('PART 1:', part1)
print('PART 2:', part2)

