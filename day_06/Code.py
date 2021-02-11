'''
each letter signifies a question that was answered positively

each empty line indicates a new group

the objective of this excercise is to create a count of how many times each all groups have had the same answers to the same questions.

question1 = {0} # a set containing all the answers for a particular person in a group
question2 = {0} # a set containing all the answers from the first person on the group
line_count = 0 # the number of people in a group
question_count = 0 # the number of same questions that were answered by a group across all groups
shared_questions = {0} # the total list of quesions for a particular group

'''  
  
def solve(input):
    """ Splits the input into different groups and people

    Args: list of strings, representing the answers for everyone in the plane

    Returns: a set of shared answers between the group
    """
    line_count = 0
    shared_questions = set()
    question1 = set()
    question2 = set()
    question_count = 0
    for line in input:
        line_count = line_count+1
        if line != "\n":
            for character in line:
                if character != "\n":
                    question1.add(character) # we add each answer to the set containing all answers for this particular person
                else:
                    if line_count == 1:
                        question2 = question1 # the first person on the group initializes the list of answers to be compared to all other lists of answers
                    shared_questions = question1.intersection(question2) # the list of answers are compared to eachother
                    print("Questions: " + str(question1))
                    question1 = set() # we reset the question list to be ready to be filled by the next group of answers
        else:

            question_count = question_count + len(shared_questions) # we add the number of shared answers to the running tally of how many shared answers were contained on each group
            print ("shared questions: " + str(shared_questions))
            print("share question count: " + str(len(shared_questions)))
            print("running count: " + str(question_count))
            print("")
            shared_questions = set()
            line_count = 0
            question1 = set()
            question2 = set()

with open('input.txt', 'r') as input:
     solve(input)
