import numpy


if __name__ == '__main__':
    line = input().strip().split(' ')
    (n, m) = line
    arr2d = [[j for j in input().strip().split(' ')] for i in range(int(n))]
    my_array = numpy.array(arr2d).astype(numpy.int32)
    print( numpy.transpose(my_array))
    print(my_array.flatten())