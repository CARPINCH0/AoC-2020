''' two numbers from the input need to add to 2020 and be multiplied together to give the answer

we need to 
1 transform the input list into a python list.
2 export that list to the Code
3 compare each value to each other value on the list
4 return the two values that euql 2020

'''

input = open("input.txt","r")

dirty_i=input.readlines()
clean_i=[]

for ele in dirty_i:
    ele2=ele[:-1]
    clean_i.append(ele2)

target = int(2020)

for value in clean_i:
    for value2 in clean_i:
        for value3 in clean_i:
            result = int(value) + int(value2) +int(value3)
            answer = int(value) * int(value2) *int(value3)
            if result == target:
                print ("answer: " + value + "+" + value2 + "+" + value3 + "=" + str(answer))


