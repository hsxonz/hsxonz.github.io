import subprocess
import random
import math
def convert(list):
    list1 =[]
    for i in list :
        if i.isnumeric():
            list1.append(int(i))
        else :
            list1.append(str(i))
    return list1

def readFile():
    f = open("inputz.inp", "r")
    list = convert(f.readline().split(" "))
    f.close()
    return list

def readAnswer():
    f = open("output.out","r")
    answer= f.read()
    f.close()
    return answer

def WriteFile():
    list =["Flood","Storm","Rain","Shower","Drizzle","Cloudy"]
    f = open("inputz.inp", "w")
    s = "{} {} {} {}".format(random.randint(1,999),random.randint(1,1000),random.randint(0,100),random.choice(list))
    f.write(s)
    f.close()
    return s

def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
def isFibonacci(n): 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 

def caculateP(list):
    return list

def th3(list):
    pass
def th4(list):
    pass

def main():
    list =readFile()
        
    if list[1]<200 :
        pass
    elif 200<=list[1] and list[1]<=800:
        pass
    else :
        pass


    

#round(number,2)
if __name__ == "__main__":
    pass
