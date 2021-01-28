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

with open('input.txt', 'r') as input:

    sitL = []

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
                sitL.append(code)
                #print (character + " minv :" + str(minv) + "," + " maxv :" + str(maxv) + "," + " minh :" + str(minh) + "," + " maxh :" + str(maxh) + " mid-point h: " + str(mid_pointh) + " mid-point v: " + str(mid_pointv))
    print (max(sitL))
