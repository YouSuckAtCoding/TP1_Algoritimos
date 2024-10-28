
def bubbleSort(self):                           
    l = 0;
    r = self.__nItems - 1;

    while(l < r):
        for inner in range(l, r):
            if(self.__a[inner] > self.__a[inner + 1]):
                self.swap(inner, inner + 1);

        r-=1;

        for inner in range(r, l, -1):
            if(self.__a[inner] < self.__a[inner - 1]):
                self.swap(inner, inner - 1);

        l+=1;


class BubbleSorter:
    def __init__(self, arr):
        self.__a = arr        
        self.__nItems = len(arr)  

    def bubbleSort(self):
        l = 0
        r = self.__nItems - 1

        while l < r:
            for inner in range(l, r):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.__a[inner], self.__a[inner + 1] = self.__a[inner + 1], self.__a[inner]  

            r -= 1

            for inner in range(r, l, -1):
                if self.__a[inner] < self.__a[inner - 1]:
                    self.__a[inner], self.__a[inner - 1] = self.__a[inner - 1], self.__a[inner] 

            l += 1

    def get_sorted_array(self):
        return self.__a
    


sorter = BubbleSorter([5, 3, 8, 4, 2])
sorter.bubbleSort()
print(sorter.get_sorted_array())
sorter = BubbleSorter([10,8,95,4,7,1,6,3])
sorter.bubbleSort()
print(sorter.get_sorted_array())
sorter = BubbleSorter([8,4,9,7,1,5,33,4,11,2,6,7,8,9])
sorter.bubbleSort()
print(sorter.get_sorted_array())