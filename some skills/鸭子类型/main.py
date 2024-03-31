"""
    Create At 2024/3/30
    At:20:16 PM
"""
class duck:
    def quack(self):
        print("Quack, quack!")

class person:
    def quack(self):
        print("I'm a person, not a duck!")

def make_sound(duck: object):
    if hasattr(duck, 'quack'): # 检查duck中是否存在quack对象
        if callable(duck.quack): # 检查quack是否为可调用对象
            duck.quack()
        else:
            print("This object doesn't quack!")
    else:
        print("This object doesn't quack!")

duck = duck()
person = person()
make_sound(duck)
make_sound(person)
