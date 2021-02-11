def chicken_talk_list(input):
    """
        speak chicken talk by transforming text into intermitent upper and lower case
        
        ex  input: "thank you for your help"
            output: "ThAnK YoU FoR YoUr hElP"
        Args: input text that you want to use

        Return: chicken talk ready to be pasted anywhere
    """
    chicken_talk_l =[]
    count = -1
    for i in input:
        count = count+1
        if count%2 == 0:
            chicken_talk_l.append(i.upper())
        else:
            chicken_talk_l.append(i.lower())
    return chicken_talk_l

def chicken_talk_string(output1):
    str1 = ""
    for e in output1:
        str1 += e
    return str1

def solve():
    output1 = chicken_talk_list ("Hello there")
    output2 = chicken_talk_string(output1)
    print(output2)


def main():
    solve()

if __name__ == "__main__":
    main()

