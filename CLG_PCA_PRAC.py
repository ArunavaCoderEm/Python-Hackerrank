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
