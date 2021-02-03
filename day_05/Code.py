'''
this is the code to solve day 5 of advent of code https://adventofcode.com/2020/day/5#part2

the data on the boarding tickets is encoded as 10 characters, either F, B, R or L.

the seating chart can be understood as an array of 128 x 8 with each letter making it smaller by half

F: the seat is in the first vertical half of this array 
B: the seat is in the second vertical half of this array
R: the seat is in the first horizontal half of the array
L: the seat is in the second horizontal half of the array

mid_pointh = the mid point on the vertical axis of the array
mid_pointv = the mid point on the horizontal axis of the array
minh =the minimum horizontal value of the array
maxh =the maximum horizontal value of the array
minv =the minimum vertical value of the array
maxv =the maximum vertical axis of the array

in order to maintain the number of the seat we will look at the difference between the maximum and minimum posible values as the start and end of a new array

for example on entry FBFBBFFRLR
it would mean
1st value 0 to 128 x 0 to 8 
    128-0 = 128
    128/2 = 64
    meaning we have an array of 0 to 128 and a mid point of 64
    the F value indicates that we are only looking at the first vertical half of the array, meaning numbers 0 to 64 and the horizontal value is unchanged

2nd value 0 to 64 x 0 to 8
    64-0 = 64
    64/2 = 32 
    the F value gives us a reduced array of 32 to 64 x 0 to 8

3rd value 32 to 64 x 0 to 8
    (64-32)/2 = 16 
    the F value again gives us the min value + and the mid value plus min  as the new parameters or 32 to 48 x 0 to 8

4th value 32 to 48 x 0 to 8
    (48-32)/2 = 8 
    the B value gives us a reduced array of 40 to 48 x 0 to 8

5th value 40 to 48 x 0 to 8
    (48-40)/2 = 4 
    Value B = 44 to 48 x 0 to 8

6th value 44 to 48 x 0 to 8
    (48-44)/2 = 2
    value F = 44 to 46 x 0 to 8

7th value 44 to 46 x 0 to 8
    (46-44)/2= 1
    value F 44 to 45 x 0 to 8

the answer to this vertical positon is 44

'''

def initialize_list():
    seat_list = []
    with open('input.txt', 'r') as input:


        for line in input:
            count = 0
            minv=0
            maxv=128
            minh=0
            maxh=8

            for character in line:
                count = count+1
                mid_pointv = (maxv - minv)/2
                mid_pointh = (maxh - minh)/2
                if character == "F":
                    maxv = mid_pointv + minv
                if character == "B":
                    minv = mid_pointv + minv
                if character == "L":
                    maxh = mid_pointh + minh
                if character == "R":
                    minh = mid_pointh + minh

                if count == 10:
                    code = (minv*8)+minh
                    seat_list.append(code)
        print (max(seat_list))
        return seat_list
                    #print (character + " minv :" + str(minv) + "," + " maxv :" + str(maxv) + "," + " minh :" + str(minh) + "," + " maxh :" + str(maxh) + " mid-point h: " + str(mid_pointh) + " mid-point v: " + str(mid_pointv))


seat_list = initialize_list()

matrix = []
rowsN = 128
rows = [iter * 8 for iter in range(rowsN)]
#print (L)


for i in rows:
    matrix.append(i+1)
    matrix.append(i+2)
    matrix.append(i+3)
    matrix.append(i+4)
    matrix.append(i+5)
    matrix.append(i+6)
    matrix.append(i+7)


def Diff(matrix, seat_list):
    li_dif = [i for i in matrix + seat_list if i not in seat_list]
    return li_dif


li3 = Diff(matrix, seat_list)
print("open seats: " + str(li3))