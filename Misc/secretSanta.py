from random import shuffle

def createGraph(names : list) -> dict:
    tmp = names
    shuffle(tmp)

    identifier = dict()
    for idx in range(len(tmp)):
        identifier[tmp[idx]] = tmp[(idx + 1)%len(tmp)]  

    return identifier

def printGraph(identifier : dict) -> None:
    for name in identifier.keys():
        print(f'{name} -> {identifier[name]}')

names = ['A', 'B', 'D', 'E', 'Ma', 'Mi', 'Mo', 'Sa']

printGraph(createGraph(names)) 