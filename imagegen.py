import random
import pickle
from sklearn import tree
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

    return total

def like(t):
    #whether you like the image or not
    if input("te gusta hombre? (y/n)\n") == "y":
        name = 'training.dat'
        with open(name, 'rb') as f:
            l = pickle.load(f)

        l[1].append(t)
        l[0] += 1
        #print(l)
        
        with open(name, 'wb') as f:
            pickle.dump(l,f)

        im = Image.new("RGB", (8, 8))
        pix = im.load()
        for x in range(8):
            for y in range(8):
                if t[y][x] == "█":
                    pix[x,y] = (0,0,0)
                else:
                    pix[x,y] = (255,255,255)
        im.save("sprites/%d.png" % l[0], "PNG")
        
    else:
        like(run(8))

def find_adjacent(l):
    pass

def learn(width):
    name = 'training.dat'
    with open(name, 'rb') as f:
        l = pickle.load(f)
        l = l[1]
    if l == []:
        return run(width)

    features = []
    labels = []

    for sprite in l:
        for i, row in enumerate(sprite):
            for j, s in enumerate(row): #s is the individual items in each row
                #-1 means there is no character adjacenct to the current character
                up      =   choices.index(sprite[i-1][j]) if i != 0 else -1 #the item above the current
                down    =   choices.index(sprite[i+1][j]) if i != width - 1 else -1
                left    =   choices.index(sprite[i][j-1]) if j != 0 else -1
                right   =   choices.index(sprite[i][j+1]) if j != width - 1 else -1

##                features.append([up, down, left, right, i, j])
                features.append([up, left, i, j]) #only up and left because down and right haven't been generated yet
                labels.append(choices.index(s))
                #print(up, down, left, right)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)

    total = []
    for i in range(width):
        total.append([])
        for j in range(width):
            total[i].append("")

    #random indices to create a fixed char (in order to randomize results)
    fixed_i, fixed_j = random.randint(0, width-1), random.randint(0, width-1)
    total[fixed_i][fixed_j] = choices[random.randint(0, len(choices)-1)]

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
    for i in range(width):
        for j in range(width):
            if i == fixed_i and j == fixed_j:
                continue
            up      =   choices.index(total[i-1][j]) if i != 0 else -1 #the item above the current
            #down    =   choices.index(total[i+1][j]) if i != width - 1 else -1
            left    =   choices.index(total[i][j-1]) if j != 0 else -1
            #right   =   choices.index(total[i][j+1]) if j != width - 1 else -1
            
##            x = clf.predict([[up, down, left, right, i, j]])[0]
            x = clf.predict([[up, left, i, j]])[0]
            total[i][j] = choices[x]        
        
    for l in total:
        strng = ""
        for sl in l:
            strng += sl
        print(strng)

    return total
    #print(clf.predict())
clear(0)
while True:      
    like(learn(8))


    
