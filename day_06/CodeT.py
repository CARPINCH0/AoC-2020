'''
each letter signifies a question that was answered positively

each empty line indicates a new group

count how many unique questions were answered by each group and add them

Collections.Counter manual https://docs.python.org/3/library/collections.html#collections.Counter

'''
from collections import Counter

group =[]
questions = []
unique_questions = []
unique_questions_count = 0
    
def spit_questions(input, group, questions):
    group =[]
    questions = []
    unique_questions = []
    unique_questions_count = 0
    for line in input:
        if line != "\n":
            for character in line:
                if character != "\n":
                    questions.append(character)
        else: 
            unique_questions = Counter(questions).keys()
            unique_questions_count = unique_questions_count + len(unique_questions)
            group.append(questions)
            print(questions)
            questions = []
            print (unique_questions_count)
    group.append(questions)
    return group


with open('inputT.txt', 'r') as input:
    group = spit_questions(input, group, questions)

