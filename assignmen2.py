#create two lists of 5 elements each and perform operations like append 2 elements to both lists, deletion of 3 elements to both list and addition of both list to the third list

aList = [1,2,3,4,5]
bList = [6,7,8,9,10]
aList.append(11)
aList.append(12)
bList.append(13)
bList.append(14)
print(aList)
print(bList)
aList.remove(1)
aList.remove(2)
aList.remove(3)
bList.remove(6)
bList.remove(7)
bList.remove(8)
print(aList)
print(bList)
cList = aList + bList
print(cList)
