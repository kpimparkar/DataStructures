import ctypes

class pyQueue(object):
    
    def __init__(self):
        self.length = 0
        self.noOfPosAvailable = 1
        self.qObject = self.formArray(self.noOfPosAvailable)
    
    def formArray(self, newLen):
        tArray = (newLen * ctypes.py_object)()
        for i in range(newLen):
            tArray[i] = None
        return tArray
    
    def __repr__(self):
        print(f"The queue has {self.length} objects as below: ")
        for i in self.qObject:
            if i:
                print(i)
    def resize(self, newLen):
        tArray = self.formArray(newLen)
        for i in range(len(self.qObject)):
            tArray[i] = self.qObject[i]
        self.noOfPosAvailable = newLen
        self.qObject = tArray
        
    def enQ(self, element):
        print(self.noOfPosAvailable, self.length)
        if self.noOfPosAvailable == self.length:
            self.resize(2*self.noOfPosAvailable)
            
        self.qObject[self.length]     
        self.qObject[self.length] = element
        self.length += 1
        print(self.noOfPosAvailable, self.length)
    
    def deQ(self):
        print(f"Removing element {self.qObject[0]} from begining of the queue following FIFO principle.")
        print(self.length)
        print(self.noOfPosAvailable)
        tArray = self.formArray(self.noOfPosAvailable)
        for i in range(1,len(self.qObject)):
            tArray[i-1] = self.qObject[i]
        self.qObject = tArray
        del tArray
        self.length -= 1
        self.__repr__()
    
    def isEmpty(self):
        return self.length == 0
    
    def peek(self):
        return self.qObject[0]
    
    def size(self):
        return self.length