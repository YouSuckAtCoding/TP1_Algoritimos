
def arrozNoTabuleiro(value):
    container = [];
    exp = 9999999;
    
    for i in range(exp):
        if(2 ** i >= value):    #'''Complexidade O(log n)'''
            return i;


print("value: " + str(arrozNoTabuleiro(33)));