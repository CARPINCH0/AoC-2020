'''separate the input code(nn-nn l: lllllllllll) into 4 values and add them into a list, clean them up into variables, 
use values in a code that does a count of characters and does an if statement 

the if statement would look something like this

 for each line, the password will be indexed twice, starting at position valid_p1 and valid_p2 looking for the key
    the results will then show the next position of the key, if any.
    then we compared the postion of the key to the provided values'''


valid_p1 = 0 # stands for valid position 1, the first position where the key value is found
valid_p2 = 0 # stands for valid position 2, the second position where the key value is found
key = "" # the letter that is being counted in the password
pwd = "" # the password from where the key is being couned
right_entry = 0 # count of the number of correct entries


input = open("input.txt","r")

dirty_i=input.readlines()
count=0

for line in dirty_i:
    clean=line.replace(" ",",")
    clean=clean.replace("-",",")
    clean=clean.replace("\n","")
    clean=clean.replace(":","")
    clean=clean.split(",")
    valid_p1 = int(clean[0])
    valid_p2 = int(clean[1])
    key = str(clean[2])
    pwd = str(clean[3])
    count = 0

    place1 = valid_p1-1
    place2 = valid_p2-1

    find1= pwd.find(key,place1)
    find2= pwd.find(key,place2)
    fcheck= 0
    
    if find1  == place1:
        fcheck = fcheck +1
    if find2  == place2:
        fcheck = fcheck +1
    if fcheck == 1:
        right_entry = right_entry +1
        print ("Correct!: " + str(clean))
        print(str(find1) + " - " + str(place1))
        print(str(find2) + " - " + str(place2))
    if fcheck == 2:
        print("Double find: " + str(clean))
        print(str(find1) + " - " + str(place1))
        print(str(find2) + " - " + str(place2))
    else:
        print("WRONG!" + str(clean))
        print(find1)
        print(find2)
print ("number of right entries: " + str(right_entry))
