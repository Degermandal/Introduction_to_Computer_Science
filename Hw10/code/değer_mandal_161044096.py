class SortedList:
    def__init__(self):
        self.thelist=[]
    def add(self,number):
        self.thelist.append(number)
    def remove(self,number):
        return self.thelist.pop(number)
    def printList(self):
        for number in self.thelist:
            print(number)
    def binarySearch(self,number):
        index=self.binarySearch(self.thelist,number)
        return index
    def binarySearch(self,MyList,number):
        if len(MyList)==1:
            return self.thelist[0]==number
        mid=math.ceil(len(MyList)/2)
        if MyList[mid]==number:
            return mid
        elif MyList[mid]<number:
            return binarySearch(MyList[:mid],number)
        elif MyList[mid]>number:
            return binarySearch(MyList[mid+1:],number)

sorted=SortedList()
sorted.add(7)
sorted.add(4)
sorted.add(9)
print sorted.remove()
print sorted.add()
print sorted.printList()
print sorted.binarySearch()
