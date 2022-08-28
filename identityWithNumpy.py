import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    numbers = tuple(map(int, input().split()))
    
    print(numpy.eye(numbers[0],numbers[1]))