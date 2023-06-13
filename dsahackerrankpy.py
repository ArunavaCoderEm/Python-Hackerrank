# # # # HACKERRANK  # # # #

# # #  HACKERRANK PERCENTAGE

name_marks = {}
x = int(input())

for i in range (0,x):
        name,m1,m2,m3 = list(float,input().split())
        m1 = float(m1)
        m2 = float(m2)
        m3 = float(m3)
        list = [m1,m2,m3]
        name_marks [name] = list 
     
y = input() 
z = (sum(name_marks[y]))/3
if ((len(str(z)))>= 5):
        print(round(z,2))
elif ((len(str(z))) == 4):
        d = str(z)+'0'
        print(d)
elif ((len(str(z))) == 3):
        m = str(z)+'0'
        print(m)
elif ((len(str(z))) == 2):
        f = str(z)+'.00'
        print(f)
elif ((len(str(z))) == 1):
        l = str(z)+'.00'
        print(l)

# # # RUNNER UP SCORE HACKERRANK
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    ar = list(arr)
    ar.sort()
    print(ar[(len(ar)-2)])

# # # HACKERRANK SWAPCASE
n = input()
z = n.swapcase()
print(z)
# # # # OR
def swap_case(s):
    y = s.swapcase()
    return (y)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# # # HACKERRAnK MUTATION
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string
        
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# # # #
l = ['Arunava','Dutta']
string = ' '.join(l)
print(string)

# # # #
c = 'Arunava Dutta'
z = list(c)
print(z)

# # # HACKERRANK FIND A STRING
x = 'ABCDCDC'
y = 'CDC'
print(x.find(y))

# # #
x = [1,2,3,4,5]
print(sum(x))

# # # HACKERRANK PLUS MINUS

def plusMinus(arr):
        pos = 0
        zero = 0
        neg = 0
        c = len(arr)
        for i in arr:
                if (i<0):
                        neg = neg + 1
                elif (i == 0):
                        zero = zero + 1
                elif (i > 0):
                        pos = pos + 1
        print(f'{pos/c}\n{neg/c}\n{zero/c}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# # # HACKERRANK STAIRCASE
n = int(input())
for i in range (1,n+1):
        print(" "*(n+1-i)+('#'*i))
def staircase(num_stairs):
    # Write your code here
    n = num_stairs - 2
    for stairs in range(1, num_stairs):
        print(' ' * n, '#' * stairs)
        n -= 1
    print('#' * num_stairs)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

# # # MIN MAX SUM HACKERRANK

def miniMaxSum(arr):
    ar = list(arr)
    ar.sort()
    maxx = (ar[1]+ar[2]+ar[3]+ar[4])
    minn = (ar[0]+ar[1]+ar[2]+ar[3])
    return (print(minn,maxx))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

# # # HACKERRANK COMPARE TRIPLETS
def compareTriplets (a,b):
        alice = 0
        bob = 0
        for i in range (0,3):
                if (a[i]>b[i]):
                        alice = alice + 1
                elif (b[i]>a[i]):        
                        bob = bob + 1
                elif (a[i] == b[i]):
                        alice += 0
                        bob += 0
        print ([alice,bob])
a = list (map(int, input().split()))
b = list (map(int, input().split()))
compareTriplets(a,b)

# # # HACKERRANK BIRTHDAY CAKE CANDLES
def birthdayCakeCandles(candles):
    # Write your code here
        z = max (candles)
        return (candles.count(z))

candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)
print(result)

# # # HACKERRANK TIME COMVERSION
def timeConversion(s):
        j = (s[0:(len(s)-2)])
        k = (s[2:(len(s)-2)])
        z = int(j[0:2])

        if ('PM' in s and z == 12) :
                z = (z + 0)
        if ('PM' in s and z < 12) :
                z = (z + (12))
        if ('AM' in s and z == 12) :
                z = (z - 12)
        if ('PM' in s and z < 12) :
                z = (z + 0)
        if ((len(str(z))) == 1):
                print(f'{0}{z}{k}')
        elif ((len(str(z)))> 1):
                print(f'{z}{k}')

timeConversion ('07:05:45PM')

# # # HACKERRANK CAT AND MOUSE
# abs() is like positive mod function in maths
def catAndMouse(x, y, z):
        j = abs (z-x)
        k = abs (z-y)
        if (j > k):
                return ('Cat B')
        elif (k > j):
                return ('Cat A')
        elif (k == j):
                return ('Mouse C')

# # # HACKERRANK DIVISION SUM PAIRS
ar = [1,2,3,4,5,6]
k = 5
count = 0
for i in range (0,len(ar)):
        for j in range ((i+1),len(ar)):
                z = ar[i] + ar[j]
                if ((z % k) == 0):
                       count = count + 1
print(count)

# # # HACKERRANK MIGRATORY BIRDS
def migratoryBirds(arr):
        l = [0] * len(arr)
        for i in range (0,len(arr)):
                l[arr[i]] += 1
        return l.index(max(l))

    
x = migratoryBirds([1, 2, 3, 4 ,5, 4, 3, 2 ,1 ,3 ,4])
print(x)
        
        
# # # HACKERRANK ANGRY PROFFESSOR
a = [-2,-1,0,1,2]
k = 3
count = 0
for i in a :
        if (i <= 0):
                count = count + 1
if (count >= k):
        print('YES')
elif (count < k):
        print('NO')

# # # HACKERRANK HURDLE RACE
k = 7
height = [2,5,4,5,2]
for i in height:
        if (i > k):
                z = (max(height) - k)
        if (i < k):
                z = 0
print(z) 
# # # #  SAME AS ABOVE
def hurdleRace(k, height):
        height.sort()
        if (height[(len(height)-1)] > k):
               z = (height[(len(height)-1)]) - k
        elif (height[(len(height)-1)] < k):
               z = 0   
        return(z) 

# # # HACKERRRANK GRADING SYSTEM
def gradingStudents(grades):
        
        for i in range (0,len(grades)):
                if (grades[i]>= 38):
                        if ((grades[i] + 1) % 5 == 0):
                                grades[i] = grades[i] + 1
                        elif ((grades[i] + 2)% 5 == 0):
                                grades[i] = grades[i] + 2
                        else :
                                grades[i] = grades[i]

        return (grades)  

x = gradingStudents ([73,67,38,33])           
print(x)

# # # HACKERRANK MOVIES BEAUTIFUL DAYS
def beautifulDays(i, j, k):
        count = 0
        def rev_num(num):
                sum = 0
                while (num>0):
                        rem = num % 10
                        sum = sum*10 + rem
                        num = num // 10
                return (sum)
        for c in range (i,(j+1)):
                z = rev_num(c)
                
                if (((abs(z-c))%k)==0):
                        count = count + 1
        return (count)
o = beautifulDays(20,23,6)
print(o)
# # # HACKERRANK DIAGONAL DIFFERENCE


# # # HACKERRANK PYTHON HASH FUNCTION
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
print(hash(tuple(integer_list)))

### HACKERRANK PYTHON TEXT WRAP
# fill gives directly in new line wrap gives in list with max widths
import textwrap
a = "klfsjgkfsdjgfdjg"
x = textwrap.wrap(a,5)
print(x)
import textwrap
def wrap(string, max_width):
        return (textwrap.fill(string,max_width))        
a=wrap ("arunavadutta",2)
print(a)


### PYTHON HACKERRANK CAPITALIZE
def solve(s):
    return ' '.join(i.capitalize() for i in s.split(' '))

w = solve("arunava dutta how are you AND")
print(w)

# iterables


# # # HACKERRANK ITERABLES
import itertools
from itertools import product
A = (map(int, input().rstrip().split()))
B = (map(int, input().rstrip().split()))

result = list(itertools.product(A,B))
for i in result:
        print(i,end=" ")

# # #
width = 20
print("HACKERRANK".ljust(width,'.'))
print("HACKERRANK".rjust(width,'#'))
print("HACKERRANK".center(width,'-'))

# # # HACKERRANK PERMUTATIONS ITERTOOLS
# TO JOIN FROM LIST TO STRING "SPACES I WANT TO GIVE BETWEEN WORDS".JOIN(LIST) TO SEPERATE FROM STRING TO LIST STRING.SPLIT("SPACES FROM WHAT I WANT TO SEPERATE")
import itertools
from itertools import permutations
S,k = (input().split())
k = int(k)
S = sorted(str(S))
result = list(itertools.permutations(S,k))
for i in result:
        print("".join(i))
list = ["Arunava","Dutta","Hello"]
print("".join(list))
print(" ".join(list))
string = "Arunava Dutta Hello  Hi"
print(string.split(" "))
print(string.split(" "))

# # # HACKERRANK COMBINATIONS
import itertools
S,K = (input().split())
K = int(K)
S = sorted(str(S))
for j in range(1,K+1):
    result = list(itertools.combinations(S,j))
    for i in result:
        print("".join(i))


    
    
# # # HACKERRANK SETS DISTINCT TREE HEIGHT
def average(array):
    array = set(array)
    z = sum(array)
    f = z/len(array)
    return(f)

# # # HACKERRANK POLAR FORM
# CMATH IS A LIBRARY FOR THESE COMPLEX AND POLAR FORMS

import cmath
c = complex(input().strip())

result = cmath.polar(c)
for i in result:
        print(i)

# # # HACKERRANK CALENDER

import calendar
m,d,y = map(int,input().split(" "))
z = (calendar.weekday(y,m,d))
if (z == 0):
        print("MONDAY")
elif (z == 1):
        print("TUESDAY")
elif (z == 2):
        print("WEDNESDAY")
elif (z == 3):
        print("THURSDAY")
elif (z == 4):
        print("FRIDAY")
elif (z == 5):
        print("SATURDAY")
elif (z == 6):
        print("SUNDAY")

# # # HACKERRANK SAMPLE TEST
def fizzBuzz(n):
    for i in range (1,n+1):
        if (i%3 == 0 and i%5 ==0):
            print("FizzBuzz")
        elif(i%3==0 and i %5 !=0):
            print("Fizz")
        elif(i%3!=0 and i %5 ==0):
            print("Buzz")
        elif(i%3!=0 and i %5 !=0):
            print(i)
fizzBuzz(15)

# # # # HACKERRANK TEST
def findMedian(arr):
    arr.sort()
    c = int((len(arr)-1)/2)
    return(arr[c])

arr = [1,3,2]
print(findMedian(arr))

# # # HACKERRANK NESTED LIST
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())



# # # HACKERRANK LONELY INTEGER
n = int(input())
a = int(input().split())

def lonelyinteger(a):
        for i in range (0,len(a)):
                if (a.count(a[i]) == 1):
                        return (a[i])

# # HACKERRANK FIND STRING
def count_substring(string, sub_string):
        count = 0
        start = 0
        while start < len(string):
                index = string.find(sub_string,start)
                if index == -1:
                        break
                count += 1
                start = index + 1

        return count
z = count_substring("ABCDCDC","CDC")
print(z)

# # # HACKERRANK TEXT-ALIGNMENT

# # # HACKERRANK STRING VALIDATORS

# # # # HACKERRANK C CODE IN PYTHON EASY
num_list = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
n = int(input("num ? "))
if (n <= 9):
    for i in range (0,n):
        print(num_list[i])
elif (n > 9):
        for i in range (0,9):
            print(num_list[i])

        for j in range (10,n+1):
            if (j % 2 == 0):
                print("Even")
            else :
                print("Odd")

# # # HACKERRANK SYMMETRIC DIFFERENCE
list1=[]
list2=[]
list3=[]
M = int(input())
x = (input().split())
for i in x:
        list1.append(int(i))
N = int(input())        
y = (input().split())
for j in y:
        list2.append(int(j))
c = (set(list1).difference(set(list2)))
d = (set(list2).difference(set(list1)))
for p in c:
        list3.append(p)
for r in d:
        list3.append(r)
list3.sort()
for t in list3:
        print(t)

# # # HACKERRANK DEFAULT DICT TUTORIAL
# CRAZY THIS HAS A LIBRARY ITSELF AND I AM CODING IT RAW STILL MANAGED IT
n,m = map(int,input().split())
A = []
B = []
for i in range (0,n):
        x = input()
        A.append(x)
for j in range (0,m):
        y = input()
        B.append(y)
for k in range (0,len(B)):
        for u in range (0,len(A)):
                if (B[k] == A[u]):
                        print(u+1,end=" ")
        print()

# # # HACKERRANK LIST PROBLEM
n = int(input())
v = []
for i in range (n):
    c = input().split()
    if (c[0] == 'append'):
        v.append(int(c[1]))
    elif (c[0] == 'print'):
        print(v)
    elif (c[0] == 'insert'):
        v.insert(int(c[1]),int(c[2]))
    elif (c[0] == 'reverse'):
            v.reverse()
    elif (c[0] == 'remove'):
        v.remove(int(c[1]))
    elif (c[0] == 'sort'):
        v.sort()
    elif (c[0] == 'pop'):
        v.pop()

# # # HACKERRANK SET PROBLEM
listcont = []
N = int(input())
for i in range (0,N):
    x = input()
    listcont.append(x)
ycont = set(listcont)
print(len(ycont))

# # # HACKERRANK EXCEPTIONS
T = int(input())
for i in range (0,T):
    try:
        a,b = map(str,input().split())
        print (int(a)//int(b))
    except Exception as e:
        print ("Error Code:",e)