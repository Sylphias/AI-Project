import sys
import torch
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt


def main():
    path = sys.argv[1]
    results = torch.load(path)
    # results = torch.load(path, map_location=lambda storage, loc: storage) # IF LOADING TO CPU

    val_acc = torch.FloatTensor(results['tracker']['val_acc'])
    val_acc = val_acc.mean(dim=1).numpy()

    plt.figure()
    plt.plot(val_acc)
    plt.savefig('val_acc.png')


if __name__ == '__main__':
    main()
