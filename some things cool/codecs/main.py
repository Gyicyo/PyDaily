"""
    created at: 2024-03-28
    At: 15:14 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
import codecs

message: str = input("Enter Message: ")

encoded: str = codecs.encode(message, "rot13")
print("Encoded Message: ", encoded)
decoded: str = codecs.decode(encoded, "rot13")
print("Decoded Message: ", decoded)