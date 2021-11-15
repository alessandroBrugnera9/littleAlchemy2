import pickle

COMBINATIONS="combinations"

def saveObj(obj, name):
    with open(name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def saveString(string, name):
    with open(name + "txt", "w+'") as f:
        f.write(string)


def loadObj(name):
    with open(name + '.pkl', 'rb+') as f:
        return pickle.load(f)
