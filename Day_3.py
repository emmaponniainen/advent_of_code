with open('input_day3.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]
    
#split each row into two lists of equal size
def parse_lists(l):
    ret_list = []
    for elt in l:
        ret_list.append(elt[0:len(elt)//2])
        ret_list.append(elt[len(elt)//2:])
    
    return ret_list
split_list = parse_lists(data)



import numpy as np

data_array = np.array(split_list).reshape(-1, 2) #make array


d = {} #dictionary to count the letters
            
for elt in data_array:  # find intersection of two columns, and put them into dict
    overlap = (((set.intersection(set(elt[0]), set(elt[1])))))
    dict_count = d.get(tuple(overlap))
    if dict_count is not None:
        d[tuple(overlap)] = dict_count + 1
    else:
        d[tuple(overlap)] = 1



scoring = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52}




total_score = 0

for key in d:
    
    total_score = total_score + (scoring.get(key[0])*(d.get(key)))

        
    
print(total_score)


