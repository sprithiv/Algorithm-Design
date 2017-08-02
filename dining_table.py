def arrange_seating(a,b):
    
    x = max(a)
    y = len(b)
    if x > y:
        print "There is no valid arrangement"
        return
    
    #Sort the table size in descending order to reserve the table.
    table = sorted(b,reverse=True)
    index = []
    for val in sorted(set(table),reverse=True):
        ind = [i for i, x in enumerate(b) if x == val]
        index.append(ind)
    index = sum(index, [])

    #Temp variable to manipulate seating arrangement.
    temp = []
    for values in table:
        temp.append(values)

    #Allocate seat
    finallist = []
    j = 0
    for val in a:
        finallist.append([])
        i = 0
        while val != 0:
            if i >= y:
                print "There is no valid arrangement"
                return
            if temp[i] > 0:
                temp[i] = temp[i] - 1
                finallist[j].append(1)
                val = val - 1
            else:
                finallist[j].append(0)
            i += 1
        while len(finallist[j]) < y:
            finallist[j].append(0)
        j += 1
    
    
    #Reconstruct origin list
    ori = []
    for i in index:
        ori.append(0)
    j = 0
    for i in index:
        ori[i] = table[j]
        j += 1

    #Construct the seating arrangement
    arrangement = []
    for j in range(0,len(a)):
        arrangement.append([])
        for i in index:
            arrangement[j].append(0)
           
    for j in range(0,len(a)):
        k = 0
        for i in index:
            arrangement[j][i] = finallist[j][k]
            k += 1

    print "Family Members:"
    print a
    print "Table capacity array:"
    print ori
    print "Sitting arrangement:"
    for val in arrangement:
        print val

def main():

    #Testcase 1
    a = [3,2,2]
    b = [1,1,3,2]

    #Testcase 2
    #a = [4,3,1,9,8]
    #b = [5,6,7,1,2,9]

    #Testcase 3
    #a = [3,3,2]
    #b = [4,2,1,3]

    #Testcase 4
    #a = [8,8,5,5,3,2,7]
    #b = [5,7,2,8,1,6,2,5,3]

    arrange_seating(a,b)
        

if __name__ == "__main__":
    main()