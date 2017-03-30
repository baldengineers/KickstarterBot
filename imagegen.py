import random
import pickle
from sklearn import tree
from pprint import pprint
from PIL import Image

##choices = ["█", " ", "▓", "▒", "░"]
choices = ["█", " "]

def clear(p):
    if p:
        name = 'training.dat'
        with open(name, 'rb') as f:
            l = pickle.load(f)

        l = l[1][:-1]
        
        with open(name, 'wb') as f:
            pickle.dump(l,f)


        
    else:
        with open("training.dat", "wb") as f:
            pickle.dump([0,[]],f)

def run(width):
    total = []
    for i in range(width):
        total.append([])
        for j in range(width):
            total[i].append("")
    if width % 2 != 0:
        for i in range(width):
            f = choices[random.randint(0,len(choices)-1)]
            total[i][int((width-1)/2)] = f


    for i in range(width):
        if width % 2 != 0:
            for j in range(int((width-1)/2)):
                x = choices[random.randint(0,len(choices)-1)]
                total[i][j] = x
                total[i][width-1-j] = x
        else:
            for j in range(int(width/2)):
                x = choices[random.randint(0,len(choices)-1)]
                total[i][j] = x
                total[i][width-j-1] = x                
        
    for l in total:
        strng = ""
        for sl in l:
            strng += sl
        print(strng)

    return sprite_to_num(total)

def like(t):
    #whether you like the image or not
    name = 'training.dat'
    with open(name, 'rb') as f:
        l = pickle.load(f)

    ans = input("te gusta hombre? (y/n)\n")
    if ans == "y":
        #print('appending to yes list:', t)
        l[1].append([t, 1]) # tell computer you like the image

        im = Image.new("RGB", (8, 8))
        pix = im.load()
        for x in range(8):
            for y in range(8):
                if t[y][x] == "█":
                    pix[x,y] = (0,0,0)
                else:
                    pix[x,y] = (255,255,255)
        im.save("sprites/%d.png" % l[0], "PNG")
    elif ans == "n":
        #print('appending to no list:', t)
        l[1].append([t, 0]) # tell computer you do not like the image
        l[0] += 1
        #print(l)
    else:
        return

    with open(name, 'wb') as f:
        pickle.dump(l,f)

def sprite_to_num(sprite):
    #converts sprite into a readable format for sklearn
    for i, row in enumerate(sprite):
        s = ""
        for j, char in enumerate(row): #char is the individual items in each row
            s += str(choices.index(char))
        sprite[i] = s

    return sprite

def learn(width):
    name = 'training.dat'
    with open(name, 'rb') as f:
        l = pickle.load(f)
        l = l[1]
    if l == []:
        #pass
        return run(width)

    features = []
    labels = []

##    for sprite in l:
##        for i, row in enumerate(sprite):
##            for j, s in enumerate(row): #s is the individual items in each row
##                #-1 means there is no character adjacenct to the current character
##                up      =   choices.index(sprite[i-1][j]) if i != 0 else -1 #the item above the current
##                down    =   choices.index(sprite[i+1][j]) if i != width - 1 else -1
##                left    =   choices.index(sprite[i][j-1]) if j != 0 else -1
##                right   =   choices.index(sprite[i][j+1]) if j != width - 1 else -1
##
##                #features.append([up, down, left, right, i, j])
##                features.append([up, left, i, j]) #only up and left because down and right haven't been generated yet
##                labels.append(choices.index(s))
##                #print(up, down, left, right)

    for sprite in l:
##        pprint(sprite[0])
##        s = sprite_to_num(sprite[0])
        
        features.append(sprite[0])
        labels.append(sprite[1])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    #random indices to create a fixed char (in order to randomize results)
    #fixed_i, fixed_j = random.randint(0, width-1), random.randint(0, width-1)
    #total[fixed_i][fixed_j] = choices[random.randint(0, len(choices)-1)]

##    if width % 2 != 0:
##        for i in range(width):
##            f = choices[random.randint(0,len(choices)-1)]
##            total[i][int((width-1)/2)] = f
##
##
##    for i in range(width):
##        if width % 2 != 0:
##            for j in range(int((width-1)/2)):
##                x = choices[random.randint(0,len(choices)-1)]
##                total[i][j] = x
##                total[i][width-1-j] = x
##        else:
##    for i in range(width):
##        for j in range(width):
##            #if i == fixed_i and j == fixed_j:
##            #    continue
##            up      =   choices.index(total[i-1][j]) if i != 0 else -1 #the item above the current
##            #down    =   choices.index(total[i+1][j]) if i != width - 1 else -1
##            left    =   choices.index(total[i][j-1]) if j != 0 else -1
##            #right   =   choices.index(total[i][j+1]) if j != width - 1 else -1
            
##            x = clf.predict([[up, down, left, right, i, j]])[0]
##            x = clf.predict([[up, left, i, j]])[0]
    total = run(width)
    #t = sprite_to_num(total)
##    print('total: ')
##    pprint(total)
    x = clf.predict([total])
    if x:
        print("Computer says YES: ")
        pprint(total)
    else:
        print("Computer says NO: ")
        pprint(total)

    return total
    #print(clf.predict())
#clear(0) #1 if remove last one, 0 if all
while True:
    #like(run(8))
    like(learn(8))


    
