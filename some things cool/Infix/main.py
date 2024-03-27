"""
    created at: 2024-03-27
"""

from typing import Callable,Any,Self
class Infix:
    """
    Infix class
    """
    def __init__(self, function:Callable): #初始化方法
        self.function = function

    def __ror__(self, other: Any) -> Self: #infix在 | 的右侧
        return Infix(lambda var: self.function(other,var))

    def __or__(self, other: Any) -> Any: #infix在 | 的左侧
        return self.function(other)

    def __repr__(self): #调试输出
        return f"<Infix {self.function}>"

infix: Infix = Infix(lambda x,y: x * y) #infix实例，该实例用于计算两边数的乘积
print(f'{1 | infix | 2}')#从左到右顺次执行，因此上边应该会先执行ror再执行or
