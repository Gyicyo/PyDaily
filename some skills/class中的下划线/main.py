"""
    Create At 2024/3/30
    At:18:40 PM
"""
class Main:

    __b = 2 # 私有变量
    _c = 3 # 声明私有，外部仍然可用，但不推荐
    def __init__(self) -> None:
        self.id = 1

    def __get_id(self): # 私有方法，仅class内部访问（但也有方法直接访问）
        return self.id

    def _get_id(self):  # 声明私有，外部仍然可用，但不推荐
        return self.__get_id()


m = Main()
print(m._get_id())# 调用_get_id()方法间接调用__get_id()方法
print(m._Main__get_id()) # 直接调用__get_id()方法
print(m._Main__b) # 直接访问私有变量__b
print(m.__get_id())# Main object has no attribute '__get_id'

