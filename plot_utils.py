from PIL import Image
import matplotlib.pyplot as plt


def plot_images(n_row, n_col, imgs, figsize=(24, 16), show_names=False):
    _, axs = plt.subplots(n_row, n_col, figsize=figsize)
    axs = axs.flatten()
    for i, (file_img, ax) in enumerate(zip(imgs, axs)):
        fName = file_img.split("/")[-1]
        # name = name.split("_")[1]

        img = Image.open(file_img)
        ax.imshow(img)
        if (show_names):
            name = fName
            ax.text(0.95, 0.95, name, color='red', fontsize=7,
                    transform=ax.transAxes, ha='right', va='top')
        # if i< n_col:
        #   ax.text(0.95, 0.95, name, color='red', fontsize=7,
        #                 transform=ax.transAxes, ha='right', va='top')
        ax.margins(x=0)
        ax.margins(y=0)
        ax.axis('off')
    plt.tight_layout(pad=0.05)
    plt.show()


def plot_scores(scores, z, title=""):
    for s, l in zip(scores, z):
        plt.plot(s, label=l)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.ylim(0.90, 1)
    plt.title(title)
    plt.xticks([i for i, x in enumerate(scores[0]) if i % 10 == 0])
    plt.legend()
    plt.show()
