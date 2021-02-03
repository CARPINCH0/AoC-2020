'''

the data on the boarding tickets is encoded as follows
the first 7 character keep splitting the number of lanes from 127 by half and picking the top or bottom half each time

for example on entry FBFBBFFRLR
it would mean
F=128/2 = 0 to 64
B=64/2 0 to


maybe work on it as a list of numbers?
pick the tophalf every time and the parameters change depending on which one was choisen?

ex:
def breakpoint (min,max)
    mid-point= (max-min)/2
    if F:
        breakpoint = (min,mid-point)
    upper half = (mid-point, max)

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