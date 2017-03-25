import pickle
with open('accounts.dat', 'rb') as f:
    l = pickle.load(f)

names = []
rm = []
for i in l:
    if i[0] not in names:
        names.append(i[0])
    else:
        print(i[0], " is in names")
        rm.append(l.index(i))

l[:] = [ item for i,item in enumerate(l) if i not in rm ]
print(l)


##    
##with open('accounts.dat', 'wb') as f:
##    pickle.dump(l, f)
