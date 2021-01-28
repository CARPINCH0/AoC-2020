'''

the data on the boarding tickets is encoded as follows
the first 7 character keep splitting the number of lanes from 127 by half and picking the top or bottom half each time

for example on entry FBFBBFFRLR
it would mean 
F=128/2 = 64
B=64/2


maybe work on it as a list of numbers?
pick the tophalf every time and the parameters change depending on which one was choisen?

ex:
def breakpoint (min,max)
    mid-point= (max-min)/2
    if F:
        breakpoint = (min,mid-point)
    upper half = (mid-point, max)

'''



input = open("input.txt","r")

def find_point (minv,maxv,minh,maxh)
    mid-point= (maxv-minv)/2
    if character == "F":
        maxv = mid-point
    if character == "B":
        minv = mid-point
    if character == "L":
        maxh = mid-point
    if character == "R":
        minh = mid-point
    print ("minv :" + str(minv) + "," + "maxv :" + str(maxv) + "," + "minh :" + str(minh) + "," + "maxh :" + str(maxh))

        

for line in input:
    minv=1
    maxv=128
    minh=1
    maxh=8
    for character in line:
        find_point(minv, maxv,minh,maxh)