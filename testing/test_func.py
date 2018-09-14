import sys

def test_func(a, b):
    return a+b

def main():
    if len(sys.argv) != 3:
        raise TypeError('No it needs two arguments')
    a = sys.argv[1]
    b = sys.argv[2]
    #a = input("Input for a: ")
    #b = input("Input for b: ")
    print(test_func(a, b))

if __name__ == '__main__':
    main()
