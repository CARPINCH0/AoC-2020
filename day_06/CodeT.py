#!/usr/bin/env python3

'''

each letter signifies a question that was answered positively

each empty line indicates a new group

the objective of this excercise is to create a count of how many times each groups have had the same answers to the same questions, and add that count across groups

the first step is to splitline the input into a list of strings containing all the individual answers separated by commas, and each group separated by an empty space.

after the lines are 

'''

    
def solve():
    """ Open the input.txt file as input, splits the input into different groups and people

        Returns: a set of shared answers between the group
    """
    
    def read_input(input):
        """ splits the input into a list of comma separated values 
            Args: the input that is to be split

            Return: the input split into a list
        """
        with open(input, 'r') as openned_input:
            clean_input = openned_input.read().splitlines()
            return clean_input
    
    def groups (clean_input):
        """ splits the clean_input list into sets containing the groups and counts the number of shared answers in each
        
            Args: the clean_input list of comma separated answers with an empty space separating the groups

            Return: running_count; the count of answers they have in common
        """
        answers = set()
        for person in clean_input:
            running_count = 0
            if person:
                print(person)
                answers.add(person)

            else:
                print(answers)
                group = answers[0].intersection(*answers)
                answers= set()
                shared_question_count = len(group)
                running_count = shared_question_count + running_count
        return running_count

    clean_input = read_input("inputT.txt")
    result = groups(clean_input)
    print(result)



def main():
    solve()

if __name__ == "__main__":
    main()


""" Create tests for each function and rebuild the code structure so that the functions can be called individually for testing"""


