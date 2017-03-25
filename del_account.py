import pickle

# use the below to delete the latest entry 
with open('accounts.dat', 'rb') as f:
    l = pickle.load(f)

l.pop(-1)

with open('accounts.dat', 'wb') as f:
    pickle.dump(l, f)
