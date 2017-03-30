import random
import pickle
from sklearn import tree

##choices = ["█", " ", "▓", "▒", "░"]
choices = ["█", " "]

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

        l.append(t)
        print(l)
        
        with open(name, 'wb') as f:
            pickle.dump(l,f)

def find_adjacent(l):
    pass

def learn(width):
    name = 'training.dat'
    with open(name, 'rb') as f:
        l = pickle.load(f)

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
    
    #print(clf.predict())
    
##while True:      
##    like(run(8))

learn(8)
    
