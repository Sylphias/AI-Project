from pytorch_vqa import sample
from PIL import Image


sampler = sample.Sample('pytorch_vqa/model.pth')


# CAT
filename = 'cat.jpg'
im = Image.open(filename)

question = "What animal is this?"
print(question, sampler.sample(im, question))