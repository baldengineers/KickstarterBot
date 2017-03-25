import pickle

def read_accounts():
    with open('accounts.dat', 'rb') as f:
        l = pickle.load(f)
    return l
    
if __name__ == '__main__':    
    l = read_accounts()
    for i in l:
        print("Name: %s\nEmail: %s\nPassword: %s\n" % (i[0], i[1], i[2]))
