import re
import json

passports = []

current_passport =  dict()

file_obj = open('input', 'r')
for line in file_obj:
    if not line.strip():
        passports.append(current_passport)
        current_passport = dict()
    else:
        items =  line.split()
        for item in items:
            key = item.split(':')[0]
            value = item.split(':')[1]
            current_passport[key] = value


passports.append(current_passport)

def filter_str(fun, str):
    result = ''
    for c in str:
        if fun(c):
            result += c
    return result


def is_passport_valid(passport):
    desired_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in desired_fields:
        if not field in passport.keys():
            return False
    return True

def is_passport_valid2(passport):
    if not is_passport_valid(passport):
        #print('Mssing fields')
        return False
    
    for key in passport.keys():
        if key == 'byr':
            if not (int(passport[key]) >= 1920 and int(passport[key]) <= 2002):
                #print('Invalid birth year ' + passport[key])
                return False
        if key == 'iyr':
            if not (int(passport[key]) >= 2010 and int(passport[key]) <= 2020):
                #print('Invalid issue year ' + passport[key])
                return False
        if key == 'eyr':
            if not (int(passport[key]) >= 2020 and int(passport[key]) <= 2030):
                #print('Invalid expiration year ' + passport[key])
                return False
        if key == 'hgt':
            height = int(filter_str(lambda x: x.isdigit(), passport[key]))
            unit = filter_str(lambda x: x.isalpha(), passport[key])
            if (not (unit == 'cm' and height >= 150 and height <= 193) and not (unit == 'in' and height >= 59 and height <= 76)):
                #print('Invalid height ' + passport[key])
                return False
        if key == 'hcl':
            if not re.match('#[\wa-f][\wa-f][\wa-f][\wa-f][\wa-f][\wa-f]', passport['hcl']):
                #print('Invalid hair color ' + passport[key])
                return False
        if key == 'ecl':
            if not passport[key] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                #print('Invalid eye color ' + passport[key])
                return False
        if key == 'pid':
            if not len(passport[key]) == 9:
                #print('Invalid ID ' + passport[key])
                return False
    return True


valid_count = 0

for passport in passports:
    if is_passport_valid2(passport):
        valid_count += 1
        #formatted = json.dumps(passport, indent=4)
        #print('Valid Passport ' + formatted)

print('Found ' + str(valid_count) + ' passports')