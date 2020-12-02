file_obj = open('input', 'r')

correct_count = 0

def is_valid(min, max, letter, password):
    count = 0
    for i in password:
        if i == letter:
            count += 1
    return min <= count and count <= max

def is_valid2(first, second, letter, password):
    firstPosition = password[first-1] == letter
    secondPosition = password[second-1] == letter
    return firstPosition != secondPosition

for line in file_obj:
    print('Checking ' + line)
    tokens = line.split()
    (min, max) = tokens[0].split('-')
    letter = tokens[1][0]
    password = tokens[2]
    if is_valid2(int(min), int(max), letter, password):
        correct_count += 1
        print('Found valid password ' + password)
    
print('Found total of '+ str(correct_count) + ' passwords')
    