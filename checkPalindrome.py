"""
Given a string, the task is to check if the string can be made palindrome by swapping a character only once.
[NOTE: only one swap and only one character should be swapped with another character]

Input : bbg
Output : true

Input : bdababd
Output : true

Input : gcagac
Output : false
"""

def displayMatrix(mat,n):
    for i in range(0,n):
        for j in range(0,n):
            print(mat[i][j],end="\t")
        print("\n")

def checkPalindrome(str):
    n = len(str)
    diffCount = 0
    d = int(n/2)

    diff = [[0 for x in range(d)] for y in range(d)]
    
    for i in range(0,d):
        if (str[i] != str[n-i-1]):
            if (diffCount == 2):
                #print("Different Characters Count=",diffCount)
                #displayMatrix(diff,d)
                return False
            diff[diffCount][0] = str[i]
            diff[diffCount][1] = str[n-i-1]
            diffCount+=1

    #print("Different Characters Count=",diffCount)
    #displayMatrix(diff,d)

    if (diffCount == 0):
        return True
    elif (diffCount == 1):
        midChar = str[i]
        if (n%2 !=0 and (diff[0][0] == midChar or diff[0][1] == midChar)):
            return True
    elif (diffCount == 2):
        if ((diff[0][0] == diff[1][0] and diff[0][1] == diff[1][1]) or (diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0])):
            return True
    else:
        return False

str = input("Enter String: ")

if (checkPalindrome(str)):
    print ("Yes")
else:
    print ("No")
