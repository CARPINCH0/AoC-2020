'''
each letter signifies a question that was answered positively

each empty line indicates a new group

going to create a line_count of all the unique question1 that have been answered by everyone


'''


question1 = {0} #a set containing all the answers that were shared across a group of people
question2 = {0}
line_count = 0 # the number of people in a group
question_count = 0 # the number of same question1 that were answered by a group across all groups
shared_questions = {0} # the total list of quesions for a particular group
    
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
                    question1.add(character)
                else:
                    if line_count == 1:
                        question2 = question1
                    shared_questions = question1.intersection(question2)
                    print("Questions: " + str(question1))
                    question1 = set()
        else:

            question_count = question_count + len(shared_questions)
            print ("shared questions: " + str(shared_questions))
            print("share question count: " + str(len(shared_questions)))
            print("running count: " + str(question_count))
            print("")
            shared_questions = set()
            line_count = 0
            question1 = set()
            question2 = set()
    return (question_count)

def split_and_compare_quesions (character):
    if character != "\n":
        question1.add(character)
    else:
        if line_count == 1:
            question2 = question1
        shared_questions = question1.intersection(question2)
        print("question1: " + str(question1))
        print("question2: " + str(question2))
    return shared_questions

with open('input.txt', 'r') as input:
     solve(input)
