
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template



@route('/<letter>')
def diamondEddy(letter: str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    diamond= ""
    for i in range(26):
        if (alphabet[i] == letter):
            number = i + 1
        i+=1


    outside_space = number-1
    inside_space = 1

    for i in range(number):
        if(alphabet[i] == "A"):
            diamond += ((" " * (outside_space)) + alphabet[i] + " " * (outside_space) + "\n")
        else:
            diamond += ((" " * (outside_space)) + alphabet[i] + (" " * inside_space) + alphabet[i] + (" " * (outside_space)) + "\n")
            inside_space += 2

        outside_space -= 1



    outside_space +=2
    inside_space -= 4





    for i in reversed(range(number-1)):


        if(alphabet[i] == "A"):
            # print(outside_space) # -1
            # print(inside_space) # 13
            diamond += ((" " * (outside_space)) + alphabet[i] + " " * (outside_space) + "\n")

        else:
            diamond += ((" " * (outside_space)) + alphabet[i] + (" " * inside_space) + alphabet[i] + (" " * (outside_space)) + "\n")
            inside_space -= 2


        outside_space += 1

    if (alphabet[i] == "A"):
        output = template('./diamondHTML.tpl', diamond=diamond)
        return output




application = default_app()