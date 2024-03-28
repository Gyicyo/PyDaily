"""
    created at: 2024-03-28
    At: 15:14 PM
"""
#pylint: disable=C0115,C0103,E0401,C0116,C0304
from captcha.image import ImageCaptcha


text: str = "023162"
captcha: ImageCaptcha = ImageCaptcha(width=400,
                                    height=220,
                                    font_sizes=(20,30,40))

img = captcha.generate_image(text)
img.show()
