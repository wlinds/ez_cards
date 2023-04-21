from PIL import Image, ImageDraw, ImageFont # For image generation
import os

# Stable diffusion
import torch
from diffusers import StableDiffusionPipeline

import requests

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

################################################

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

def stable_diffusion():
    PROMPT = "My repo"
    TOKEN = "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"

    DEVICE, DTYPE = ("cuda", torch.float16)\
        if torch.cuda.is_available()\
        else ("cpu", torch.bfloat16)

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        use_auth_token=TOKEN,
        torch_dtype=DTYPE
    ).to(DEVICE)

    with torch.autocast(device, dtype=dtype):
        image = pipe(PROMPT)["sample"][0]

    image.save("test.png")


model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)
pipe.enable_attention_slicing()

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")