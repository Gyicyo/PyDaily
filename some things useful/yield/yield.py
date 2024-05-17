
def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter

def test_calc_avg():
    i = 0
    print('create generator')
    while i < 10:
        p = yield i
        print(f'i be yield : {i}')
        i += 1
        print(f'i be print : {i}')
        print(f'p be print : {p},in this time,i : {i}')

gen = test_calc_avg()
# print(type(gen))

print('0:')
print(gen.send(None))
print('1:')
print(gen.send(10))