from abc import abstractmethod

class Pet(object):

    @abstractmethod
    def make_voice(self):
        print('Pet is abstract')

class Dog(Pet):

    def make_voice(self):
        return super().make_voice()


c = Dog()
c.make_voice()
