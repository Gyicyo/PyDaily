def func(a,b,*,c,d):
    print(a,b,c,d)

try:
    func(1,2,3,4)
except TypeError as e:
    print(e)

func(1,2,c=3,d=4)