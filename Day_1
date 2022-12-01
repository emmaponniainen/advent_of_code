with open('input_day1.txt') as f:  #read the data
    data = (f.readlines())


            
strip_data = [x.strip() for x in data] #strip data from \n

print(type(strip_data))


zero_data = ["0" if x == '' else x for x in strip_data] #change '' to 0



#Make the strings into integers

integer_data = [] 


for element in zero_data:
    value = int(element)
    integer_data.append(value)


    
#add together the numbers that are groups
elfs = []
add = 0
for i in integer_data:
    if i > 0:
        add = add + i
        #print(add)
            
    else:
        elfs.append(add)
        add = 0


elfs.sort() #sort the list

print(sum(elfs[-3:])) # print three largest numbers


        