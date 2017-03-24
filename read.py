import pickle
with open('accounts.dat', 'rb') as f:
    l = pickle.load(f)
    
for i in l:
    print("Name: %s\nEmail: %s\nPassword: %s\n\n" % (i[0], i[1], i[2]))
