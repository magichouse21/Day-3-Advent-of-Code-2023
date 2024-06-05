#if they are adjacent add it to the list, find it by checking if a .isalpha() and ! '.' is
#either next to it on the same line, or it is diagonally adjacent (only one diagonal away)

def findNum(s1,s2,s3):
    k = 0
    total = 0
    if s1 == None: s1 = '..........................................................................'
    if s3 == None: s3 = '..........................................................................'
    print(s2)
    while k < len(s2):
        if s2[k].isnumeric():
            start = k
            while s2[k].isnumeric():
                k += 1
                if k == len(s2): break
            finish = k

            if start == 0: s = 1
            else: s = start
            if finish == len(s2): f = len(s2)-1
            else: f = finish

            if not s2[s-1].isalnum() and s2[s-1] != '.': total += int(s2[start:finish])
            elif not s2[f].isalnum() and s2[f] != '.': total += int(s2[start:finish])
            elif any(not c.isalnum() and c != '.' for c in s1[s-1:f+1]):    
                total += int(s2[start:finish])
            elif any(not c.isalnum() and c != '.' for c in s3[s-1:f+1]):    
                total += int(s2[start:finish])

            
        k+=1
    return total

        



def main():
    file = open('C:/Users/wizar/PycharmProjects/AdventofCode/Day 3/day3.txt', 'r')
    _list = file.readlines()
    list = []
    for parts in _list:
        list_ = parts.split('\n')
        list.append(list_[0])
    total = 0

    for k in range (0,len(list)):
        if k+1 == len(list): l3 = None
        else: l3 = list[k+1]
        total += findNum(list[k-1], list[k], l3)
    print(total)

main()

