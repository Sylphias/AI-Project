from pytorch_vqa import sample
from PIL import Image


sampler = sample.Sample('pytorch_vqa/results.pth')

filename = 'cat.jpg'
im = Image.open(filename)
for i in range(10):
    print(sampler.sample(im, "What animal is this?"))