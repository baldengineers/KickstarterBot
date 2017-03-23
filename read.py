import pickle
with open('accounts.dat', 'rb') as f:
    print(pickle.load(f))
