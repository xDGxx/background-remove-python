from rembg import remove
from PIL import Image


img = Image.open('suaimagem.png')

imgRemove = remove(img)
imgRemove.save('./nomePasta/imageRemove.png')