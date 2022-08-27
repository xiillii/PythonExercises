import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1]).astype(numpy.float64)
    
    
if __name__ == '__main__':
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)