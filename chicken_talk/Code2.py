"""
    speak chicken talk by transforming text into intermitent upper and lower case
    
    ex  input: "thank you for your help"
        output: "ThAnK YoU FoR YoUr hElP"
    Args: input text that you want to use

    Return: chicken talk ready to be pasted anywhere
"""


def read_input(input):
    """ open text provided and dumps it into a list
        Args: the input that is to be dumped

        Return: the input dumped into a list
    """
    with open(input, 'r') as openned_input:
        clean_input = openned_input.read()
        return clean_input

def chicken_talk_list(clean_input):
    """
        Transforms each individual line of text into a list of character with intermitent upper and lower case

        Args: clean_input; a list of the text that has been deposited on the inpute.txt

        Return: a list of chicken talk characters
    """
    chicken_talk_l =[]
    count = -1
    chicken_talk_l.append( letter for letter in clean_input where)
    for letter in clean_input:
        count = count+1
        if count%2 == 0:
            chicken_talk_l.append(letter.upper())
        else:
            chicken_talk_l.append(letter.lower())
    return chicken_talk_l

def chicken_talk_string(output1):
    """ 
        Turns the list chicken text into a string of chicken text

        Args: output1; list of chicken text

        Return: str1; string of chicken text
    """
    str1 = ""
    for letter in output1:
        str1 += letter
    return str1

def solve():
    input = read_input("input.txt")
    output1 = chicken_talk_list (input)
    output2 = chicken_talk_string(output1)
    print(output2)


def main():
    solve()

if __name__ == "__main__":
    main()

