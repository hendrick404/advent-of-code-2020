numbers = []

file_obj = open('input', 'r')
for line in file_obj:
    numbers.append(int(line))

for n in numbers:
    for m in numbers:
        for o in numbers:
         if n != m and n!= o and m != o and n + m + o == 2020:
            print('Found n: ' + str(n) + ', m: ' + str(m) + ' and o: ' + str(o) + '. Mulitpied: ' + str(n*m*o))
            
