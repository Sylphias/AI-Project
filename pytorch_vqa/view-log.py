import sys
import torch
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt


def main():
    path = sys.argv[1]
    # results = torch.load(path)
    results = torch.load(path, map_location=lambda storage, loc: storage) # IF LOADING TO CPU

    epoch = results['epoch']
    print("LOADED RESULTS FROM EPOCH {}".format(epoch))

    val_acc = torch.FloatTensor(results['tracker']['val_acc'])
    val_acc = val_acc.mean(dim=1).numpy()

    train_acc = torch.FloatTensor(results['tracker']['train_acc'])
    train_acc = train_acc.mean(dim=1).numpy()

    val_loss = torch.FloatTensor(results['tracker']['val_loss'])
    val_loss = val_loss.mean(dim=1).numpy()

    train_loss = torch.FloatTensor(results['tracker']['train_loss'])
    train_loss = train_loss.mean(dim=1).numpy()

    plt.figure()
    plt.title('Training and Test Accuracies over Epochs')
    plt.plot(train_acc)
    plt.plot(val_acc)
    plt.legend(['Training Accuracy', 'Test Accuracy'], loc='lower right')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.grid(alpha = 0.3)
    plt.savefig('accs.png')

    plt.figure()
    plt.title('Training and Test Losses over Epochs')
    plt.plot(train_loss)
    plt.plot(val_loss)
    plt.legend(['Training Loss', 'Test Loss'], loc='lower right')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(alpha = 0.3)
    plt.savefig('losses.png')


if __name__ == '__main__':
    main()
