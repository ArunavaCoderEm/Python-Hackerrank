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

# # # # # THIS MUCH TOOK ME TO GOLD BADGE PYTHON # # # #

# # # # # HACKERRANK NUMBER LINE JUMPS
def kangaroo(x1, v1, x2, v2):
    sum1 = x1 + v1
    sum2 = x2 + v2
    while (sum1 != sum2 and x1 >= 0 and x2 > 0 and v1 >= 1 and v2 >= 1 and x1 < x2 and sum1 <= 10000000):            
            sum1 = x1 + v1
            x1 += v1
            sum2 = x2 + v2
            x2 += v2
    if (sum1 == sum2):
            return ("YES")
    else:
            return ("NO")
        
y = kangaroo(0,2,5,3)
print(y)


# # # # HACKERRANK BILL DIVISION

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    sumla = int(sum(bill)/2)
    if (sumla == b):
        print("Bon Appetit")   
    else:
        print(abs(b-sumla)) 

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)


# # # HACKERRANK SUB-ARRAY DIVISION

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0
    for i in range (0,len(s)-m+1):
        x = 0
        for j in range (i,i+m):
            x += s[j]
        if (x == d):
            count += 1
    return (count)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

# # # HACKERRANK COUNTING VALLEYS
def countingValleys(steps, path):
    valley = 0
    seaL = 0
    for i in range (0,steps):
        if (path[i] == 'U'):
            seaL += 1
        elif (path[i] == 'D'):
            seaL -= 1
        if (seaL == 0 and path[i] == 'U'):
            valley += 1
    print(valley)

# # # # HACKERRANK DAY OF A PROGRAMMER 

def dayOfProgrammer(year):
    if (year >= 1700 and year <= 1917):
        if (year % 4 == 0):
            date = f'12.09.{year}'
        else :
            date = f'13.09.{year}'
    if (year == 1918):
        date = f'31.08.{year}'
    if (year >= 1919 and year <= 2700):
        if (year % 400 == 0 and year % 100 == 0):
            date = f'12.09.{year}'
        elif (year % 4 == 0 and year % 100 != 0):
            date = f'12.09.{year}'
        else :
            date = f'13.09.{year}'
    return date

# # # HACKERRANK DESIGNER PDF VIEWER
import math
import os
import random
import re
import sys



def designerPdfViewer(h, word):
    l = int(len(word))
    alph = []
    for i in range (0,l):
            if (word[i] == 'a'):
                    alph.append(h[0])
            if (word[i] == 'b'):
                    alph.append(h[1])
            if (word[i] == 'c'):
                    alph.append(h[2])
            if (word[i] == 'd'):
                    alph.append(h[3])
            if (word[i] == 'e'):
                    alph.append(h[4])
            if (word[i] == 'f'):
                    alph.append(h[5])
            if (word[i] == 'g'):
                    alph.append(h[6])
            if (word[i] == 'h'):
                    alph.append(h[7])
            if (word[i] == 'i'):
                    alph.append(h[8])
            if (word[i] == 'j'):
                    alph.append(h[9])
            if (word[i] == 'k'):
                    alph.append(h[10])
            if (word[i] == 'l'):
                    alph.append(h[11])
            if (word[i] == 'm'):
                    alph.append(h[12])
            if (word[i] == 'n'):
                    alph.append(h[13])
            if (word[i] == 'o'):
                    alph.append(h[14])
            if (word[i] == 'p'):
                    alph.append(h[15])
            if (word[i] == 'q'):
                    alph.append(h[16])
            if (word[i] == 'r'):
                    alph.append(h[17])
            if (word[i] == 's'):
                    alph.append(h[18])
            if (word[i] == 't'):
                    alph.append(h[19])
            if (word[i] == 'u'):
                    alph.append(h[20])
            if (word[i] == 'v'):
                    alph.append(h[21])
            if (word[i] == 'w'):
                    alph.append(h[22])
            if (word[i] == 'x'):
                    alph.append(h[23])
            if (word[i] == 'y'):
                    alph.append(h[24])
            if (word[i] == 'z'):
                    alph.append(h[25])
    area = max(alph)*l    
    return area   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

# # # HACKERRANK SALES BY MATCH
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    setar = list(set(ar))
    count = []
    sum = 0
    for i in range (0, len(setar)):
        x = ar.count(setar[i])
        count.append(x)

    for j in range (0, len(count)):
        if (count[j] % 2 == 0):
            sum += (count[j] // 2 )
        elif (count[j] % 2 != 0 and count[j] > 2):
            if ((count[j]-1) % 2 == 0):
                sum += ((count[j]-1) // 2 )
    return (sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# # # # HACKERRANK CAMELCASE

import math
import os
import random
import re
import sys

def camelcase(s):
    count = 1
    for i in range (0,len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            count += 1
    return (count)


from typing import List
# sliding window
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        i = 0
        j = i + 2
        if(len(nums) == 1): return False
        while(i < len(nums)):
            if(sum(nums[i:j]) % k == 0 and len(nums[i:j]) >= 2): 
                return True
            else : j += 1
            if(j > len(nums)):
                i += 1
                j = i + 2
        return False 
# DP table
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if(len(nums) < 2): return False
        numsum = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            numsum[i] = numsum[i-1] + nums[i-1]
        print(numsum)
        for j in range(len(nums) - 1):
            for m in range(j+2, len(nums) + 1):
                if(numsum[m] - numsum[j]) % k == 0: return True
        return False
     
sol = Solution()
x = sol.checkSubarraySum([23,2,6,4,7],13)
print(x)   


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = (10**9) + 7
        res = [1]*n
        presum = [1]*(n)
        j = 0
        while(j < k):
            for i in range(1,n):
                presum[i] = res[i] + presum[i-1]
            res = presum
            j += 1
        ansp = presum[-1]
        ans = ansp % mod
        return ans
        
    
sol = Solution()
x = sol.valueAfterKSeconds(5,3)
print(x)

from typing import List
from collections import Counter
import numpy as np

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = []
        for i in arr2:
            res += [i]*c[i]
            del c[i]
        resi = sorted(c)
        for j in resi:
            res += [j] * c[j]
        return res

sol = Solution()
print(sol.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))

def diff(a,b):
    return a-b
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        med = int (np.median(arr))
        print(med)
        res = []
        for i in range(len(arr)):
            res.append([abs(arr[i] - med), arr[i]])
        res.sort()
        res.reverse()
        ans = []
        for j in range (k):
            ans.append(res[j][1])
        return ans
sol = Solution()
print(sol.getStrongest([1,2,3,4,5],2))

from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(len(hours) - 1):
            for j in range(i+1, len(hours)):
                if((hours[i] + hours[j]) % 24 == 0): count += 1
        return count

class Solution:
    # Hint 2 .. has given the answer only LOL
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        res = [0]*24
        for j in hours:
            count += res[(24-(j%24)) % 24]
            res[j % 24] += 1
        return count

sol = Solution()
print(sol.countCompleteDayPairs([12,12,30,24,24]))

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = i + 1
        m = len(nums1)
        n = len(nums2)
        mi = min(m,n)
        while(i < len(mi)):
            if(nums1[i:j] == nums2[i:j]): j += 1
            pass
        
        
sol = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(sol.findLength(nums1,nums2))


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if (n == 0 or k == 0): return 0
        fr = [i for i in range(1,n+1)]
        st = 0
        size = n
        while(size > 1):
            st = (st + k -1) % size
            fr.pop(st)
            size -= 1
        return fr[0]
    
sol = Solution()
print(sol.findTheWinner(6,5))

class Solution:
    def maximumSwap(self, num: int) -> int:
        res = list(map(int, list(str(num))))
        i = res.index(max(res))
        j = res.index(min(res))
        if(i != 0 and j < i):
            res[i], res[j] = res[j], res[i]
        summ = 0
        for i in res: summ = (10 * summ) + i
        return summ

sol = Solution()
print(sol.maximumSwap(9973))

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if(i != "../" and i != './'): stack.append(i)
            elif(i == './'): continue
            elif(len(stack) and i == '../'):
                stack.pop()
            print(stack)
        return len(stack)
    
sol = Solution()
print(sol.minOperations(["d1/","d2/","../","d21/","./"]))

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
	    
        pos = 2
        criticalpts = []
        
        if (head is None or head.next is None or head.next.next is None):
            return [-1, -1]

        start = head
        mid = start.next
        end = mid.next
        
        while (end):
            if(mid.val > start.val and mid.val > end.val): 
                criticalpts.append(pos)
            if(mid.val < start.val and mid.val < end.val): 
                criticalpts.append(pos)
                
            start = mid
            mid = start.next
            end = mid.next
            pos += 1
        
        if(len(criticalpts) == 2): 
            maxdiff = abs(criticalpts[0] - criticalpts[1])
            mindiff = abs(criticalpts[0] - criticalpts[1]) 
            return [mindiff, maxdiff]
        
        print(criticalpts)
        if(len(criticalpts) < 2): return [-1,-1]

        maxdiff = abs(criticalpts[0] - criticalpts[-1])
        mindiff = float("inf") 
        
        for i in range(0,len(criticalpts) - 1):
            mindiff = min(mindiff, abs(criticalpts[i] - criticalpts[i + 1]))
        
        return [mindiff, maxdiff]


# Drivers code
 
head = ListNode(5)
temp1 = ListNode(3)
temp2 = ListNode(1)
temp3 = ListNode(2)
temp4 = ListNode(5)
temp5 = ListNode(1)
temp6 = ListNode(2)

head.next = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
temp4.next = temp5
temp5.next = temp6

sol = Solution()
print(sol.nodesBetweenCriticalPoints(head))


from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        if (board[0][0] == 'O'):
            return False
        x_count = 0
        o_count = 0
        for i in board:
            res = list(i)
            for j in res:
                if (j == 'O'): 
                   o_count += 1
                elif (j == 'X'):
                   x_count += 1
        if(x_count != o_count): return False
        if(board[1][1] == board[1][2] == board[1][0] and x_count == o_count): return False
        if(board[2][1] == board[2][2] == board[2][0] and x_count == o_count): return False
        if(board[0][1] == board[0][2] == board[0][0] and x_count == o_count): return False
        if(board[0][0] == board[1][0] == board[2][0] and x_count == o_count): return False
        if(board[0][1] == board[1][1] == board[2][1] and x_count == o_count): return False
        if(board[0][2] == board[1][2] == board[2][2] and x_count == o_count): return False
        if(board[0][0] == board[1][1] == board[2][2] and x_count == o_count): return False
        if(board[0][2] == board[1][1] == board[2][0] and x_count == o_count): return False
        return True
        
sol = Solution()
board = ["XXX","   ","OOO"]
print(sol.validTicTacToe(board))


class Solution:
    def reverseParentheses(self, s: str) -> str:

        stk = [] 
        
        que = []
        
        for i in s:
            if (i != ")"):
                stk.append(i)
            if (i == ")"):
                popstk = stk.pop()
                while (popstk != "("):
                    que.append(popstk)
                    popstk = stk.pop()
                    
            while(len(que)):
                popque = que.pop(0)
                stk.append(popque)
        
        retstr = "".join(stk)
        return retstr
        
# drivers code

sol = Solution()
driverip = "(ed(et(oc))el)"
print(sol.reverseParentheses(driverip))

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stk = [num[0]]
        i = 1        
        
        
        while (i < len(num)):
            while (k > 0):
                if (len(stk) and stk[-1] > num[i]):
                    k -= 1
                    stk.pop()
                else: break
            stk.append(num[i])
            i += 1
            
        while (k > 0):
            stk.pop()
            k -= 1

        while (len(stk) and stk[0] == "0"): stk.pop(0)
            
        retres = ""

        retres = "".join(stk)
        
        return "0" if (retres == "") else retres


from typing import List, Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        num_set = set(nums)
        compo = 0
        
        if(len(nums) == 1): return 1
        if(head == None): return None
        if(head.next == None):
            x = head.val
            if(x in nums): return 1
            
        temp = head
        
        print(nums)
        
        while(temp != None):
            if (temp.val in num_set and (temp.next is None or temp.next.val not in num_set)):
                compo += 1
            temp = temp.next
        
        return compo
    
    
sol = Solution()

nums = [0,3,1,4]


node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

print(sol.numComponents(head, nums))


## Ezz bit manipulation 
## xor is 1 when between different bits 
## that's why the differbits function acts like that

def differbits(m, n):
    difbit = m ^ n
    difbitbin = bin(difbit)[2:]
    res = difbitbin.count('1')
    return res
    
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        totalhamdist = 0
        for i in range(32): 
            count = 0
            flag = (1 << i)
            for num in nums:
                if (num & flag):
                    count += 1
            totalhamdist += count * (len(nums) - count)
        return totalhamdist

## same brute force that got TLE
from typing import List

def differbits(m, n):
    difbit = m ^ n
    difbitbin = bin(difbit)[2:]
    res = difbitbin.count('1')
    return res
    
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        totalhamdist = 0
        for i in range (0, len(nums) - 1):
            for j in range (i + 1, len(nums)):
                res = differbits(nums[i], nums[j])
                totalhamdist += res
        return totalhamdist
             
sol = Solution()
nums = [4,14,2]
print(sol.totalHammingDistance(nums))


class Solution:
    def reverseVowels(self, s: str) -> str:
        
        i = 0
        j = len(s) - 1

        s = list(s)
        
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while (i < j):
            if (s[i] in vow and s[j] in vow):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                print(s, i, j)
            elif (s[i] in vow and s[j] not in vow):
                j -= 1
                print(s, i, j)
            elif (s[j] in vow and s[i] not in vow):
                i += 1
                print(s, i, j)
            
            elif (s[i] not in vow and s[j] not in vow):
                i += 1
                j -= 1
        
        res = "".join(s)
        
        return res
    
sol = Solution()
s = "aA"
print(sol.reverseVowels(s))

def remstr (s, top, next, greed):

    stk = []
    res = 0

    for i in s:
        if (len(stk) and stk[-1] == top and i == next):
            stk.pop()
            res += greed
        else :
            stk.append(i)
    
    ans = ''.join(stk)
    
    return [ans, res]

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if (not len(s)): return 0
        if (x == 0 and y == 0): return 0
        
        # if my greed is x 
        if (x > y) :
            pt1 = remstr(s, 'a', 'b', x)[1]
            s = remstr(s, 'a', 'b', x)[0]
            pt2 = remstr(s, 'b', 'a', y)[1]
            s = remstr(s, 'b', 'a', y)[0]
            
        # if not   
        elif (y > x) :
            pt1 = remstr(s, 'a', 'b', y)[1]
            s = remstr(s, 'a', 'b', y)[0]
            pt2 = remstr(s, 'b', 'a', x)[1]
            s = remstr(s, 'b', 'a', x)[0]
        
        return pt1 + pt2
            
        
sol = Solution()
s = "cdbcbbaaabab"
x = 4
y = 5
print(sol.maximumGain(s,x,y))

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        zercount = nums.count(0)
        
        newlist = []
        
        for i in nums:
            if (i != 0):
                newlist.append(i)
        
        res = newlist + ([0]*zercount)
        
        nums = res[:]
            

sol = Solution()
nums = [0,1,0,3,12]
print(sol.moveZeroes(nums))

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        if(not len(nums)): return 0

        nums.sort()
        ope = 0
        
        i = 0
        j = len(nums) - 1
        
        while (i < j):
            
            if (nums[i] + nums[j] < k):
                i += 1
            elif (nums[i] + nums[j] > k):
                j -= 1
            elif (nums[i] + nums[j] == k):
                ope += 1
                i += 1
                j -= 1
        
        return ope                
    
sol = Solution()
nums = [3,1,3,4,3]
k = 6
print(sol.maxOperations(nums,k))        


from typing import List

def issafe(board, row, col, n):
    j = 0
    while j < col:
        if (board[row][j]): return False
        j += 1

    i = row
    j = col
    while (i >= 0 and j >= 0):
        if board[i][j]: return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while (j >= 0 and i < n):
        if board[i][j]: return False
        i += 1
        j -= 1
    
    return True

def solveQutil(board, col, n, finalres):
    if (col >= n): 
        finalres.append(["".join('Q' if board[i][j] else '.' for j in range(n)) for i in range(n)])
        return
    for i in range(n):
        if (issafe(board, i, col, n)):
            board[i][col] = 1
            solveQutil(board, col+1, n, finalres)
            board[i][col] = 0

def solver(n):
    board = [[0]*n for _ in range(n)]
    res = []
    solveQutil(board, 0, n, res)
    return res
    

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if(n == 1): return [["Q"]]
        return solver(n)

sol = Solution()
n = 4
print(sol.solveNQueens(n))


from typing import List

def greaterCount(arr, val):
    return sum(1 for i in arr if i > val)

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        for i in range (2, len(nums)):
            count1 = greaterCount(arr1, nums[i])
            count2 = greaterCount(arr2, nums[i])
            
            if count1 > count2:
                arr1.append(nums[i])   
            elif count1 < count2:
                arr2.append(nums[i])  
            else:
                if len(arr1) > len(arr2):
                    arr2.append(nums[i])
                elif len(arr1) < len(arr2):
                    arr1.append(nums[i])
                else:
                    arr1.append(nums[i])
                    
        return arr1 + arr2
    
sol = Solution()
nums = [2,1,3,3]
 
print(sol.resultArray(nums))
 
 
class Solution:
    def minimumSteps(self, s: str) -> int:
        res = list(s)
        count = 0
        
        i = 0
        j = i + 1
        
        while(j < len(res)):
            if(res[i] == '0' and res[j] == '0'):
                j += 1
                if (j >= len(res)): break
                
            if(res[i] == '0' and res[j] == '1'):
                i += 1
                j = i + 1
                if (j >= len(res)): break

            if(res[i] == '1' and res[j] == '0'):
                res[i], res[j] = res[j], res[i]
                i += 1
                j = i + 1
                count += 1
                if (j >= len(res)): break
                    
            if(res[i] == '1' and res[j] == '1'):
                j += 1
                if (j >= len(res)): break
                
            
        return count
            
        
sol = Solution()
s = '0111'
print(sol.minimumSteps(s))



def count_vowels(s: str) -> int:
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
    
    return count

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        maxvow = float("-inf")
        
        i = 0
        j = i + k
        
        while(j <= len(s)):
            cnt = count_vowels(s[i:j])
            if(cnt > maxvow):
                maxvow = cnt
                i += 1
                j = i + k
            else:
                i += 1
                j = i + k
        
        return maxvow                
            
        
        
sol = Solution()
s = "leetcode"
k = 3
print(sol.maxVowels(s,k))

class Solution:
    def romanToInt(self, s: str) -> int:
        
        romhash = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        rom_to_dig = 0
        i = 0
    
        while (i < len(s)):
            
            
            # remember this and works from left to right
            # so rohash and i < len(s) - 1 gives you index error
            # but this code first check index then move is fine
            # this took 20 mins for me to figure out !!!!!
            
            if (i < len(s) - 1 and romhash[s[i]] < romhash[s[i+1]]):
                res = romhash[s[i + 1]] - romhash[s[i]]
                rom_to_dig += res
                i += 2

            else :
                res = romhash[s[i]]
                rom_to_dig += res
                i += 1

        return rom_to_dig
    
sol = Solution()
s = "VIII"
print(sol.romanToInt(s))


##


from typing import List

def givepos(posarr):
    return posarr[0]

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        stk = []

        robotstats = []

        for i in range(len(positions)):
            ans = [positions[i], healths[i], directions[i], i]      
            robotstats.append(ans)
            
        print(robotstats)
        
        robotstatssort = sorted(robotstats, key = givepos)

        for j in robotstatssort:

            if (j[2] == 'L'):

                while (len(stk) and stk[-1][2] == 'R' and stk[-1][1] < j[1]):
                    stk.pop()
                    j[1] = j[1] - 1
                    
                if (not len(stk) or stk[-1][2] == 'L'):
                    stk.append(j)
                    
                elif (len(stk) and stk[-1][1] == j[1]):
                    stk.pop()
                    
                elif (len(stk) and stk[-1][1] > j[1]):
                    stk[-1][1] -= 1
                    
            else :
                stk.append(j)
                
        retres = []
        
        for k in stk:
            retres.append(k[1])
            
            
        if (not len(retres)): return []
            
        healths_index = {element: index for index, element in enumerate(healths)}

        ordered_retres = sorted(retres, key=lambda x: healths_index[x])
        
        return ordered_retres

        
        

sol = Solution()
pos = [1,2,5,6]
he = [10,10,11,11]
dire = "RLRL"
print(sol.survivedRobotsHealths(pos, he, dire))

from typing import List

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        
        stack = [ast[0]]

        for i in range (1, len(ast)):
            
            if (not len(stack) or ((stack[-1] > 0 and ast[i] > 0) or (stack[-1] < 0 and ast[i] < 0))):

                stack.append(ast[i])

            else :
                if (abs(stack[-1]) > abs(ast[i])):
                    continue
                
                elif (abs(stack[-1]) < abs(ast[i])):

                    while (len(stack) and abs(stack[-1]) < abs(ast[i]) and (ast[i] < 0 and stack[-1] > 0) or (ast[i] > 0 and stack[-1] < 0)):
                        print("hi")
                        stack.pop()
                        
                    if (not len(stack) or ((stack[-1] > 0 and ast[i] > 0) or (stack[-1] < 0 and ast[i] < 0))):
                        stack.append(ast[i])
                        
                elif (abs(stack[-1]) == abs(ast[i])):
                        stack.pop()
                        continue
                    
        return stack
    
sol = Solution()

ast = [-2,2,1,-2]

print(sol.asteroidCollision(ast))

# from typing import List
                        
                        
# class Solution:
#     def asteroidCollision(self, ast: List[int]) -> List[int]:
        
#         stack = [ast[0]]

#         for i in range (1, len(ast)):
            
#             if (not len(stack) or ((stack[-1] > 0 and ast[i] > 0) or (stack[-1] < 0 and ast[i] < 0))):

#                 stack.append(ast[i])




from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:  

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        
        print(nums_set)
        
        if (not head): return None
        
        
        while (head.val in nums_set):
            head = head.next
        
        temp = head

        while (temp.next != None):
            
            if (temp.next.val in nums_set):
                temp.next = temp.next.next
            else:
                temp = temp.next
                
        return head

# Another approach

def appendll (head, new_data):

        new_node = ListNode(new_data)

        if head is None:
            head = new_node
            return
        last = head
        while (last.next):
            last = last.next
 
        last.next = new_node

        return head
    
    
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        
        print(nums_set)
        
        rethead = ListNode(None)
        
        if (not head): return None
        
        while (head != None):
            if (head.val not in nums_set):
                print("hi")
                rethead = appendll(rethead, head.val)
                print(head.val)
            head = head.next
                
        return rethead.next

                
                
sol = Solution()
nums = [1,2,3]
head4 = ListNode(5)
head3 = ListNode(4, head4)
head2 = ListNode(3, head3)
head1 = ListNode(2, head2)
head = ListNode(1, head1)
print(sol.modifiedList(nums,head))


from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        res = []
        temp = head
        while (temp != None):
            res.append(temp.val)
            temp = temp.next

        print(res)
        
        m = res.index(x)
        if (m == -1): return None
        
        le, ri = 0, m+1
        
        while (le <= m or ri < len(res)):
            
            if (res[le] < x and res[ri]):
                le += 1

sol = Solution()
x = 3
head5 = ListNode(2)
head4 = ListNode(5,head5)
head3 = ListNode(2,head4)
head2 = ListNode(3,head3)
head1 = ListNode(4,head2)
head = ListNode(1,head1)
print(sol.partition(head, x)) 

from typing import List
import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def checkprofit(idx, allowbuy, dyp, lt, lim):
            
            if (idx == len(prices)): return 0
            
            if (lt >= lim): return 0
            
            if (dyp[idx][allowbuy][lt] != -1): return dyp[idx][allowbuy][lt]

            if (allowbuy):
                profit = max(-prices[idx] + checkprofit(idx + 1, 0, dyp, lt, lim), checkprofit(idx + 1, 1, dyp, lt, lim))
            else:
                profit = max(prices[idx] + checkprofit(idx + 1, 1, dyp, lt + 1, lim), checkprofit(idx + 1, 0, dyp, lt, lim))
    
            dyp[idx][allowbuy][lt] = profit

            return profit 
        
        n = len(prices)
        
        dimensions = (n, 2, 3) 

        dyp = np.full(dimensions, -1)

        print(dyp)

        resprof = checkprofit(0, 1, dyp, 0, 2)
        
        return resprof
        
        
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

from typing import List
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = i + 1

        while (i <= len(nums)):
            print(nums[i:j])
            if(sum(nums[i:j]) >= k):
                return len(nums[i:j])

            else: j += 1
            if (j > len(nums)):

                i += 1
                j = i + 1

        return -1

sol = Solution()
print(sol.shortestSubarray([2,-1,2],3))

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1]*len(nums)
        mx = max(nums)
        m = nums.index(mx)
        res[0] = nums[0]
        if (m+1 < len(nums)):
            res[m + 1] = mx
        i = 0
        j = 0
        
        
        while (i < len(nums)):
                
            if (i == m + 1 or i == m): 
                i += 1
                if (i >= len(nums)): break
            
            elif (nums[i] >= nums[j]):
                j += 1    
                if (j >= len(nums)): j = 0    
                
            else:
                res[i] = nums[j]
                i += 1
                j = i + 1
                if (j >= len(nums)): j = 0
        
        res[m] = -1
                
        return res
    
sol = Solution()
res = [1,5,3,6,8]
print(sol.nextGreaterElements(res))



class Solution:
    def minLength(self, s: str) -> int:
        while ("AB" in s or "CD" in s):
            if ("AB" in s):
                s = s.replace("AB", "")
            elif ("CD" in s):
                s = s.replace("CD", "")
        return len(s)

s = "ACBBD"               
sol = Solution()
print(sol.minLength(s))

import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        punc = "!"
        nums = "1234567890"
        
        allowed = ".-"
        
        if (len(sentence) == 1 and sentence[0] in nums or sentence[0] in punc or sentence[0] in allowed): return 0

        split_sen = re.split(r'\s+', sentence)
        
        print(split_sen)

        count = 0

        for i in split_sen:
            if (any(char in punc for char in i) or any(char in nums for char in i)):
                count += 1
        return len(split_sen) - count
    
s = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."               
sol = Solution()
print(sol.countValidWords(s))

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        ress1 = ''.join(sorted(s1))
        ress2 = ''.join(sorted(s2))
        
        can_s1 = True
        can_s2 = True
        
        for i in range(len(ress1)):
            if (ress1[i] < ress2[i]):
                can_s1 = False
            if (ress2[i] < ress1[i]):
                can_s2 = False
        
        return can_s1 or can_s2


s1 = "abc"
s2 = "xya"
sol = Solution()
print(sol.checkIfCanBreak(s1, s2))

from typing import List

def arrStartDep(arr):
    st = []
    en = []
    for i in arr:
        st.append(i[0])  
        en.append(i[1]) 
    return [st, en]

def returnSmallest(arr):
    return arr[0]

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        n = len(times)
        chairs = [False] * n
        
        arrival, departure = arrStartDep(times)

        indexed_times = [(times[i][0], times[i][1], i) for i in range(n)]
        
        indexed_times.sort(key= returnSmallest)  
        
        for arrival, departure, original_index in indexed_times:
            for k in range(n):
                if chairs[k] and departure <= arrival:
                    chairs[k] = False  
            
            for j in range(n):
                if not chairs[j]: 
                    chairs[j] = True  
                    break
            
            if original_index == targetFriend:
                return j  

        
            
sol = Solution()
times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(sol.smallestChair(times, targetFriend))