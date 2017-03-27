import random

choices = ["█", " ", "▓", "▒", "░"]

def run(width):
    total = []
    for i in range(width):
        total.append([])
        for j in range(width):
            total[i].append("")
    if width % 2 != 0:
        for i in range(width):
            f = choices[random.randint(0,4)]
            total[i][int((width-1)/2)] = f


    for i in range(width):
        if width % 2 != 0:
            for j in range(int((width-1)/2)):
                x = choices[random.randint(0,4)]
                total[i][j] = x
                total[i][width-1-j] = x
        else:
            for j in range(int(width/2)):
                x = choices[random.randint(0,4)]
                total[i][j] = x
                total[i][width-j-1] = x                
        
    for l in total:
        strng = ""
        for sl in l:
            strng += sl
        print(strng)

run(8)
    
