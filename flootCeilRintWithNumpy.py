import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    line = numpy.array(input().strip().split(' ')).astype(float)
    
    print(numpy.floor(line))
    print(numpy.ceil(line))
    print(numpy.rint(line))