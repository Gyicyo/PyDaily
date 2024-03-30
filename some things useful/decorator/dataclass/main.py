from dataclasses import dataclass,InitVar,field

@dataclass(frozen=False) #若未True则不可修改类成员（一经初始化不能有任何改变）
class Fruit:
    name: str
    cost_per_kg: float
    grams: float

    is_rare: InitVar[bool] = False #这个变量仅用于初始化期间，而不作为类的实例属性
    total_price: float = field(init=False) # 默认不对total_price进行初始化
    #(有这么个变量但是不能在初始化时赋值（Fruit（total_price=1000）会报错）)
    similar_fruits: list[str] = field(default_factory=list) # 默认similar_fruits是个空列表


    def __post_init__(self,is_rare: bool) -> None: # 初始化完成后调用，is_rare是InitVar
        self.similar_fruits.append('apple')
        self.total_price = (self.cost_per_kg * self.grams / 1000)
        if is_rare:
            self.total_price *= 2.0
            self.cost_per_kg *= 2

banana: Fruit = Fruit('banana', 10, 500,is_rare=True)
