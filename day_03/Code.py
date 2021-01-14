''' 
move from one line to the next 3 units to the right and one unit down,
how many trees do I hit before getting to the bottom of the Queue
the tree patterns repeat themselves.

this can be solved as a mathematical problem, where different values are true for each line, and they repeat themselves
every 31 characters it restarts.
we can list what characters on each line we actually care about and get a tally of how many values we get

multiply index of current line multiplied by the value of units that we are shifting to the right
and get the remainder of the expected position (index*vector of right movement) which will equal the position that we need to be on.
adjust the result we previously received to fit a list starting at 0 instead of 1
check if the value for that position is equal to "#"
count the number of results that fit that condition

only problem is with the index starting at 0, we need to accomodate for that
'''

index = -1       # the number of the line we are sitting on, this needs to be -1 so that hen countng lines we start at 0
map_t = []      # a list containing all the values of a single line of the input.
pos_c= 0   # the current mathematical position we are standing on.
pos_i= 0   # the current index position we are standing on 
tree_c= 0       # count of trees on the pathway
vector_r = 0    #the amount of spaces that are moved right
vector_d = 0    #the amount of spaces that are moved down

input = open("input.txt","r")

dirty_i=input.readlines()

def track(vector_r,vector_d):
    index = 0
    tree_c = 0

    for line in dirty_i:
        index = index +1
        map_t = []
        pos_c = ((index*vector_r)%31)+1 
        pos_i = pos_c -1
        if index%vector_d == 0:
            for spot in line:
                map_t.append(spot)
            if map_t[pos_i] == "#":
                tree_c = tree_c +1
    print("slope "+ str(vector_r) + " Right, " + str(vector_d) + " Down: " + str(tree_c))

track(vector_r=1,vector_d=1)
track(vector_r=3,vector_d=1)
track(vector_r=5,vector_d=1)
track(vector_r=7,vector_d=1)
track(vector_r=1,vector_d=2)

'''
index = -1
tree_c2 = 0
for line in dirty_i:
    index = index +1
    map_t = []
    pos_c = ((index*3)%31)+1
    pos_i = pos_c -1
    for spot in line:
        map_t.append(spot)
    if map_t[pos_i] == "#":
        tree_c2 = tree_c2 +1
print("slope 3 Right, 1 Down: " + str(tree_c2))

index = -1
tree_c3 = 0
for line in dirty_i:
    index = index +1
    map_t = []
    pos_c = ((index*5)%31)+1
    pos_i = pos_c -1
    for spot in line:
        map_t.append(spot)
    if map_t[pos_i] == "#":
        tree_c3 = tree_c3 +1
print("slope 5 Right, 1 Down: " + str(tree_c3))

index= -1
tree_c4 = 0
for line in dirty_i:
    index = index +1
    map_t = []
    pos_c = ((index*7)%31)+1
    pos_i = pos_c -1
    for spot in line:
        map_t.append(spot)
    if map_t[pos_i] == "#":
        tree_c4 = tree_c4 +1
print("slope 7 Right, 1 Down: " + str(tree_c4))

index= -1
tree_c5 = 0
for line in dirty_i:
    index = index +1
    map_t = []
    pos_c = ((index*1)%31)+1
    pos_i = pos_c -1
    if index%2 == 0:
        print (index)
        for spot in line:
            map_t.append(spot)
        if map_t[pos_i] == "#":
            tree_c5 = tree_c5 +1
print("slope 1 Right, 2 Down: " + str(tree_c5))

print("final result: " + str(tree_c1*tree_c2*tree_c3*tree_c4*tree_c5))'''