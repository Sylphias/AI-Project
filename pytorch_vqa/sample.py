import sys
import os.path
import math
import json

import torch.nn as nn
import torch.utils.data
import torch
import torchvision.models as models

import config
import data
import utils
import model
from torch.autograd import Variable
import resnet as caffe_resnet
from PIL import Image

class Sample():
    def __init__(self, weights):
        with open(config.vocabulary_path, 'r') as fd:
            vocab = json.load(fd)

        self.answers = {v: k for k, v in vocab['answer'].items()}
        self.token_to_index = vocab['question']

        self.resnet = Net()
        self.net = nn.DataParallel(model.Net(len(vocab['question']) + 1))

        self.net.load_state_dict(weights)


    def encode_question(self, question):
        """ Turn a question into a vector of indices and a question length """
        vec = torch.zeros(len(question)).long()
        for i, token in enumerate(question):
            index = self.token_to_index.get(token, 0)
            vec[i] = index
        return vec, len(question)


    def sample(self, image, question):
        question = question.lower()[:-1]
        question = question.split(' ')
        q, q_len = self.encode_question(question)

        transform = utils.get_transform(config.image_size, config.central_fraction)
        inputImg = transform(image)

        q = Variable(q.unsqueeze(0))
        q_len = Variable(torch.tensor([q_len]))
        v = Variable(self.resnet(inputImg.unsqueeze(0)))

        out = self.net(v, q, q_len)

        _, answer = out.data.max(dim=1)

        return self.answers[int(answer)]


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = caffe_resnet.resnet152(pretrained=True)

    def forward(self, x):
        output = self.model(x)
        return output


def main():
    path = sys.argv[1]
    results = torch.load(path, map_location=lambda storage, loc: storage)

    sample = Sample(results['weights'])

    filename = 'cat.jpg'
    im = Image.open(filename)
    for i in range(10):
        print(sample.sample(im, "What color is its fur?"))


if __name__ == '__main__':
    main()
