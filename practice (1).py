import math
import random
#Q2 LAB2
"""
def F(s1, s2):
    r = []
    for e1 in s1:
        for e2 in s2:
            if e1 == e2:
               r += [e1]
               break
    return r
"""

def F(s1,s2):
    r =[]
    i =0
    while i < len(s1):
        j =0
        while j < len(s2):
            if s1[i] == s2[j]:
                r.append(s1[i])
            j+=1
        i+=1
    return r

#Q4 LAB2
def iter_factorial(n):
    for val in range(1,n):
        n =val *n
    return n
print(F([1,3,5],[1,3,7]))
print(iter_factorial(3))
"""
def reducedFeeEntitlement(d):
    my_list =[]
    for key,val in d.items():
        if len(val) < 2:
           my_list.append(val)
    return my_list
"""
def commonModules(d,s1,s2):
    my_list =[]
    second_list =[]
    third_list =[]
    for key,val in d.items():
        if s1 == key:
            my_list.append(val)
            if s2 == key:
                second_list.append(val)
    for i in my_list:
        print(my_list)
        if i in second_list:
            print(second_list)
            third_list.append(i)
    return third_list
print(commonModules({'1':['1','2','3'],'2':['2','3','4'],'3':['5','2']},'1','2'))
def hailstone(n):
    print(n)
    while n!= 1:

        if n%2==0:
            n =n/2
            print(n)
            continue
        if n%2!=0:
            n =(3*n) +1
            print(n)
        if n == 1:
            break
    return
#print(hailstone(10))
 # Write a Python  function called isHexDigit, which takes a string as an argument
#and returns  True  if  its  argument  is  a  single-character  string  with  a  value  that
#is  used  in hexadecimal numerals (i.e. in the range ’0’ to ’9’ or ’a’ to ’f’) but returns
#False otherwise.
def isHexDigit(egg):
    x = '0123456789abcdef'

    for val in egg:
        if val in x:
            return True
        else:
            return False

#print(isHexDigit('123'))
#print(isHexDigit('xxx'))
#print(isHexDigit('xx12e'))
 # Write a Python function called maxProd, which takes as an argument a list of sets
#of numbers, calculates the product of the values in each of the sets, and returns the
#largest such product.  (Note that the sets may contain negative numbers so the largest
#product could be negative.)  If any of the sets is empty, its product should be treated
#as 1; if the list is empty, the value None should be returned.
def maxProd(my_list):
    egg =1
    for val in range(0,len(my_list)):
        if len(my_list) == 0:
            return None
        egg *= my_list[val]
    return egg
#print(maxProd([(1,2),(2,3)]))
def rotate(s,n):

    s += s[0:n]
    return False, s[n:len(s)]
#print(rotate("abcde", 1))
#print(rotate("abcde", 2))
#lab4 q4
def append_list():
    list_1 =[1,2,3]
    list_2 =[10,20,30]
    totals =list(map(lambda x:x[0]+x[1],zip(list_1,list_2)))
    return totals
#print(append_list())
"""
def chooseLargest():
    l1 =[1,2,3,4,5]
    l2 =[2,2,9,0,9]

    result =[list(map(lambda x,y:max[x],max[zip(l1,l2)))]
    return result
#print(chooseLargest())
"""
def randomList4096():
    global out
    out = [0]
    for i in range(1, 4095):
        out.insert(random.randint(0,i), i)
    return out
#print(randomList4096())
def unique_num():
    num_list = out
    return max(num_list)
#print(unique_num())
def substrings(s):
    my_list =[]
    my_list.append("")
    for val in range(0,len(s)):

        my_list.append(s[val])


    return my_list
#print(substrings("the"))
def HailstoneR(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        return [n] + HailstoneR(n//2)
    else:
        return [n] + HailstoneR(3 * n + 1)
#print(HailstoneR(20))
def recursive_N(n):
    if n ==0:
        return (False,0)
    else:
        if n>0:
            return(False,n + recursive_N(n-1)[1])
        else:
            return(False,n+ recursive_N(n+1)[1])
print(recursive_N(1))
print(recursive_N(2))
print(recursive_N(-5))
def containsAll(str,chars):

    s1 = set(str)
    s2 =set(chars)
    return s1 == s2
#print(containsAll("man","nma"))
def createDeck():
    cards=[]
    values =["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits =["s","h","d","c"]
    for i in values:
        for j in suits:
            res =i+j
            cards.append(res)

    return cards
#print(createDeck())

def shuffle(deck):
    random.shuffle(deck)
    return deck
#print(shuffle(['2s','5h','7d']))
def binarysearch(man,man2):
    my_list =[]
    for i in range(0,len(man)):
        print(man[i])
        i = i//2

    #my_list.append(tea)
    return my_list


#print(binarysearch([3, 5, 6, 8, 11, 12, 14, 15, 17, 18],8))
def redact():
    good_list =[]
    bad_list=[]
    bad = open("unredacted.txt", "r")
    info = bad.readlines()
    good = open("sensitiveWords.txt", "r")
    medium =open("redacted.txt", "r")
    info3 =medium.readlines()
    info2 = good.readlines()
    for i,val in enumerate(info2):
        info2[i] =val.strip('\n')
    #print(info2)

    for i,sentence in enumerate(info):
        for word in info2:
            if word in sentence:
                sentence =sentence.replace(word,"*" * len(word))
                print(sentence)
        info[i] =sentence
   # print(info)
    for sentence in info:
        medium.write(sentence)
#print(redact())
def F_lambda(S1,S2):
    return list(map(lambda x:x,[e1 for e1 in S1 if e1 in S2]))
#print(F_lambda([1,2,3],[1,2]))

def check_lsms(lsms):
    rows_list =[]
    row1_list =[]
    row2_list=[]
    row3_list=[]
    column1_list =[]
    column2_list =[]
    column3_list =[]
    first_dig =[]
    second_dig =[]
    barry =lsms[0][0]
    bell =lsms[1][1]
    bang =lsms[2][2]
    belle =lsms[2][0]
    briget =lsms[0][2]
    first_dig.append(barry)
    first_dig.append(bell)
    first_dig.append(bang)
    second_dig.append(belle)
    second_dig.append(bell)
    second_dig.append(briget)



    for x in zip(*lsms):
        rows_list.append(sum(x))
    for val in range(0,len(lsms)):
        column1_list.append(lsms[val][0])
        column2_list.append((lsms[val][1]))
        column3_list.append((lsms[val][2]))

    l =rows_list[0]
    #man =sum(rows_list)
    man2 =sum(column1_list)
    man3 =sum(column2_list)
    man4 =sum(column3_list)
    man5 =sum(first_dig)
    man6 =sum(second_dig)
    if l== man2:
        return True
    else:
        return False

#print(check_lsms([[4,9,2],
#                  [3,5,7],
 #                 [8,1,6]]))
def clues(hunt):
    print(11)
    i =0
    j =0
    start =str(hunt[i][j])

    while i >=0:
        x =str(hunt[i][j])
        print(x)
        first = int(x[0]) - 1
        second = int(x[1]) - 1
        i =first
        j =second
        if x == '52':
            break
    return hunt
#print(clues([[34, 21, 32, 41, 25],
  #           [14, 42, 43, 14, 31],
 #            [54, 45, 52, 42, 23],
 #            [33, 15, 51, 31, 35],
  #           [21, 52, 33, 13]]))
def answer_key(answers):
    file1 = open("students.txt", "r")
    student_list =[]
    big_list =[]
    q1_list =[]
    info = file1.readlines()
    for line in info:
        line =line.strip('\n').split(',')
        #print(line[0])
        index = range(1, len(line))
        student_list.append(line[0])
        q1_list.append(line[1])
    q1 =len(student_list)
    return q1_list,answers
#print(answer_key(['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','C','D']))
def peaks(numlist):
    new_list=[]
    new_list.append(numlist[0])
    for val in range(0,len(numlist)-1):
        if numlist[val] > new_list[-1]:
            new_list.append(numlist[val])

    return new_list
#print(peaks([3,2,5,5,7,6,1,8,4]))
#print(peaks([9,8,7,6,5,4,3,2,1]))

def reducedFeeEntitlement(d):
    my_list=[]
    for key ,val in d.items():
        if len(val) <2:
           my_list.append(key)

    return my_list
#print(reducedFeeEntitlement({'10':['a','b','c'],'11':['d'],'12':['e']}))
def commonModules(d, s1, s2):
    my_list =[]
    second_list =[]
    third_list =[]
    for key,val in d.items():
        if key == s1:
            my_list.append(val)
        if key == s2:
            second_list.append(val)
            if val == val:
                third_list.append(val)
    return my_list,second_list,third_list
#print(commonModules({'10':['a','b','d'],'11':['d'],'12':['d']},'10','11'))
def inverse(d):
    inv_map = dict(zip(d.values(), d.keys()))
    return inv_map
#print(inverse({'glas':'green','gorm':'blue'}))
def print_dictionary(d):

    return sorted(d)
#print(print_dictionary({'rothair':'bike','glas':'green','gorm':'blue'}))
def client_matcher():
    filein =open("clients.txt","r")
    my_list =[]
    clients ={}
    for line in filein:
        client =line.strip("\n").split(",")
        clients[client[0]] =client[1:]
        #print(client[1])
        #s = client[0], "should meet", client[0]
        #print(clients.values())

    for a in clients.keys():
        for b in clients.keys():
            if a != b:
                if clients[a][2] == clients[b][0]:
                    s = a ,"should meet",b
                    my_list.append(s)


    return my_list
#print(client_matcher())
def extract(text,n,m):
    word =n-1
    words =text.split()
    man =words[m-1::m]
    my_list =[]
    #print(words[4][0])
    #my_list.append(words[m-1][n-1])
    for i in man:
        my_list.append(i[word])
        if len(i) >n:
            return "Oops,there is no character",word,"in the word",i
    return my_list
#print(extract("Yesterday I saw an aardvark while walking my pet tortoise, Frank. What"
             # " a sight this was! Aardvarks are nocturnal animals appearing in daylight "
              #"with caution. Make sure to bring kippers when you visit",1,5))
#print(extract("Yesterday I saw an aardvark while walking my pet tortoise, Frank. What"
             # " a sight this was! Aardvarks are nocturnal animals appearing in daylight "
             # "with caution. Make sure to bring kippers when you visit",6,5))
def F(s1, s2):
        r = []
        i =0
        while i < len(s1):
            j =0
            while j < len(s2):
                if s1[i] == s2[j]:
                     r.append(s1[i])
                j+=1
            i+=1
        return r
#print(F([1,2,3],[1,3,5]))
"""def print_names2(people):
    for person in people:
        #print(person)
        to_print = ""
        for name in person:
            to_print += name
        print(to_print)
    return
print(print_names2('James'))"""
def print_names2(people):
    i = 0
    while i < len(people):
        j = 0
        while j < len(people[i]):
            print(people[i][j])
            j += 1
        i += 1
#print(print_names2('James'))
def tenkSteps(stepData):
    my_list = []
    for x in zip(*stepData):
        my_list.append(sum(x))
        count = 0
        for val in my_list:
            if val > 100000:
                count = count + 1
    return count
"""
#Jasons solution
def mostSteps(stepData):
    total =0
    employ_numb =0
    while employ_numb < len(stepData):
          employ_total =0
          for val in stepData[employ_number]:
                 employ_total +=val
          if total < employ_total:
               most_walked =employ_numb
    return employ_numb
"""
def del_1000(courierData):
    my_list = []
    for x in zip(*courierData):
        my_list.append(sum(x))
        count = 0
        for val in my_list:
            if val > 1000:
                count = count + 1
    return count
print(del_1000([[1000,0,0,0,0],[1000,3000,0,0,0]]))
def most_del(courierData):
    total =0
    employ_numb =0
    while employ_numb < len(courierData):
          employ_total =0
          for val in courierData[employ_numb]:
                employ_total +=val
          if total < employ_total:
               most_walked =employ_numb
               total =employ_total
          employ_numb +=1
    return most_walked
#print(most_del([[1000,0,0,0,0],[9000,0,0,0,0]]))
def chooseLargest():
    a =[1,2,3,4,5]
    b =[2,2,9,0,9]
    return list(map(lambda i:max(i[0],i[1]),zip(a,b)))
print(chooseLargest())
def F():
    s1 =[1,2,3]
    s2 =[1,3,5]
    return list(map(lambda x:x,[x for x in s1 if x in s2]))
#print(F())
def loop_the_loop_while(a1, a2):
   """ new_loop = []

    for e1 in a1:
        for e2 in a2:
            new_loop.append(e1 + e2)
    return new_loop"""
   new_loop =[]
   i =0
   while i < len(a1):
       j =0
       while j < len(a2):
           if a1[i] == a2[j]:
               new_loop.append(a1[i]+a2[j])
           j+=1
       i+=1
   return new_loop
#print(loop_the_loop_while([1,2,3],[1,3,5]))
def read_file(input_file):
    try:
        #Open the file in the parameter
        filein = open(input_file, "r")

        my_list = []
        clients = {}
        #For the info in the file
        for line in filein:
            client = line.strip("\n").split(",")
            #Get the key and get rid of brackets
            s =client[0]
            egg = s.replace("(", "")
            new_egg =int(egg)
            my_list.append(client[1])
            #get the last value and replace the ending brackets
            m =client[2]
            egg2 = m.replace(")", "")
            egg2=client[2]
            my_list.append(egg2)
            #Get the key and values and create the dictionary
            clients[new_egg] = client[1:]

        return clients
    except:
        return "Oops there has been an error"
print(read_file("details.txt"))
def write_dict(d):
    try:
        #Open the file output.txt
        filein =open('output.txt','r')
        #Read all the information in the file
        man =filein.readlines()
        #For the items in the dictionary
        for val in d:
            #Write the info to the file
            filein.write(str(val))


        return man
    except:
        return "Oops there has been an error"
print(write_dict({2:['12','13'],3:['14','15']}))


