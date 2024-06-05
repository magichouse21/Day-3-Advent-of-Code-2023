#if they are adjacent add it to the list, find it by checking if a .isalpha() and ! '.' is
#either next to it on the same line, or it is diagonally adjacent (only one diagonal away)

def middle(s2, gear):
    nums = []
    k = gear
    
    if k == len(s2)-1 or s2[gear-1].isnumeric(): 
        if s2[k-1].isnumeric(): # checks for numbers to the left of the gear
            k-=1
            nlr = k #number left right (left side of the gear last number)
            while s2[k-1].isnumeric():
                k -= 1
                if k == 0: break
            nll = k #number left left (left side of the gear)
            numl = int(s2[nll:nlr+1])
            nums.append(numl)
    if gear != len(s2)-1:
        if s2[gear+1].isnumeric(): #checks for numbers to the right of the gear
            k = gear
            k+=1
            nrl = k #number right left (right side of the gear first number)
            while s2[k].isnumeric():
                k += 1
                if k == len(s2): break
            nrr = k #number right right (right side of the gear)
            numr = int(s2[nrl:nrr])
            nums.append(numr)

    return nums



def findNum(string, gear):
    nums = []
    start = 0
    finish = 0
    if not string[gear].isnumeric():
       # print('mmmmmmmmmmmmmmmmmmmiiiiiiiiiiiiiiiiiiiiiiiiiidddddddddddddddddddddlllllllllllllllllleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        nums = middle(string, gear)
        
    if string[gear].isnumeric():
        start=gear
        finish=gear+1

        if (gear != 0) and string[gear-1].isnumeric():
            while string[start-1].isnumeric():
                start -= 1
        if (gear!=len(string)-1) and string[gear+1].isnumeric():
                while string[finish].isnumeric():
                    finish += 1
                    if finish == len(string):break
        num = int(string[start:finish])
        nums.append(num)

    return nums 

def mathing(s1,s2,s3):
    k = 0
    total = 0
    _total = 0
    if s1 == None: s1 = '............................................................................................................................................'
    if s3 == None: s3 = '............................................................................................................................................'

    while k < len(s2):
        if s2[k] == '*':
            gear = k
            if gear-3 <= 0: s = 0
            else: s = gear-3
            if gear+4 >= len(s2): f = len(s2)+1
            else: f = gear+4

           # print(s2[s:f],s1[s:f],s3[s:f])

            wheregear = s2[s:f].find('*')
            if wheregear != 3:
                print(list,top,under)
            list = middle(s2[s:f], 3)
            top = findNum(s1[s:f], 3)
            under = findNum(s3[s:f], 3)
            print(wheregear)
            
            #print(list,top,under)

            if len(list)+len(top)+len(under) == 2:
                _total = 1
                for numbers in list:
                    _total *= numbers
                for numbers in top:
                    _total *= numbers
                for numbers in under:
                    _total *= numbers
            #else:print('NOTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
            if _total == 1: _total = 0
            
            total += _total

        k+=1
    return total

def main():
    file = open('C:/Users/wizar/PycharmProjects/AdventofCode/Day 3/day3.txt', 'r')
    _list = file.readlines()
    list = []
    
    for parts in range (0,len(_list)):
        list.append(_list[parts][0:142])
    total = 0

    for k in range (0,len(list)):   
        if k+1 == len(list): l3 = None
        else: l3 = list[k+1]
        if k-1 == -1: l1 = None
        else: l1 = list[k-1]
        total += mathing(l1, list[k], l3)
    print(total)
main()

