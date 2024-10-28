
def greatestNumber(array):

    max = 0;
    for i in array:
        if(i > max):
            max = i;
    
    return max;

print(greatestNumber([1,2,3,4,5]));