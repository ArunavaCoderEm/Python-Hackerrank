# # # TRUE FALSE
# # bool3= True
# # bool4= False
# # print("value of bool3 and bool4",(bool3 and bool4)) #both true and true so false
# # print("Value of bool3 or bool4",(bool3 or bool4)) #one true or true so true
# # print("Value of bool3 not bool4",(not bool4)) #given opposite so true

# # # TRUE TRUE
# # bool1= True
# # bool2= True
# # print("value bool1 and bool 2",(bool1 and bool2)) #both true and true so true
# # print("Value of bool1 1 or bool2",(bool1 or bool2)) #one true or true so true
# # print("The value of bool2",(not bool1)) #given opposite so false
# # # FALSE FALSE
# # bool5= False
# # bool6= False
# # print("value of bool5 and bool6",(bool5 and bool6)) #both true and true so false
# # print("Value of bool5 or bool6",(bool5 or bool6)) #one true or true so false
# # print("Value of bool5 not bool6",(not bool6)) #given opposite so true

# # # INPUT FUNCTION
# # a= input("Enter a number : ")
# # a= int(a)
# # print ("The value of a*a=",a*a)
# # print(type(a))

# # # STRING SLICING
# # name= "ARUNAVA"
# # print(type(name))
# # print(name[0]) # A
# # print(name[1]) # R
# # print(name[2]) # U
# # print(name[3]) # N
# # print(name[4]) # A
# # print(name[5]) # V
# # print(name[6]) # A
# # print(name[0:4]) # ARUN
# # print(name[3:6]) # NAV
# # print(name[:6]) # ARUNAV
# # print(name[1:]) # RUNAVA
# # print(name[-1]) # A 
# # print(name[-2]) # V
# # print(name[-3]) # A
# # print(name[-4]) # N
# # print(name[-5]) # U
# # print(name[-6]) # R
# # print(name[0]) # A  
# # '''WHEN GOING FORWARD THE LENGTH IT COUNTS 01234 FROM THE FIRST LETTER AND -4 -3 -2 -1 0 FROM BACKWARDS, LIKE
# # # FORWARD- 0 TO INFINITE FROM FIRST LETTER TO LAST LETTER
# # # BACKWARD- -INFINITY TO 0 FROM THE LAST LETTER TO FIRST LETTER'''
# # # STRING SKIPPING AND LENGTHS
# # me= "ARUNAVADUTTA"
# # print(len(me)) # length=12 (0 to 11)
# # print(me[0:8:2]) # Skip every 2nd letter while printing from 0 to 8 except 8 = AUAA
# # print(me[4:11:3]) # print 0 to 11 except 11 skip every 3rd letter = ADT 
# # print (me[0::2]) # print 0 to 11 (end blank=upto last) skip every 2nd letter = AUAAUT
# # print(me[:11:3]) # print from 0 (start blank=from first) to 11 skip every 3rd letter = ANAT

# # # STRING / STORY FUNCTION
# # story= "i am a very good boy.i am the boy who loves to master every prospect of life"
# # print(len(story))
# # print(story.endswith("goals")) # true or false if the story ends with goals or not = false
# # print(story.endswith("life")) # if the story ends with life or not = true
# # print(story.count("e")) # count how many letter "e" is present in story
# # print(story.count("boy")) # count how many times boy is written on story
# # print(story.count("oy")) # also counts these kinds of letters in order meaningful or not
# # print(story.count("girls")) # if there is no such word in story = 0 
# # print(story.capitalize()) # nothing have to be written in b/w, capitalizes ONLY FIRST LETTER OF FIRST LINE OF ENTIRE STORY
# # print(story.find("boy")) # will find the ONLY FIRST OCCURACE OF THE WORD IN STORY AND GIVE IT"S CHARACTER NUMBER AND NOT FIND EXCEPT 1ST ONE
# # print(story.find("of"))
# # print(story.find("i"))
# # print(story.find("girls")) # if the word to find is not in story give "-1" (word not in this story)
# # print(story.replace("good","bad")) # unlike find (finds first occurance) replace-replaces every word in story {story.replace("old","new")}

# # # ESCAPE SEQUENCE - BREAK LINE (\n) big space (\t) insert ' (\') insert \ (\\) etc
# # story1= " I love to play Guitar.\nI love to play chess" # breaks the line after (\n)
# # story2= "I love to play Guitar.I love to play\t chess" # big gap where (\t) is means big gap between play and chess
# # story3= "I love to play Guitar\'s string" # we can write normally but still apostrophee s
# # story4= "I love to pla\\y chess" # we can write normally but still a slash between a & y in play.
# # print(story1)
# # print(story2)
# # print(story3)
# # print(story4)

# # # CHAPTER 3 VIDEO PRACTICE SET
# # B= input("Good Afternoon Mr./Mrs.-")
# # print(B)
# # print(type(B)) 
# # C= input("Dear-")
# # D= input("Date-")
# # E= "You are Selected!"
# # F= print(C), print(E), print(D)
# # story5= "I  am  a  very  good  boy" # find and count double spaces in story 
# # print(story5.count("  ")) 
# # print(story5.find("  "))
# # print(story5.replace("  "," "))
# # # ALSO BEST WAY TO DO IT
# # letter= '''Dear <|NAME|>,
# #           You are selected ! for the best job which
# #           will pay you 4.5 Cr per annum working hour = 6 hrs.
# #              Joining Date : <|DATE|> '''
# # name= input("ENTER YOUR NAME : ")             
# # date= input("ENTER DATE : ")
# # letter= letter.replace("<|NAME|>",name)
# # letter= letter.replace("<|DATE|>",date)
# # print(letter)
# # # NEXT ESCAPE SEQUENCE
# # letter1= "DearSLIM,I wrote you a letter but you still aint calling." # Correct the letter format
# # letter1= "Dear\tSLIM,\n\tI wrote you a letter but you still ain\'t calling\\" # \t for tab space,\n break line, \' apostrophe,\\ slash,\anything instert anything
# # print(letter1)

# # # LIST
# # A= [9,6,8,4,324,56,23,78]
# # print(A)
# # print(A[0])
# # print(A[5])
# # print(A[7])
# # print(A[0:5])
# # print(A[2:4])
# # print(A[:6])
# # print(A[3:])
# # print(A[0:7:2])
# # print(A[:6:3])
# # print(A[1::2])
# # A.sort()
# # print(A) # commands to arrange low to high
# # A.reverse()
# # print(A) # write the same thing from backwards
# # A.append(69)
# # print(A) # will add 69 at the end of list with comma
# # A.insert(1,49) # In the list A put 49 at 1st index (9,49,8,4,324,56,23,78) after reversing as it's done before
# # print(A)
# # A.remove(23)
# # print(A)
# # # LIST AGAIN
# # B= ["ARD",45.89,True,676]
# # print(B[0])
# # (B[1])= "GODARD"
# # print(B)
# # print(type(B[3])) 
# # print(len(B))
# # B.remove(True)
# # print(B)

# # # PRACTICE SET 4
# # # 1.PRINT FRUIT LIST
# # Flist= ["apple","banana", "guava","orange","grapes", "lichi", "jackfruit"]
# # print(type(Flist))
# # print(Flist)

# # h= input("ENTER NAME OF 7 FRUITS : ")
# # print("FRUIT LIST")
# # print(h)
# # # 2.MAKE A FRUITLIST BY USER
# # f1= input("Enter first fruit :")
# # f2= input("Enter second fruit : ")
# # f3= input("Enter third fruit : ")
# # f4= input("Enter fourth fruit : ")
# # f5= input("Enter fifth fruit : ")
# # f6= input("Enter sixthh fruit : ")
# # f7= input("Enter seventh fruit : ")
# # print("FRUIT-LIST :--> ")
# # print(1.),print(f1)
# # print(2.),print(f2)
# # print(3.),print(f3)
# # print(4.),print(f4)
# # print(5.),print(f5)
# # print(6.),print(f6)
# # print(7.),print(f7)
# # MyFruitList= [f1,f2,f3,f4,f5,f6,f7]
# # print(MyFruitList)
# # # 3.STUDENTS MARKS LIST AND SORT THE LIST
# # m1= int(input("Marks Student 1 got = ")) # better start with int(....) to make sure it's int
# # m2= int(input("Marks Student 2 got = "))
# # m3= int(input("Marks Student 3 got = "))
# # m4= int(input("Marks Student 4 got = "))
# # m5= int(input("Marks Student 5 got = "))
# # m6= int(input("Marks Student 6 got = "))
# # MarksList= [m1,m2,m3,m4,m5,m6]
# # MarksList.sort()
# # print(MarksList)
# # # 4.CHECK A TUPLE CAN'T BE CHANGED
# # # tuple= (1,2,3,4,8,6,9)
# # # tuple[0]= 66 # it will throw an error cause tuple don't allow change 0th element will be 0 only not 66
# # # SUM OF 4 DIGITS OF A LIST
# # list6= [20,21,10,18]
# # print(list6)
# # print("sum of list6= ",list6[0]+list6[1]+list6[2]+list6[3]) 
# # l0= input("FIRST VALUE = ")
# # l1= input("SECOND VALUE = ")
# # l2= input("THIRD VALUE = ")
# # l3= input("FOURTH VALUE = ")
# # l0=int(l0)
# # l1=int(l1)
# # l2=int(l2)
# # l3=int(l3)
# # List8= [l0,l1,l2,l3]
# # print(List8)
# # print("SUM OF LIST_ = ", List8[0]+List8[1]+List8[2]+List8[3])
# # # 5.COUNT NUMBER OF ZEROS
# # a= (7,0,8,0,0,9)
# # print(a.count(0))
# # # DICTIONARY
# # dict1ry={
# #    "quarantine":"being in home", # LHS = Keys RHS = Values
# #    "list":[67,97,"go"],
# #    "tuple":(1,6,"no"),
# #    "marks":"69",
# #     21:22
# # }
# # print(dict1ry)
# # print(dict1ry["quarantine"]) # print given dictionary keys throws their resp values
# # print(dict1ry["list"])
# # print(dict1ry["tuple"])
# # print(dict1ry["marks"])
# # print(dict1ry[21])
# # print(dict1ry.keys()) # (keys)
# # print(dict1ry.values()) # (values)
# # print(dict1ry.items()) # (keys,values)
# # print(type(dict1ry.keys())) # dict_keys
# # print(type(dict1ry.values())) # dict_values
# # print(type(dict1ry.items())) # dict_items
# # print(type(list(dict1ry.keys()))) # turns dict_keys to list
# # print(type(list(dict1ry.values()))) # turns dict_values to list
# # print(type(list(dict1ry.items()))) # turns dict_items to list
# # updatedict1= {"sorry":"forgive",
# #               21:32}
# # dict1ry.update(updatedict1)
# # print(dict1ry)

# # dict2ry={
# #    "hii":"hello",
# #    "other":{"top":"up"}
# # }
# # print(dict2ry["hii"])
# # print(dict2ry["other"]["top"])
# # # DICTIONARY GET FUNCTION
# # dict3ry={
# #    "slimshady":"chainsaw"
# # }
# # print(dict3ry["slimshady"])  # chainsaw
# # print(dict3ry.get("slimshady")) # chainsaw
# # print(dict3ry.get("bye")) # returns "NONE" if there is no such element in given dict then (.get) throws NONE
# # '''print(dict3ry["bye"])'''  # returns "ERROR" won't work, if there is no such element in given dict then [] throws ERROR

# # # CHAPTER 5 VIDEO PRACTICE SET :-
# # # 1. Dict where user enters hindi and it returns eng translaation
# # dicthe={
# #        "भूख": "Hunger",
# #        "साधन":"tools"
# # }
# # print("options are -",dicthe.keys())
# # ahe= input("enter the hindi word-")
# # print("the meaning of your word",dicthe[ahe])
# # #2. Input 8 numbers from user and display unique number
# # n1=int(input("1-number : "))
# # n2=int(input("2-number : "))
# # n3=int(input("3-number : "))
# # n4=int(input("4-number : "))
# # n5=int(input("5-number : "))
# # n6=int(input("6-number : "))
# # n7=int(input("7-number : "))
# # n8=int(input("8-number : "))
# # set={n1,n2,n3,n4,n5,n6,n7,n8}
# # print(set)
# # #3. Can we have 18 and "18" seperately in set
# # set1={18,"18"} # yes
# # print(set1)
# # #4. length of set after 3 operations
# # s=set() # 20 and 20.0 same
# # s.add(20)
# # s.add(20.0)
# # s.add("20")
# # print(s)
# # print(len(s))
# # #5. Type of set
# # s1={} # type is dict 
# # print(type(s1))
# # s2=set() # type is empty set
# # print(type(s2))
# # #6. Empty dict friends input 
# # na1=input("name 1 ?")
# # la1=input("language 1 = ")
# # na2=input("name 2 ?")
# # la2=input("language 2 = ")
# # na3=input("name 3 ?")
# # la3=input("language 3 = ")
# # na4=input("name 4 ?")
# # la4=input("language 4 = ")
# # empdict={
# #    "name1":"lang1",
# #    "name2":"lang2",
# #    "name3":"lang3",
# #    "name4":"lang4"
# # }
# # empdict.replace("name1",na1)
# # empdict.replace("name2",na2)
# # empdict.replace("name3",na3)
# # empdict.replace("name4",na4)
# # empdict.replace("lang1",la1)
# # empdict.replace("lang2",la2)
# # empdict.replace("lang3",la3)
# # empdict.replace("lang4",la4)
# # print(empdict)
# # #6. Empty dict friends input 
# # dictionary={}
# # p1=input("Enter fav language of Arunava ")
# # p2=input("Enter fav language of sohan ")
# # p3=input("Enter fav language of zunaid ")
# # p4=input("Enter fav language of Nishan ")
# # dictionary["Arunava"]=p1
# # dictionary["sohan"]=p2
# # dictionary["zunaid"]=p3
# # dictionary["Nishan"]=p4
# # print(dictionary)
# # # Dictionary more
# # dicty={
# #    "hello":"hi",
# #    "good":"bye"
# # }
# # print(dicty)
# # print(dicty.keys())
# # print(dicty.values())
# # print(dicty.items())
# # # Enter correct password to enter problem given by Sohan.
# # passDict={
# #     "39rrty6#":"Your password is correct and you have access to servers of NASA !"
# # }
# # a=input("Enter your password here --> ")
# # print("Okay So --> ",passDict.get(a))
# # # Sets
# # Set4_={12,23,45,56,(4,3,2)}
# # Set4_.add(20)
# # print(Set4_)
# # print(Set4_.union({(33,6)}))
# # print(Set4_.intersection({22,56,(4,3,2),(4,3,1),20,99})) # {56,(4,3,2),20}
# # # If Elif Else Is In == > < <= >=
# # password=input("Enter User Password -->\t")
# # if (password=="hello1234@"):
# #       print("You Can Access To This Website.")
# # elif(password=="hello123@"):
# #       print("Forgot Password ?")
# # else:
# #       print("Worng Password So Try Again Later") 
# # #
# # ageReq=int(input("Enter Candidate Age -->\n\t"))
# # if (ageReq>25 and ageReq<60):
# #       print("Yes, You can work with us.Please Contact")
# # else:
# #       print("No You can't work  with us.Sorry")      
# # ageReq1=int(input("Enter Candidate Age -->\n\t"))
# # if (ageReq1>25 or ageReq1<60):
# #       print("Yes, You can work with us.Please Contact")
# # else:
# #       print("No You can't work  with us.Sorry")

# # crazy=input("Enter Meaning of crazy ")
# # if (crazy=="mad"):
# #       print("Correct")
# # elif (crazy=="psycho"):
# #    print("OK but find a better one ! ")
# # else:
# #    print("No, it didn't match at all")         
# # # IS IN
# # verb= "False"
# # if(verb is "True"):
# #        print("YES")
# # else:
# #       print("NO")  
# # verb_= "True"
# # if(verb_ is "True"):
# #        print("YES")
# # else:
# #       print("NO")     

# # set5_= {23, 56, 78}
# # print(23 in set5_)  
# # print(239 in set5_)  
# # print("ARDEM University of Computer Science And Engineering (ARDEM UCSE) Grade 2022")
# # StuMarks=int(input("Student Please Enter Your Academic Score Down out of 100 --> \n\t"))
# # if(StuMarks>=90 and StuMarks<=100):
# #         print("Your Grade Is 'AA',Excellent")
# # elif(StuMarks>=80 and StuMarks<90):
# #         print("Your Grade Is 'A',Good")
# # elif(StuMarks>=70 and StuMarks<=80):
# #         print("Your Grade Is 'B',Do Better")
# # elif(StuMarks>=60 and StuMarks<=70):
# #         print("Your Grade Is 'C',Study Well")
# # elif(StuMarks>=50 and StuMarks<=60):
# #         print("Your Grade Is 'D',Cosult With Teacher")
# # elif(StuMarks<50):
# #         print("Your Grade Is 'E',Bring Your Parent to School ")
# # else:
# #         print("Check Again And Fill Correctly.")
# # # Just in case
# # x__="Hello Bye"
# # x__=x__.replace("Bye","Hi") # replace is comma meaning is semi colone 
# # print(x__)

# # # 
# # dict__={
# #         "Ard":"Best",
# #         "No":"unacceptable"
# # }
# # updateD_={
# #         "Hello":"Hiii"
# # }
# # dict__.update(updateD_)
# # print(dict__)
# # # 
# # dict___={
# #         "Ard":"Best",
# #         "No":"unacceptable"
# # }
# # updateD__={
# #         "Ard":"Hiii"
# # }
# # dict___.update(updateD__)
# # print(dict___)
# #  # just in case
# # numBER= int(input("Enter the number you wanna check is odd or even --> "))
# # if(numBER%2==1):
# #         print("It's an odd number")
# # else:
# #         print("It's an even number")
# #  # just in case
# # numBER_= int(input("Enter the number you wanna check is odd or even --> "))
# # if(numBER_%2==0):
# #         print("It's an even number")
# # else:
# #         print("It's an odd number")

# # # loop
# # # 1- multiplication table
# # numm=int(input("Enter the number you want table of --> "))
# # for table in range (numm,(10*numm)+1,numm):  # as we know 1st for where to start,2nd for stop one less,
# #                                              # 3rd for skip like if 2 then write every 2nd value and skip in between
# #         print(table)
# # print("Table Done !")
# # # another way of (1)
# # numm_=int(input("Enter the number you want table of --> "))
# # for mult in range (1,11):  # it means 1 to 10     
# #         print(str(numm_) + " X "+str(mult) + " = " + str(numm_*mult))
# # # 2- greet all members start with "A"
# # list_1=["Arunava", "Sohan", "Asim", "Dibya", "Arnab", "Nishan"] # given list
# # for item in list_1: # asked machine to go through all the elements of list_1
# #         if (item.startswith("A")): # gave a condition to work on
# #                 print(item,"Good Night !") # if given condition satisfied by list_1 print given
# # # 3 - Attempt (1) not using for loop but using while loop
# # integer=int(input("Enter the number user wants Number Table of --:> \n\t"))
# # num_ber=1
# # while (num_ber<11):
# #         print(str(integer) + " X " + str(num_ber) + " = " + str(integer*num_ber))
# #         num_ber=num_ber+1
# # # 4- A given number is prime or not
# # primeNUM=int(input("Enter the number you want to check is prime or not --:> \n\t"))
# # for seqq in range(2,primeNUM):   # if given number gets divided by any number from 2 to it's own prior 
# #         if(primeNUM%seqq==0):              # number and gives no remainder then it's not prime
# #                 print(primeNUM,"It's not a prime number")
# #                 break
# # else:
# #         print(primeNUM,"It's a prime number")
# # # #
# # num1_=int(input("Enter digit number 1 --> "))
# # num2_=int(input("Enter digit number 2 --> "))
# # num3_=int(input("Enter digit number 3 --> "))
# # num4_=int(input("Enter digit number 4 --> "))
# # list__=[num1_,num2_,num3_,num4_]
# # print(list__)
# # if(num1_>num2_):
# #         f1_=num1_
# # else:
# #         f1_=num2_
# # if(num4_>num3_):
# #         f2_=num4_ 
# # else:
# #         f2_=num3_
# # if(f1_>f2_):
# #         print(f1_,", is the greatest among those 4 numbers.")
# # else:
# #         print(f2_,", is the greatest among those 4 numbers.")
# # ##
# # sub1_=int(input("Enter the number of subject 1 out of 100 :- "))
# # sub2_=int(input("Enter the number of subject 2 out of 100 :- "))
# # sub3_=int(input("Enter the number of subject 3 out of 100 :- "))
# # print("Your percentage in subject 1 is ",sub1_," % ")
# # if(sub1_<33):
# #         print("You are failed in subject 1 and so failed the total exam year.")
# # else:
# #         print("You are passed in subject 1.")
# # print("Your percentage in subject 2 is ",sub2_," % ")
# # if(sub2_<33):
# #         print("You are failed in subject 2 and so failed the total exam year.")
# # else:
# #         print("You are passed in subject 2.")
# # print("Your percentage in subject 3 is ",sub3_," % ") 
# # if(sub3_<33):
# #         print("You are failed in subject 3 and so failed the total exam year.")
# # else:
# #         print("You are passed in subject 3.")
# # print("Your total percentage is --> ",((sub1_+sub2_+sub3_)/300)*100," % ")        
# # if((((sub1_+sub2_+sub3_)/300)*100)<= 40):
# #         print("As your total marks don't cross 40 percent you fail this year.")
# # else:
# #         print('''First check for each subject you pass or not if not you are failed for the entire year and 
# #         if Yes then you crossed 40% and passed in each subject and passed the entire year.''')
# # # 5- sum of first n natural number 
# # nat_=int(input("Enter the number upto which you want the sum --> "))
# # A_=(nat_*(nat_+1))/2 # I knew it from Arithmatic Progression not loop though
# # print(A_)
# # # WHILE LOOP COUNT FROM 1 TO 15 USING IT.
# # loop = 0 # given an initial value
# # while (loop<15):
# #         loop = loop + 1
# #         print("Number" + str(loop))
# # # WHILE LOOPS TO PRINT MATERIAL OF LIST
# # list_0 = ["Arunava", "Sohan", "Nishan", "Dibya"]
# # i= -1    # -1 to get 0th element as -1+1 = 0
# # while (i < len(list_0)):
# #         i = i+1
# #         print("The Items In List Are --> " + list_0[i])
# # #
# # num1=int(input("Enter number 1 "))
# # num2=int(input("Enter number 2 "))
# # num3=int(input("Enter number 3 "))
# # num4=int(input("Enter number 4 "))
# # listt_=[num1, num2, num3, num4]
# # print(listt_)
# # #
# # UserName = input("Enter Your UserName --> ")
# # Password = input("Enter Your Password --> ")
# # count = 0
# # while (count<4):
# #         count = count + 1
# #         if (UserName == "Arunava Dutta" and Password == "Hello#1234"):
# #                 print("Access Granted You Are Logged In.")
# #                 break
# #         elif(UserName=="Arunava Dutta" or Password== "Hello#1234"):
# #                 print("Try Again Later Password and UserName Doesn't Match.")
# #                 break
# # else:
# #         print("Wrong UserName And Password Try To Log In Again.")
# # # 5- same thing but with loop
# # fruit__list =["apple", "grapes", "guava", "lichi"]
# # fruitnum = 0
# # while (fruitnum < len(fruit__list)):
# #         print(str(fruitnum) + "   " + fruit__list[fruitnum])
# #         fruitnum = fruitnum + 1
# # #
# # for i in range (1,15,4):
# #         print(i)
# # # While loop for multiplication table in different method
# # userNum = int(input("User Enter The Number --> "))
# # numT1 = 1
# # while (numT1 <= 10):
# #     print(str(userNum) + "X" + str(numT1) + "=" + str(userNum*numT1))
# #     numT1 = numT1 + 1
# # #
# # userNum = int(input("User Enter The Number --> "))
# # numT1 = userNum
# # while (numT1 <= (10*userNum)):
# #     for i_ in range (1,11):
# #         print(str(userNum) + " X " + str(i_) + " = " + str(numT1))
# #         numT1 = numT1 + userNum
# # # input value repeatation without writing again and again to make a list till it's correnct
# # password = input ("USER PLEASE ENTER YOUR PASSWORD --> ")
# # for passwoed in range (2):
# #     if (password == "ard123em"):    
# #         print("You Are Logged In.")
# #         break
# #     elif (password != "ard123em"):
# #         print(input("IT'S WRONG , ENTER YOUR PASSWORD AGAIN --> "))
# #     elif(password == "ard123em"):
# #         print("You Are Logged In.")
# # else:
# #     print("User, Your Three Tries Were Wrong So Sign-In Again")

# # # Function arguments 
# # def mysum(a,b,):
# #         return print(a+b)
# # mysum(2,5)
# # mysum(2,9)

# # def mysumm(a,b,c,d,e):
# #         return (((a+b)/(c+d))*e)
# # print(mysumm(8,9,2,1,3))
# # # 
# # def percentage (list):
# #         return ((sum(list)/500)*100)
# # list_12 = [78,89,45,34,79]
# # print(percentage(list_12))
# # #
# # def greet(name):
# #         print(f"{name}, hello , good night")
# # greet("Arunava")
# # def greet(name = "Anonymous"):
# #         print(f"{name}, hello , good night")
# # greet("Arunava")
# # greet()
# # # Recursion

# # # Lower case Identification no matter in what case actually written.Show lower case it will detect
# # with open ('file.txt','r') as q123:
# #         data66 = q123.read()
# # if ("python" in data66.lower()): # just show how it looks as lowercase it will detect in any kind of case by .lower()
# #         print("YES")
# # else:
# #         print("NO")
# # class Employee:
# #         company = "Google"
# #         salary = "5 Cr per annum"
# #         office_address = "Bangalore"
# #         post = "Software Devoloper"
# # Arunava = Employee()
# # Arunava.post = "Web Devoloper"
# # Arunava.salary = "7 Cr per annum"    # if external info available doesn't take info from class
# # print(Arunava.salary)                    # if not available takes info from class
# # print(Arunava.company)                          # if nowhere info available throws an error
# # print(Arunava.office_address)
# # print(Arunava.post)
# # def infoaboutperson(salary,company,name, post,):
# #         print(f"The salary of {name} in {company} is {salary}")
# # salary = input("Your Salary You Wanted --> ")
# # company = input("Enter the company name --> ")
# # name = input("Enter Your Name --> ")
# # infoaboutperson(salary,company,name)
# # # Renaming a file by python
# # import os
# # oldfile = 'oldfile.txt'
# # newfile = 'newfile.txt'
# # with open (oldfile,'r') as q4567:
# #         data23 = q4567.read()
# # with open (newfile,'w') as q789:
# #         q789.write(data23)
# # os.remove(oldfile)
# # # 
# # class employees :
# #         Company = "Microsoft"
# #         Salary = "6 Crore Per Annum"
# #         Post = "Software Devoloper"
# #         age_range = "From 20 to 60 years"
# #         min_exp = "They all have minimum experience on VS code for 4 years atleast."
# # Arunava = employees()
# # print(Arunava.Company)
# # print(Arunava.Salary)
# # print(Arunava.Post)
# # print(Arunava.age_range)
# # print(Arunava.min_exp)
# # # Squaring a number
# # # double star means to the power
# # # square means **2 , cube means **3 and square root means **0.5
# # a = 2
# # a = a**2
# # print(a)
# # b = 3 
# # b = b**3
# # print(b)
# # c = 9
# # c = int(c**(0.5))
# # print(c)
# # class employee:
# #     company = "google"
# #     salary = "100k $ per month"
# # Arunava = employee()
# # Arunava.company = "microsoft"
# # print(Arunava.company)

# # # Reversing a string function
# # def rvrstr(stg):
# #     for chac in range (0,len(stg)):
# #         rvr = print((stg[((len(stg)-1)-chac)]),end = "")
# #     return rvr

# # inpstr = input("Enter Your String --> ")
# # rvrstr(inpstr)
# # # Fizz-Buzz
# # numtake = int(input("Enter Your Number --> "))
# # if (numtake % 3 == 0 and numtake % 5 == 0):
# #     print("Fizz-Buzz")
# # elif (numtake % 3 == 0):
# #     print("Fizz")
# # elif (numtake % 5 == 0):
# #     print("Buzz")
# # else:
# #     print(numtake)
# # #
# # name = input("Enter Name --> ")
# # surname = input("Enter SurName --> ")
# # age = int(input("Enter Age --> "))
# # qual = input("Enter qualification --> ")
# # print(f"{name} {surname} with an age of {age} is a {qual}")
# # superhero = input(f"{name} {surname} , Which Super Hero Are You  --> ")
# # print(f"{name} {surname} is a/an {superhero}")

# # # Change Class Attributes
# # class employee:
# #         company = "google"
# #         salary = "salary is 400 dollars per day in India"
# # ard = employee()
# # print(ard.company)
# # print(ard.salary)
# # employee.company = "TOP CLASS BUSINESSMAN"
# # print(ard.company)
# # print(ard.salary)
# # class student:
# #     college = "Techno Main Salt Lake"
# #     def __init__(self):
# #         print("Student is created.") # without even calling it runs as soon as object is created under class
# #     def greet(self):
# #         print(f"Hello Student")
# #     @staticmethod
# #     def time():
# #         print("Time is 9 A.M")
# # Arunava = student()
# # print(Arunava.college)
# # Arunava.greet()
# # Arunava.time()
# # class student:
    
# #     def __init__(self,name,subject,college):
# #         self.name = name
# #         self.subject = subject
# #         self.college = college
# #         print(f"{self.name} studies {self.subject} in {self.college}")
# # Arunava = student("Arunava","CSE AIML","TMSL INDIA")

# # # 
# # class employee:
# #         def getdetails(self,name,salary):
# #                 self.name = name
# #                 self.salary = salary
# #                 print(f"The salary of {self.name} is {self.salary}")

# # Arunava = employee()
# # z=Arunava.getdetails("Arunava",10000000000000000000000)
# # print(z)
# # #
# # class calculator:
# #         def __init__(self,number):
# #                 self.number = number
       
# # class calculator:
# #         def __init__(self,number):
# #                 self.number = number

# #         def squrtsqcube(self):
# #                 print(f"The square of the number is {(self.number)**2}")

# #                 print(f"The square root of the number is {(self.number)**0.5}")
        
# #                 print(f"The cube of the number is {(self.number)**3}")
# # a =calculator(9)
# # a.squrtsqcube()
# # #
# # for i in range (1,6):
# #         print("*" * i)

# # # OR
# # i1 = 1
# # while (i1<=5):
# #         print("*" * i1)
# #         i1 = i1 + 1
         
# # # # OR 
# # i2 = 1
# # while (i2<6):
# #         print("*" * i2)
# #         i2 = i2 + 1

# # # 
# # class employee :
# #         company = "Google"
# # class programmer(employee):
# #         subunit = "YouTube"
# # Arunava = programmer()
# # a = Arunava.company
# # print(a)

# # #
# # class workspace:
# #         company = "MicroSoft"
# #         def __init__(self,name):
# #                 self.name = name
# #                 print(f"{self.name} worker is created")
        
# # class salarywork:
# #         salary = "$ 700k per month "
# # class workhour:
# #         hour = "work 6 hours a day"
# # class worker(workspace,salarywork,workhour):
# #         # def __init__(self,name):
# #         #         self.name = name
# #         #         print(f"{self.name} worker is created")
# #         day = "Work 5 days a week"

# # Arunava = worker("Arunava")
# # print(Arunava.company)
# # print(Arunava.salary)
# # print(Arunava.hour)
# # print(Arunava.day)

# # #
# # class worker:
# #         worksat = "Fiverr"
# # class freelancer(worker):
# #         def __init__ (self,name):
# #                 self.name = name
# #                 print(f"{self.name} worker is created")
# #         level = 0
# #         def upgradelevel(self):
# #                 self.level = self.level+1

# # sohon = freelancer("Sohon")
# # print(sohon.worksat)
# # print(f"Initial level is {sohon.level}")
# # sohon.upgradelevel()
# # sohon.upgradelevel()
# # print(f"After all upgradation final level is {sohon.level}")

# # class employee:
# #         company = "YT"
# # class worker:
# #         company = "Visa"
# # class new(worker,employee):
# #         salary = 400
# # # a = new()
# # # print(a.company)        
# # # print(a.salary)        

# # # #
# # class a:
# #         def __init__(self,name):
# #                 self.name = name
# #                 print(f"{self.name} is created")
# #         company = "YTR"
# # class b(a):
# #         salary = 400
# # class c(b):
# #         work = 8
# # sohon = c("sohon")
# # print(sohon.company)
# # print(sohon.salary)
# # print(sohon.work)

# # # #
# # class a:
# #         def __init__(self,name,company,salary):
# #                 self.name = name
# #                 self.company = company
# #                 self.salary = salary
# #                 print(f"{self.name} is created")
# #         company = "YTR"
# # class b(a):
# #         salary = 400
# # class c(b):
# #         work = 8
# # sohon = c("sohon","MICROSOFT",300)  # doesn't print the parent class as latest "c" has attributes.
# # print(sohon.company)
# # print(sohon.salary)
# # print(sohon.work)

# # # super to call previous class
# # class a:
# #         company = "YT"
# #         def salary(self):
# #                 print("No Salary")
# # class b(a):
# #         def salary(self):
# #                 super().salary()     # print form a class then b class of same function salary if available.
# #                 print("400 salary")
# # class c(b):
# #         def salary(self):
# #                 super().salary()       # continuing from a class prints from both class b first then c class 
# #                                         # as c sent signal to b and b sent signal to a so started from a to b to c if available.
# #                 print("800 salary")
# # a1 = a()
# # print(a1.company)
# # a1.salary()
# # b1 = b()
# # print(b1.company)                
# # b1.salary()
# # c1 = c()
# # print(c1.company)
# # c1.salary()

# # #

# # class human:
# #         def __init__(self):
# #                 print("Human is initiated --- ")

# # class student(human):
        
# #         def __init__(self):
# #                 super().__init__()
# #                 print("Student is initiated ... ")

# # # Sohon = student("Sohon")  ## when self name argument given
# # Sohon = student()

# # class xyz:
# #         @staticmethod 
# #         def abc():
# #                 print("hdvgfcuhbdsuhvdvc")

# # po = xyz()
# # po.abc()

# # class xyzx:
# #         @staticmethod     # with static method self is just an instant attribute.
# #         def __init__(name):
                
# #                 print(f"{name} is initiated .. ")

# # poi = xyzx("Sohon")

# # # #
# # import os

# # with open ('oldfile.txt' , 'r') as q:
# #         data = q.read()
# # with open ('newfile.txt','w') as data2:
# #          data2 = data2.write(data)
# # os.remove('oldfile.txt')

# # #
# # with open ('sampletext.txt' , 'r') as q1:
# #         data1 = q1.read()
# #         print(data1)

# # #
# # for i in range (0,5):
# #         print(11**i)
# # # a
# # n = int(input("Number : "))
# # for i in range (2,n):
# #     if (n%i == 0):
# #         print(f"{n} is not a prime number")
# #         break
# # else:
# #         print(f"{n} is a prime number")

# # # e
# # def rvrstr(stg):
# #     for chac in range (0,len(stg)):
# #         rvr = print((stg[((len(stg)-1)-chac)]),end = "")
# #     return rvr
# # num = input("Number : ")
# # rvrstr(num)

# # # 6 a
# # a1 = input("element 1 : ")
# # a2 = input("element 2 : ")
# # a3 = input("element 3 : ")
# # list = [a1,a2,a3]
# # print("list - ",list)
# # tup = (a1,a2,a3)
# # print("Tuple - ",tup)
# # set = {a1,a2,a3}
# # print("set - ",set)
# # # 6 b
# # a1 = input("element 1 : ")
# # a2 = input("element 2 : ")
# # a3 = input("element 3 : ")
# # list = [a1,a2,a3]
# # x = int(input("Position :- "))
# # y = int(input("Inserted Number :- "))
# # list.insert(x,y)
# # print(list)
# # z = int(input("deleted notation : "))
# # list.remove(list[z])
# # print(list)
# # # 6 c
# # a1 = int(input("element 1 : "))
# # a2 = int(input("element 2 : "))
# # a3 = int(input("element 3 : "))
# # list = [a1,a2,a3]
# # if (a1>a2):
# #     final1 = a1
# # else:
# #     final1 = a2
# # if (final1>a3):
# #     final2 = final1
# # else:
# #     final2 = a3
# # print("MAX NUMBER IS ",final2)
# # if (a1>a2):
# #     final3 = a2
# # else:
# #     final3 = a1
# # if (final1>a3):
# #     final4 = a3
# # else:
# #     final4 = final3
# # print("MIN NUMBER IS ",final4)
# # # 6 d
# # a1 = int(input("element 1 : "))
# # a2 = int(input("element 2 : "))
# # a3 = int(input("element 3 : "))
# # list = [a1,a2,a3]
# # print(list[a1])
# # print(list[a2])
# # print(list[a3])
# # # 6 e
# # a1 = int(input("element 1 : "))
# # a2 = int(input("element 2 : "))
# # a3 = int(input("element 3 : "))
# # list = [a1,a2,a3]
# # list.sort()
# # print(list)
# # # #
# # # krishnamurthy factorial sum is number itself

# # #         print((f"{num1} is krishnamurty number."))
# # # else:
# # #         print(f"{num1} is not krishnamurty number.")

# # #
# # class xyz:
# #         def __init__ (self,name):
# #                 self.name = name
# #                 print(f"{self.name} Just Nothing.")
# #         def normal(self):
# #                 print("Xyz is normal")
# # class abc(xyz):
                
# #         def __init__(self,name):
# #                 super().__init__(name)       # super only works when parent class is proper prefer self always everywhere 
# #                 self.name = name                        # always prefer self instead of @staticmethod.
# #                 print(f"{self.name} is the best")
       
# #         def normal1(self):    
# #                 super().normal()            
# #                 print("abc is normal 1.")

# # sohan = abc("Sohan")
# # sohan.normal()
# # sohan.normal1()

# # for i in range (0,3):
# #         askuser = input("Enter Username :- ")
# #         askpass = input("Enter Password :- ")
# #         if (askuser == "Arunava Dutta" and askpass == "#qwer123"):
# #                 print("Yes You are logged in.")
# #                 break
# #         elif (askuser != "Arunava Dutta" or askpass != "#qwer123"):
# #                 print("Check Properly or you will be logged out after 3 tries.")
# #         elif (askuser != "Arunava Dutta" and askpass != "#qwer123" and i == 0):
# #                 print("Check Properly or you will be logged out after 3 tries.")        
# #         elif (askuser != "Arunava Dutta" and askpass != "#qwer123" and i == 1):
# #                 print("Check Properly or you will be logged out after 3 tries.")        
# #         elif (askuser != "Arunava Dutta" and askpass != "#qwer123" and i == 2):
# #                 print("You are logged out.")
# #                 break
# #         elif (askuser == "Arunava Dutta" and askpass != "#qwer123" and i == 2):
# #                 print("You are logged out.")
# #                 break
# #         elif (askuser != "Arunava Dutta" and askpass == "#qwer123" and i == 2):
# #                 print("You are logged out.")
# #                 break
# # #
# # class v2d:
# #         def vec1(self,i,j):
# #                 self.i = i
# #                 self.j = j
# #                 print(f"{self.i}i + {self.j}j")
# # class v3d(v2d):
# #         def vec2(self,i,j,k):
# #                 super().vec1(i,j)
# #                 self.k = k
# #                 print(f"{self.i}i + {self.j}j + {self.k}k")
# # vector = v3d()
# # vector.vec1(2,9)
# # vector.vec2(11,6,7)
# # #
# # Number = int(input("Enter the Number to Check Krishnamurthy Number = "))
# # Sum = 0
# # Temp = Number

# # while Temp > 0:
# #     fact = 1
# #     i = 1
# #     rem = Temp % 10

# #     while i <= rem:
# #         fact = fact * i
# #         i = i + 1
# #     print('Factorial of %d = %d' %(rem, fact))
# #     Sum = Sum + fact
# #     Temp = Temp // 10

# # print("The Sum of the Digits Factorials = %d" %Sum)

# # if Sum == Number:
# #     print("\n%d is a Krishnamurthy Number." %Number)
# # else:
# #     print("%d is Not a Krishnamurthy Number." %Number)
# # #
# # for i in range (1,6):
# #         for j in range (1,i+1):
# #                 # print(end=" ")
# #                 print(j,end=" ")
# # # #
# #         print()
# # #
# # from math import factorial
 
# # n = 5
# # for i in range(n):
# #     for j in range(n-i+1):
 
        
# #         print(end=" ")
 
# #     for j in range(i+1):

# #         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    
# #     print()
# # # 
# # n = int(input ("Input Number N - "))
# # s = " "
# # for i in range (1,n+1,2):
# #         print(f"{s}{ i }" ,end = "")
# # #
# # s = " "
# # for i in range (0,101,5):
# #         print(f"{s} {100-i}",end = "")
# # #
# # n = int(input("Number : "))
# # s =" "
# # for i in range(1,n+1):

# #      j=(i**3)+1

# #      print(f"{s}{j}",end="")
# # #
# # for i in range (1,6):
# #         for j in range (1,16,i):
# #                 print(j)
# # #
# # # n = int(input("Enter Number of tries: "))

# # # step = 1

# # # count = 1

# # # while step!=n+1:

# # #    print(count)

# # #    count += step

# # #    step += pass
# # #    pass
# # # #
# # class number:
# #         def __init__(self,num1):
# #                 self.num1 = num1
                
# #         def __add__(self,num2):
# #                 self.num2 = num2
                
# #                 return (self.num1 + num2.num1)
# #         def __mul__(self,num2):
# #                 self.num2 = num2
# #                 return (self.num1 * num2.num1)
# # n1 = number(3)
# # n2 = number(5)
# # print("add is ",n1 + n2)
# # print("multiply is ",n1 * n2)
# # #
# # class number:
# #         def __init__(self,num1):
# #                 self.num1 = num1
# #         def __add__(self,num2):
# #                 self.num2 = num2
# #                 return (self.num1 + num2.num1)
# #         def __mul__(self,num2):
# #                 self.num2 = num2
# #                 return (self.num1 * num2.num1)
# #         def __str__(self):
# #                 return (f"The number is {self.num1} ")
# # n1 = number(4)
# # n2 = number(7)
# # print(n1)
# # print(n2)
# # print(n1+n2)
# # print(n1*n2)
# # # #
# # class string:
# #         def __init__(self,str):
# #                 self.str = str
# #         def __str__(self):
# #                 return (f"String is {self.str}")
# #         def __len__(self):
# #                 return 14
# # f = string("hjsgfdhg")
# # print(f)
# # print(len(f))

# # # # 
# # x = 10_000_000_000_000  # if we can't keep track of numbers we can't use commas in python so use _ won't affect the number
# # y = 10_000_000
# # print(x+y)

# # #
# # def addcalc(x,y):
# #         return print("Sum is ",x+y)
# # x1= int(input("Number 1 - "))
# # y1 = int(input("Number 2 - "))
# # addcalc(x1,y1)

# # #
# # names = ['ard','arunava','sohan','nishan','dibya','sahil','junaid']
# # length = len(names)
# # x = 1
# # while x <= length:        
# #         for i in names:
# #                 print(f"{x}. {i}")
# #                 x = x + 1
# # #
# # names = ['Arunava Dutta','Sohan Karfa','Dibyatanu Mukherjee','Zunaid Akhter','Sahil Mallick']
# # professions = ['Best and richest Businessman','Best Coder','Best Footballer','Best Doctor','Best Medic']
# # i = 1
# # j = 0
# # while (i <= len(names)):
# #         while (j < len(professions)):
# #                 for name in names:
# #                         print(f"{i}. {name} is the {professions[j]} in the world")
# #                         i = i + 1
# #                         j = j + 1

# # # To loop both or more list we can use 'zip' method ZIP METHOD - ZIP will stop after shortest length list
# # names = ['Arunava Dutta','Sohan Karfa','Dibyatanu Mukherjee','Zunaid Akhter','Sahil Mallick']
# # professions = ['Best and richest Businessman','Best Coder','Best Footballer','Best Doctor','Best Medic']
# # do = ['EMINEM','Arijit Singh','Ronaldo','Nusrat Fateh Ali Khan','Jubin Nautiyal']
# # i = 1
# # while (i <= len(names)):
# #         for (name,work,fan) in zip (names,professions,do):
# #                 print(f"{i}. {name} is the {work} in the World stans {fan}.")
# #                 i += 1
# # #
# # tuple = (1,2)
# # for i in tuple:
# #         print(i)
# # # can't have more variables than values and vice versa always values == variables for individual
# # tuple = (1,2,3)
# # (a,b,c) = (tuple)
# # print(a)
# # print(b)
# # print(c)

# # # ----        * means rest of all like -  prints a as 1 b as 2 and c as from 3 to end which rest of all except taken by a and b
# # tuple = (1,2,3,4,5,6,7,8,9)
# # a,b,c = tuple
# # print(a)
# # print(b)
# # print(c)
# # # getpass to hide input passwords it won't show what we are writing but it's actually writing
# # from getpass import getpass
# # username = input("Username - ")
# # password = getpass("password - ")
# # if (username == 'Arunava' and password == 'ard#12'):
# #         print("Logging in ...")
# # else:
# #         print("Logging out ...")
# # # 
# # with open ('use.txt','r') as f:
# #         f1 = f.read()
# # print(f1)
# # f1 = f1.replace ('stupid','#$%&@')
# # f1 = f1.replace ('shit','#$%&@')
# # f1 = f1.replace ('donkey','#$%&@')
# # with open ('use.txt','w') as f2:
# #         f2.write(f1)
# # # pattern 1
# # for i in range (0,5):
# #         print(5 * " * ")
# # i1 = 1
# # print("-----------------")
# # while i1 <= 5 :
# #         print (5 * " * ")
# #         i1 += 1
# # print("-----------------")
# # for i2 in range (1,6):
# #         print(" * " * i2)
# # print("------------------")
# # i3 = 1
# # while i3 <= 5:
# #         print(i3 * " * ")
# #         i3 = i3 + 1
# # print("-----------------")
# # for i4 in range (2,6):
# #         print ((6 - i4) * " * ")
# # print("-----------------")
# # i5 = 1
# # while i5 <= 5:
# #         print((6-i5) * " * ")
# #         i5 += 1
# # print("-----------------")
# # for i6 in range (1,6):
# #         print ()

# # print("-----------------")
# # for i2 in range (1,6):
# #         print(" * " * i2)
# # for i4 in range (2,6): 
# #         print ((6 - i4) * " * ")
# # N = int(input())
# # # Newton School
# # if N > 0:
# #     if (N % 3 == 0):
# #         print("Yes")
# #     else:
# #         print("No")
# # # ARRAY
# # # all functions are same like list tuple reverse,append,insert,pop etc

# # from array import *

# # val = array('I',[1,2,3,4,5,6,7])
# # # I - positive int , i = all int
# # print(val)
# # print(val.buffer_info())   # output = address, length of array
# # lsit = [1,5,6,3,2,9]
# # for i in range (0,len(lsit)):
# #         x= max(lsit)
# #         y= min(lsit)
# #         print(x-y)

# # #
# # # 9 a
# # # input is given already
# # class box :
# #         def __init__(self,l,b,h):
# #                 self.l = l
# #                 self.b = b
# #                 self.h = h
# #                 y = print (f'vloume of box is {self.l * self.b * self.h} unit cube')
# #                 return y

# # x = box (2,3,4)    
# # # or this one .. here user takes input (advanced)
# # class box :
# #         def __init__(self,l,b,h):
# #                 self.l = l
# #                 self.b = b
# #                 self.h = h
# #                 y = print (f'vloume of box is {self.l * self.b * self.h} unit cube')
# #                 return y
# # m = int(input('length = '))
# # n = int(input('breadth = '))
# # o = int(input('height = '))
# # x = box (m,n,o)
# # # 9 b 
# # class car:
# #         acc = 2
# #         def __init__(self, initial,time):
# #                 acc = 2
# #                 self.initial = initial
# #                 self.time = time
# #                 y = print (f'final velocity = {self.initial+(acc*self.time)}')
# #                 return y
# # ini = int(input ('initial velocity = '))
# # tacc = int(input ('time of accelaration = '))
# # toyota = car (ini,tacc)
# # # 9 d
# # class loan:
# #         def bank (self):
# #                 p = 10000
# #                 r = 1.2
# #                 t = 2
# #                 a = p*((1 + (0.01*r))**t)
# #                 return print(f'maturity amount = {a}')
# # supratim = loan()
# # supratim.bank()
# # # # 9 d advanced
# # class loan:
# #         def __init__ (self,p,r,t):
# #                 self.p = p
# #                 self.r = r
# #                 self.t = t
# #                 a = self.p*((1 + (0.01*self.r))**self.t)
# #                 return print(f'maturity amount = {a}')
# # p = int (input ('principal = '))
# # r = float (input ('rate of interest per year = '))
# # t = int (input ('duration = '))
# # nemo = loan (p,r,t)
# # # 7 a
# # with open ('sample.txt','r') as q :
# #         data = q.read()
# # print(data)
# # # 7 b
# # with open ('sample.txt', 'r') as q1 :
# #         data1 = q1.read()
# # with open ('samplenew.txt', 'w') as q2 :
# #         data2 = q2.write(data1)
# # # 7 c
# # with open ('sample.txt', 'r') as q3 :
# #         data3 = q3.read()
# # with open ('sample.txt', 'a') as q4 :
# #         data4 = q4.write(' Hello Bye.')
# # # # 7 d # give locations
# # dict = {}
# # with open("Z_OTHER_STAFFS/samplenew.txt", 'r') as f:
# #         for line in f:
# #                 (key, val) = line.split()
# #                 dict[(key)] = val

# # print (dict)

# # # IEM
# # #  OR 1
# # f = open ('xyz.txt', 'r')
# # data = f.read ()
# # f.close()
# # # 2
# # for i in range (1,4):
# #         print ('condition')
# # # 2 or ..... read() reads every word and letter but readline() reads lines by line only no words and letter 

# # # 3
# # with open ('xyz.txt', 'w') as f1 :
# #         data1 = f1.write('writing anywhere in file')
# # with open ('xyz.txt','a') as f2 :
# #         data2 = f2.append ('only writes things at the very end or at last sentence')
# # # 3 or
# # class xyz:
# #         def __init__(self):
# #                 print('Self callable function the moment instance is created due to __init__()')
# # # 4
# # x = 'jhjfihdfijdijihwdhjcodwfhjidhfief'
# # y = len(x) # prints length of x i.e how many characters are there !
# # print(y)
# # # 4 or
# # with open ('xyz.txt','a') as r:
# #         data9 = r.append('at the end')
# #         print(data9)
# # # 6
# # first = 'name'
# # second = 'surname'
# # final = (first + second)
# # print(final)
# # # 6 or
# # with open ('copyfile.txt','r') as q :
# #         copy = q.read ()
# # with open ('pastefile.txt','w') as qq:
# #         paste = qq.write(copy)
# # # 7
# # N = int(input("How many terms? "))
# # n1, n2 = 0, 1
# # count = 0
# # if N <= 0:
# #    print("Please enter a positive integer")
# # elif N == 1:
# #    print("Fibonacci sequence upto",N,":")
# #    print(n1)
# # else:
# #    print("Fibonacci sequence:")
# #    while count < N:
# #        print(n1)
# #        nth = n1 + n2
# #        n1 = n2
# #        n2 = nth
# #        count += 1
# # # 7 or
# # N1 = int(input('Terms ? '))
# # for sn in range (1,(N1)):
# #        N1 = N1 * sn 
# # print(f"{N1}")
# # # 8 or
# # def triangle(n):
# #     k = n - 1
# #     for i in range(0, n):
# #         for j in range(0, k):
# #             print(end=" ")
# #         k = k - 1
# #         for j in range(0, i+1):
         
# #             print("* ", end="")
# #         print("\r")
# # n = 6
# # triangle(n)
# # o = 1
# # while (o <= 4) :
# #         print('   |  |   ')
# #         o += 1
# # import matplotlib.pyplot as plt
# # class student :
# #         department = 'ECE'
# #         def __init__(self, stid, name, roll, batch, marks):
# #                 self.name = name
# #                 self.stid = stid
# #                 self.roll = roll
# #                 self.batch = batch
# #                 self.marks = marks
# #                 if (self.marks >= 90):
# #                         grade = 'A and PASS'
# #                 elif (self.marks >= 80):
# #                         grade = 'B and PASS'
# #                 elif (self.marks >= 70):
# #                         grade = 'C and PASS'
# #                 elif (self.marks >= 60):
# #                         grade = 'D and PASS'
# #                 elif (self.marks >= 50):
# #                         grade = 'E and PASS'
# #                 elif (self.marks < 40):
# #                         grade = 'F and FAIL'
# #                 with open (f'{self.name}.txt','w') as q :
# #                         data = q.write (f'''
# # STUDENT ID :- {self.stid}
# # NAME :- {self.name}
# # CLASS ROLL NUMBER :- {self.roll} 
# # MARKS :- {self.marks}
# # BATCH NAME :- {self.batch}
# # GRADE = {grade} \n\n''')

# # supratim = student ('ECE2201','Supratim Nandi', '02', 'ECE22', 88)
# # arnab = student ('ECE2203','Arnab Pal', '03', 'ECE22', 89)
# # nemo = student ('ECE2204', 'Suranjan Nemo', '05','ECE22', 90)
# # x = [supratim.name, arnab.name, nemo.name]
# # y = [supratim.marks, arnab.marks, nemo.marks]
# # plt.hist(y, ec = 'red')
# # plt.xlabel('Grades')
# # plt.ylabel('Number of Students')
# # plt.title ('Students-Marks Graph')
# # plt.show()



# # # EXTRAS
# # say = print
# # say ("whoa! I can't belive that this even works")

# # def students ():
# #     print('students')
# # students()
# # print(students)
# # pupil = students
# # print(pupil)
# # pupil()

# # class employee:
# #     salary = 10000000000
# # ard = employee
# # print(ard.salary)
# # worker = employee
# # arunava = worker
# # print(arunava.salary)

# # def num (num):
# #     y= bin(num)
# #     x = str(y)
# #     for i in range (2,len(x)):
# #         print(x[i], end = "")
# # num(823)

# # print('\n')

# # def binnum (x):
# #     y= bin(x)
# #     z = str(y)
# #     for i in range (2, len(z)):
# #         print(z[i], end = "")
# # binnum(678)

# # def divide (x,y):
# #     return print(x/y)
# # divide (10,2)

# # # LAMBDA IS A FUNCTION FOR INSTANCE LIKE WE CREATE A FUNCTION AND WE ALSO NOT 
# # action = lambda x,y,z,a : ((x+a)/(y-z))
# # print(action(2,8,4,10))

# # # PLOTTING GRAPHS MOST TYPE IN PYTHON USING MATPLOTLIB.PYPLOT
# # import matplotlib.pyplot as plt
# # x = ['math', 'english', 'cse']
# # y = [93,94,95]
# # plt.hist(x,y)
# # plt.xlabel('Subjects')
# # plt.ylabel('Marks')
# # plt.title('Subjecs-Marks Graph')
# # plt.show(block = True)
# # A = int(input())
# # S = "LOL LOL"
# # if (A<3200 and A>= 2800):
# #     print("red")
# # elif (A>= 3200 and A <= 5000):
# #     print(S)
    

# # A = int(input())
# # S = 'lol'
# # if (A>= 2800 and A<3200 and A<=5000):
# #     print("red")
# # elif (A>= 2800 and A>= 3200 and A <= 5000):
# #     print(S)
# # def divmod(n,m):
# #         x = (n//m)
# #         k = (n%m)
# #         y = (x,k)
# #         return y
# # n = int(input())
# # m = int(input())
# # print(n//m)
# # print(n%m)
# # print(divmod(n,m))
# # x = int(input())
# # k = int(input())
# # y=x**3+x**2+x+1
# # if (y==k):
# #         print(True)
# # else:
# #         print(False)
# # class Box:
# #         def volume (l,b,h):
# #                 return print (f'The volume is {l*b*h}')
# # cuboid = Box
# # cuboid.volume(6,4,5)
# # l = [22,22]
# # for i in range (0,len(l)):
# #         print(sum(i))

# # marks = {

# #         'Arunava': [78,89,56],
# #         'Supratim':[78,90,67]
# # }

# # name = input()
# # y = (marks[name])
# # for i in y:
# #         z = sum(i)/3
# #         print(z)
# # # Your code here
# # P,Q,S,O,U = input().split()
# # print(P)
# # print(Q)
# # print(S)
# # print(O)
# # print(U) 

# # # # #
# # names = ['Arunava','Sohan','Zunaid','Nishan','Dibya']
# # surnames = ['Dutta','Karfa','Akhtar','Bag','Mukherjee']
# # jobs = ['Google SDE','Microsoft SDE','Doctor','Farmer','Footballer']

# # for name, sur, job in zip (names,surnames,jobs):
# #     print(f'NAME :- {name} || SURNAME :- {sur} || SO, {name} {sur} IS A {job}')

# # # # #
# # from getpass import getpass 
# # username = input("Username - ")
# # password = getpass ("Password - ")

# # if (username == 'ARD' and password == 'arunava2004'):
# #     print (f'Logging in to your account {username}')
# # else :
# #     print ("Details didn't match")

# # # # # Star pattern
# # n = int(input("Enter number of rows "))
# # for i in range (1,n+1):
# #         print((n-i)*" ",((2*i)-1)*"*")
# # for k in range (1,n):
# #         print((k)*" ",((2*(n-k)-1)*"*"))

# # # 
# # n = int(input("Enter number of rows here : "))
# # for i in range (1,n+1):
# #         print((n-i)*" ",i*"*")
        
# # # Good H pattern
# # n = int(input())
# # for i in range (1,(n+1)):
# #     print(" "*((n-i)),"H"*(2*i-1))
# # for k in range (0,(n+1)):
# #         print(" "*(n-3),"H"*n,end = "")
# #         print(" "*((3*n)-4),"H"*n)
# # for u in range (0,(n-2)):
# #         print(" "*(n-3),"H"*(n**2))
# # for k in range (0,(n+1)):
# #         print(" "*(n-3),"H"*n,end = "")
# #         print(" "*((3*n)-4),"H"*n)
# # for p in range (1,(n+1)):
# #         print(" "*((3*n)+2),end = "")
# #         print(" "*(p-1),"H"*((2*(n-p))+1))

# # # # Library management python simple codes
# # b = ['sherlock holmes','feluda','byomkesh']
# # u = input("Check the availability of the book you want - \n").lower()
# # for i in range (0,len(b)):
# #     if (u in b):
# #         print("Yes the book is in our library.")
# #         break    
# #     while (b[i] != u):
# #         u = input("Okay book not avaialable what more do you want\n").lower()
# # print("Okay ... Anything more or only this one ?")
# # u1 = input("Enter your preference - ")
# # if (u1 == 'more'):
# #     while (u1 != 'no more'):
# #         u1 = input("what more ? or no more ? ")
# #     while (b[i] != u):
# #         u2 = input("Okay book not avaialable what more do you want\n").lower()

# # # reverse a number
# # n = int(input("Enter number here \n"))
# # temp = n
# # x = len(str(n))
# # sum = 0
# # for i in range (0,x):
# #     rem = temp%10
# #     sum = sum*10 + rem
# #     temp = temp // 10
# # print(f'reversed number is {sum}')

# # # or
# # n = input("Enter number here ")
# # a = n[::-1]
# # a = int(a)
# # print(f"reverse is {a}")

# # # Pattern Christmas Tree
# # n = int(input("Rows :- "))
# # for i in range (1,n+1):
# #         print(" "*(n-i), "*"*(2*i-1))
# # for j in range (1,(n//2)+1):
# #         print(" "*((n//2)),"||"*((n//2)))



# # # # # Series
# # n = int(input("Enter number here - "))
# # sum = 0
# # for i in range (0,n+1):
# #     sum += (n**i)
# # print(sum)         

# # # # # Series
# # def fact(k):
# #     mul = 1
# #     for j in range (1,k+1):
# #         mul = mul * j
# #     return (mul)

# # n = int(input("Enter number here n - "))
# # x = int(input("Enter number here x - "))
# # sum = 0
# # for i in range (0,n+2):
# #     sum += (x**i)/fact(i+1) 
# # print(sum)

# # # # # sin(x) Maclaurin series value

# # def fact(n):
# #     facto = 1
# #     for i in range (1,(n+1)):
# #         facto = facto * i
# #     return (facto)

# # n = int(input("Enter n here - "))
# # x = int(input("Enter x here - "))
# # sum = 0
# # count = 2
# # print(f"Your Expansion Value Of sin({x}) Till {n} Is -\n")
# # for j in range (1,(n+1),2):
# #     if (j % 2 != 0 and count % 2 == 0):
# #         sum += (x**j)/fact(j)
# #         count += 1
# #     elif (j % 2 != 0 and count % 2 != 0):
# #         sum -= (x**j)/fact(j)
# #         count += 1
# # print(sum)    


# # #### reversing particular position of list
# # listrev = [0,1,2,3,4,5,6]
# # start = int(input("Enter Start Here ")) #2
# # last = int(input("Enter End Here "))#4   0 1 4 3 2 5 6
# # length = len(listrev)
# # if (start < length and last < length and start < last):
# #     for i in range (0,start):
# #         print(f'{listrev[i]}',end=" ")
# #     for j in range (start,(last+1)):
# #         print(f"{listrev[length-j-1]}",end=" ")
# #     for k in range (last+1,length):
# #         print(f"{listrev[k]}",end=" ")

# # # # Open file with user text

# # x = input("Enter Whatever You Want To Write - ")
# # with open('sample.txt','w') as w:
# #         data = w.write(x)

# # # Avg of user defined list
# # x = True  #just defining x
# # listr = [] #creating an empty list
# # while (x != 00): #giving condition that if user inputs 00 code will stop asking for numbers
# #     x = int(input("ENTER 00 TO STOP INPUT ,, ENTER THE NUMBERS : ")) # asking the number
# #     listr.append(x) #appending every elememt user inputs in empty list
# # listr.remove(listr[len(listr)-1]) #as the last elememt is 00 we dont count that so removing 00 from listr
# # print(listr)
# # y = len(listr)#length
# # r = sum(listr) #sum is a function to have the sum of all the elements in list
# # avg = r/y
# # print(avg)

# # # # if all digits are even then print number
# # def evencount(n):
# #     listr = [] # 2222
# #     u = str(n)
# #     for i in u:
# #         if (int(i) % 2 == 0):
# #             listr.append(int(i))
# #     if (len(listr) == len(u)):
# #         return 1
# #     else :
# #         return 0
# # s = int(input("Start "))
# # e = int(input("End "))
# # if (s < e):
# #     for i in range (s,e+1):
# #         if (evencount(i) == 1):
# #             print(i)

# # # last one .... break list from  middle
# # listr = []
# # m = 6
# # o = 0
# # for i in range (0,10):
# #     x = int(input("Element "))
# #     listr.append(x)
# # for j in range (0,2):
# #     for k in range (o,m-1):
# #         print(f"{listr[k]}",end = ' ')
# #     o += 5
# #     m += 5
# #     print()

# # x = input("Here ").strip()
# # print(x)

# # import numpy as np
# # x = np.array([1,2,3,4,5])
# # print(x)
# # y = np.array([1,2,3,4],[5,6,7,8])
# # print(y)


# # # # NUMPY

# # import numpy as np
# # import random

# # x = np.arange(12)
# # print(x)
# # y = x.reshape(4,3)
# # print(y)
# # y1 = x.reshape(3,4)
# # print(y1)
# # z = x.reshape(6,2)
# # print(z)
# # z1 = x.reshape(2,6)
# # print(z1)
# # z2 = x.reshape(12,1)
# # print(z2)
# # x = [[1,2,3],[3,4,5]]
# # # # 2d array
# # arr = np.array(x)
# # print(arr.sum(axis=0))
# # print(arr.sum(axis=1))
# # g = np.array([[1,2],[3,4]])
# # h = np.array([[5,6],[7,8]])
# # print(g+h)
# # print(g*h)
# # x = np.random.randint(1,10,(6,5))
# # y = np.random.randint(5,size = (5,3)) # two methods 5 means 0 to 5
# # print(x)  ## generates a 2d array of dimension 6x5 RxC with random values in b/w = 1 and =1 0
# # print(y)


# # # # PANDAS

# # # Replace All 0's With 1's In A Number
# def replaceOandZ (n):
#     if (n == 0):
#         n = 1 
#     return n    
# def CheckOandZ (n):
#     z = len(str(n))
#     c = []
#     for i in range (z):
#         rem = n % 10
#         s = replaceOandZ(rem)
#         c.append(str(s))
#         n //= 10
#     c.reverse()
#     return (int(''.join(tuple(c))))      
# x = int (input("Enter A Number here - "))
# print(CheckOandZ(x))

## Leetcode
# l1 = [2,4,3]
# l2 = [5,6,4]
# sum1 = 0
# sum2 = 0
# for i in range (0,len(l1)):
#     sum1 += ((10**(len(l1)-i-1)) * (l1[len(l1)-i-1]))
# for j in range (0,len(l2)):
#     sum2 += ((10**(len(l2)-j-1)) * (l2[len(l2)-j-1]))
# sum3 = sum1 + sum2
# b = len(str(sum3))
# retlist = []
# for k in range (0,b):
#     x = str(sum3)
#     retlist.append(int(x[b-k-1]))
# print(retlist)

## Leetcode
# class Solution(object):
#     def isPalindrome(self, x):
#         temp = x
#         sum1 = 0
#         if (x >= 0):
#             while (temp != 0):
#                 rem = temp % 10
#                 sum1 = (sum1*10)+rem
#                 temp //= 10
#             if (sum1 == x):
#                 print('true')
#             else:
#                 print('false')
#         else :
#             print("false")
            
# y = Solution()
# y.isPalindrome(122)