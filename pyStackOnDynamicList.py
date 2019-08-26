import ctypes

class pyStack(object):
    def __init__(self):
        self.length = 0
        self.noOfEles = 1
        self.stackObject = (self.noOfEles*ctypes.py_object)()
        self.stackObject[0] = None
            
    def isEmpty(self):
        return self.length == 0
    
    def getLength(self):
        return self.length
    
    def resize(self, newlen):
        tempArray = (newlen * ctypes.py_object)()
        for i in range(len(tempArray)):
            tempArray[i] = None
        for j in range(len(self.stackObject)):
            tempArray[j] = self.stackObject[j]
        self.noOfEles = newlen
        self.stackObject = tempArray
    
    def appendEle(self, element):
        self.resize(2*self.noOfEles)
        self.stackObject[self.length] = element
        self.length += 1
    
    def __repr__(self):
        print("Stack object has {} elements. Content of the stack object = ".format(self.length))
        for i in range(len(self.stackObject)):
            if self.stackObject[i]:
                print(self.stackObject[i])
            
    def peek(self):
        return self.stackObject[self.length-1]
    
    def popLast(self):
        print("Removing element {} from index {}".format(self.stackObject[self.length-1], self.length-1))
        self.stackObject[self.length-1]=None
        self.length -= 1
        self.__repr__()