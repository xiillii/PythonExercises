import numpy

if __name__ == "__main__":
    line = numpy.array(input().strip().split(' ')).astype(numpy.int32)
    (n, m, p) = line
    arr1 = numpy.array([[int(j) for j in input().strip().split(' ')] for i in range(n)])
    arr2 = numpy.array([[int(j) for j in input().strip().split(' ')] for i in range(m)])
 
    print(arr1)
    print(arr2)
    print(numpy.concatenate((arr1, arr2)))