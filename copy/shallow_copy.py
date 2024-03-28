"""
    created at: 2024-03-28
    At: 15:14 PM
    浅拷贝
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
sample_dict: dict = {'1':[1,2],'2':2,'3':3}
my_copy: dict = sample_dict.copy() # 深层的内容不会被拷贝

my_copy['1'][0]= 3
print(sample_dict)
print(my_copy)
