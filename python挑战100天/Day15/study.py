from PIL import Image,ImageFilter

image = Image.open('123.png')
image2 = Image.open('ball.png')
print(image.size)
print(image.format)
print(image.mode)
# image = image.crop((80, 20, 310, 360)) # 裁剪图片，四个参数是坐标
# image.thumbnail((128, 128)) # 缩放图片，两个参数是宽和高,但是缩放会保持原比例
image.paste(image2, (100, 100)) # 粘贴图片，元组是粘合位置
image.rotate(180).show() # 旋转180度
image.transpose(Image.FLIP_LEFT_RIGHT).show() # 左右翻转图片

# 操作像素
for x in range(0,200):
    for y in range(0,200):
        image.putpixel((x,y),(255,255,255))
image.show()

image.filter(ImageFilter.CONTOUR).show() # 轮廓滤镜