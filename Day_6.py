with open('input_files/input_day6.txt', 'r') as f:
    data = [line.strip().replace(' ', '') for line in f]


##### First task

check = []
count = 0


for character in data:
    for letter in character:
        count += 1
        if len(check)==14:
            break
        elif letter in check:
            check = []
        else:
            check.append(letter)
            #print(check)
    

####second task

s = data[0]
print(type(data))
for i in range(len(s)):
    if i+14 < len(s):
        print(s[i:i+14])
        if len(set(s[i:i+14])) == 14:
            print(i+14)
            break

        
        
    