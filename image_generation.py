from PIL import Image, ImageDraw, ImageFont # For image generation
import os

# Create new dir for images
if not os.path.exists('Images'):
    os.makedirs('Images')


# Generate png files for cards images
def gen_card(n):
    img = Image.new('RGB', (1280, 640), color = 'white')
    draw = ImageDraw.Draw(img)
    font = font = ImageFont.truetype('Arial.ttf', 60)
    text = f'repo number {n}'
    text_size = draw.textsize(text, font)
    x = (1280 - text_size[0]) / 2
    y = (640 - text_size[1]) / 2
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    img.save(f'Images/repo_{n}.png')