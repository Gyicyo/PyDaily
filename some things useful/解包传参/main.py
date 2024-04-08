def main(a,b,c):
    print("a:",a)
    print("b:",b)    
    print("c:",c)


if __name__ == '__main__':
    args = [1,2,3]
    main(*args)