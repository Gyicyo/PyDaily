"""
    created at: 2024-03-28
    At: 15:14 PM
    深度拷贝
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
import copy
sample_dict: dict = {'1':[1,2],'2':2,'3':3}
my_copy: dict = copy.deepcopy(sample_dict) # 完全拷贝

my_copy['1'][0]= 3
print(sample_dict)
print(my_copy)
