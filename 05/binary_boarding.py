def get_seat_id(boarding_pass):
    seat_number = 0
    exp = 6
    for c in boarding_pass[:7]:
        if c == 'B':
            seat_number += 2**exp
        exp -= 1
    
    seat_number *= 8

    exp = 2

    for c in boarding_pass[7:]:
        if c == 'R':
            seat_number += 2**exp
        exp -= 1

    return seat_number

booked = set()

file_obj = open('input', 'r')

for line in file_obj:
    booked.add(get_seat_id(line))

for i in range(1023):
    if not i in booked and (i-1) in booked and (i+1) in booked:
        print('Your seat is ' + str(i))