from pytorch_vqa import sample
from PIL import Image

threshold = 0.01 # threshold confidence for printing

sampler = sample.Sample('pytorch_vqa/model.pth')


# CAT
filename = 'cat.jpg'
im = Image.open(filename)

question = "What animal is this?"
answers = sampler.sample(im, question, topk = 5) # topk: number of results to get back

for i in range(len(answers)):
    conf = answers[i][1]
    if conf > threshold:
        print("{}: {:.2f}".format(answers[i][0], conf))