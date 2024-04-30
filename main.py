from PIL import Image, ImageDraw, ImageFont

image_path = input("底圖檔案名稱: ")
text = input("震央位置: ")
max = input("最大震度(0~9): ")
loc = input("本地震度(0~9): ")

image = Image.open(image_path).point(lambda p: p * 0.5)

overlay_max = Image.open('./resource/{}.png'.format(max)).resize((150, 150))
overlay_loc = Image.open('./resource/{}.png'.format(loc)).resize((150, 150))

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("font.ttf", 150)

(width, height), (ox, oy) = font.font.getsize(text)

image_width, image_height = image.size
x = (image_width - width) / 2
y = image_height - height - 100


def d_text(text, x, y):
    text_color = (255, 255, 255)
    outline_color = (0, 0, 0)

    outline_positions = [
        (x - 5, y - 5), (x + 5, y - 5),
        (x - 5, y + 5), (x + 5, y + 5),
        (x - 5, y), (x + 5, y),
        (x, y - 5), (x, y + 5),
    ]

    for outline_position in outline_positions:
        draw.text(outline_position, text, fill=outline_color, font=font)
    draw.text((x, y), text, fill=text_color, font=font)


d_text(text, x, y)
d_text("最大震度", 550, 300)
d_text("本地震度", 550, 550)

image.paste(overlay_max, (1200, 305), overlay_max)
image.paste(overlay_loc, (1200, 555), overlay_loc)

border_width = 35

color_list = [
    "6B7878",
    "6B7878",
    "1E6EE6",
    "32B464",
    "FFE05D",
    "FFAA13",
    "EF700F",
    "E60000",
    "A00000",
    "5D0090"
]

new_width = image.width + 2 * border_width
new_height = image.height + 2 * border_width

rgb_color = tuple(int(color_list[int(max)][i:i+2], 16) for i in (0, 2, 4))

bordered_image = Image.new('RGB', (new_width, new_height), rgb_color)
bordered_image.paste(image, (border_width, border_width))

bordered_image.save('output.jpg')
bordered_image.show()
