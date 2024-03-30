"""
    Create At 2024/3/30
    At:20:16 PM
"""
import secrets
from cryptography.hazmat.primitives.hashes import Hash,SHA256

print(secrets.randbelow(100)) # 生成随机整数(0-100)
print(secrets.token_urlsafe(16)) # 生成随机URL安全的字符串
print(secrets.token_hex(16)) # 生成随机16进制字符串
print(secrets.choice(['apple', 'banana', 'orange'])) #更安全的choice

#模拟加盐哈希

password = "hello world"
hex_model = Hash(SHA256()) #获取哈希256对象
salt = secrets.token_hex(16) #生成随机盐值

hex_model.update(bytes(salt.join(password), encoding='utf-8')) #加盐哈希加密
hex_password = hex_model.finalize().hex() # 获取密码的哈希值
print(hex_password)
