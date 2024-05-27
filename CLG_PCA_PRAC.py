# ORDERED TUPLE FROM EXTERNAL LIST
test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
ord_list = ['Geeks', 'best', 'CS', 'Gfg']
res = []
dik = dict(test_list)
for i in ord_list:
    if(i in dik.keys()):
        res.append((i,dik[i]))
print(res)

# STONE PAPER SCISSOR
import random 
def play():
    c = ['stone','paper','scissors']
    x = random.choice(c)
    print('computer has choosen something \n choose yours - ')
    f = input('enter your choice - ').lower()
    if(x == 'stone'):
        if(f == 'paper'): print(f'You win PC choosed {x}')
        elif(f == 'scissors'):print(f"you lose PC choosed {x}")
        else: print(f"It's a Draw PC choosed {x}")
    elif(x == 'paper'):
        if(f == 'stone'): print(f'You lose PC choosed {x}')
        elif(f == 'scissors'):print(f"you won PC choosed {x}")
        else: print(f"It's a Draw PC choosed {x}")
    elif(x == 'scissors'):
        if(f == 'paper'): print(f'You lose PC choosed {x}')
        elif(f == 'stone'):print(f"you won PC choosed {x}")
        else: print(f"It's a Draw PC choosed {x}")
play()
v = input("wanna play more ? (y // n) - ").lower()
while(v != 'n'):
    play()
    v = input("wanna play more ? (y // n) - ").lower()


## HANGMAN
word_pool = ["kitty", "dog", "teeth", "sitting"]
word = word_pool[0]  
encoded_word = ["_"] * len(word)
print(" ".join(encoded_word))
human = ['head','body','hands','legs']
while(len(human) != 0):
    guess = input("Which letter do you want to guess? ")
    if guess in word:
        print(f"Yes, {guess} is correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                encoded_word[i] = guess
    
        print(" ".join(encoded_word))
    else:
        print(f"No, {guess} isn't correct!")
        hang = human.pop()
        print(f"{hang} HANGED ! Remains {human}")
    if("".join(encoded_word) == word):
        break

if(encoded_word != guess and len(human) == 0):
    print("You lose human hanged")
elif(encoded_word == word and len(human) != 0):
    print("you win human not hanged")

# Guess Number
import random
def play():
    x = random.randint(1,10)
    print("You have 5 tries to guess the Number , PC ALREADY CHOOSEN ONE")
    for i in range(1,6):
        y = int(input("Enter guess here - "))
        if(x > y):
            print(f"Try something higher - YOU {y} ; TRIES - {5-i}")
        elif(x < y):
            print(f"Try something lower - YOU {y} ; TRIES - {5-i}")
        else:
            print(f"You won in {5-i} tries, you and PC both choosed {y}")
            break
    if(y != x and i == 5):
        print(f"You lost PC choosed {x} and you choosed {y}")

m = 'y'
while(m != 'n'):
    play()
    m = input('wanna play more (y // n) ? ')

#pangram
def pan(sentence):
    x = 'abcdefghijklmnopqrstuvwx'
    for i in x:
        if(i not in sentence):
            return False
    return True
sentence = input("enter - ").lower()
if(pan(sentence)):print("pangram")
else:print('not pangram')
    
## robot move
inix,iniy = 0,0
m = 'y'
while(m != 'n'):
    dir = input("(up/down/left/right) which direction ? ").lower()
    if(dir == 'up'):
        h = int(input("How much up ? "))
        iniy += h
    
    if(dir == 'down'):
        h = int(input("How much down ? "))
        iniy -= h
    
    if(dir == 'right'):
        h = int(input("How much right ? "))
        inix += h
    
    if(dir == 'left'):
        h = int(input("How much left ? "))
        inix -= h
    m = input("wanna move robot again ? (y/n) - ")
print(inix,iniy)
dis = ((inix ** 2) + (iniy ** 2))**0.5
print(f"Robot is {dis} distance from origin")

# combination of any number
import itertools
num = 123
nums = list(str(num))
nums = [int(i) for i in nums]
comb = list(itertools.permutations(nums, len(nums)))
print(comb)


#beta variate
import random
import matplotlib.pyplot as plt 
l = 5
h = 10
n = []
for i in range (100):
    temp = random.betavariate(l,h)
    n.append(temp)
plt.hist(n)
plt.show()

## gammavariate
import random
import matplotlib.pyplot as plt 
l = 5
h = 10
n = []
for i in range (100):
    temp = random.gammavariate(l,h)
    n.append(temp)
plt.hist(n)
plt.show()

# ordered string ordered dict
from collections import OrderedDict
def check(i,p):
    d = OrderedDict.fromkeys(i)
    pl = 0
    for i,j in d.items():
        if(i == p[pl]):
            pl += 1
        if(len(p) == pl): return True
    return False

# prisoners

prisoners = list(map(int, input("Please enter prisoner arrangement - : ").strip()))
freed = 0
toggle = True
for i in range(len(prisoners)):
  if (prisoners[i] and toggle) or (not prisoners[i] and not toggle):
    freed += 1  
    toggle = not toggle
print(freed)


# A *

import heapq

def conspath(parent, nown):
    target = [nown]
    while(nown in parent):
        nown = parent[nown]
        target.append(nown)
    target.reverse()
    return target
def astar(graph,heur,start,goal):
    pq = []
    parent = {}
    heapq.heappush(pq,(heur[start],start))
    gs = {node:float('inf') for node in graph}
    fs = {node:float('inf') for node in graph}
    while(pq):
        nown = heapq.heappop(pq)[1]
        if(nown == goal):
            return conspath(parent,nown)
        for nei, cost in graph[nown]:
            tgn = gs[nown] + int(cost)
            if(tgn < gs[nei]):
                gs[nei] = tgn
                parent[nei] = nown
                fs[nei] = tgn + heur[nei]
                if(nei not in [i[1] for i in pq]):
                    heapq.heappush(pq,(fs[nei],nei))
    return None
def graphA():
    graph = {}
    n = int(input("Enter Number of vertex here - "))
    for i in range(n):
        node = input(f"Enter {i+1}th Node - ")
        nei = []
        neigh = input(f"Enter neightbour of {node} - (eg- BC) - ")
        for j in list(neigh):
            k = int(input(f"Enter cost of {j} - "))
            nei.append((str(j),int(k)))
        graph[node] = nei
    return graph
graphm = graphA()
def heuristic():
    heu = {}
    for i in graphm.keys():
        c = int(input(f"Enter heuristic cost of {i} - "))
        heu[i] = c
    return heu
heur = heuristic()
start = input("Enter Start Node - ")
goal = input("Enter Goal Node - ")
path = astar(graphm, heur, start, goal)
print(f"Path: {path}")


# DFS and BFS

visd = set()
def graphd():
    graph = {}
    n = int(input("Enter total vertex - "))
    for i in range(n):
        node = input(f"Enter {i+1} Vertex - ")
        nei = map(str,input(f"Enter neighbours of {node} - "))
        if(nei): graph[node] = list(nei)
        else: graph[node] = []
    return graph

def dfs(graph,visd,start):
    if(start not in visd):
        print(start,end=" -> ")
        visd.add(start)
    for n in graph[start]:
        dfs(graph,visd,n)

g = graphd()
dfs(g,visd,'A')
print("\n\n")
visb = []
q = []
def bfs(graph,visb,start):
    if(start not in visb):
        visb.append(start)
        q.append(start)
    while(q):
        node = q.pop(0)
        print(node, end=" -> ")
        for n in graph[node]:
            if(n not in visb):
                visb.append(n)
                q.append(n)
bfs(g,visb,'A')