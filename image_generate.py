# %%
from PIL import Image, ImageDraw, ImageFont

# 创建一个 256x256 像素的图标（较大分辨率，兼容性更好）
size = 256
background_color = (150, 150, 150)  # 深灰色背景
text_color = (255, 255, 255)     # 白色文字

# 创建图片
img = Image.new("RGB", (size, size), background_color)
draw = ImageDraw.Draw(img)

# 尝试加载字体（使用系统默认字体）
try:
    font = ImageFont.truetype("Arial.ttf", 140)  # 大号字体
except IOError:
    font = ImageFont.load_default()

# 文字
text = "TN"
text_width, text_height = draw.textsize(text, font=font)
text_x = (size - text_width) / 2
text_y = (size - text_height) / 2

# 绘制文字
draw.text((text_x, text_y), text, font=font, fill=text_color)

# 保存为 PNG 文件
output_path = "/Users/juntao/Desktop/PersonalPage/images/favicon.png"
img.save(output_path, "PNG")
output_path