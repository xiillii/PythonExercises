import numpy

if __name__ == "__main__":
    line = numpy.array(input().strip().split(' ')).astype(numpy.int32)
    (n, m) = line
    
    arr1 = numpy.array( [[j for j in input().strip().split(' ')] for i in range(int(n))], int)
    arr2 = numpy.array( [[j for j in input().strip().split(' ')] for i in range(int(m))], int)
    
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1 * arr2)
    print(arr1 // arr2)
    print(arr1 % arr2)
    print(arr1 ** arr2)