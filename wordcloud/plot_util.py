from os import path
import numpy as np

from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_cloud(freq_table):
    q_mask = np.array(Image.open(path.join("Q_big.png")))
    wc = WordCloud(
        width=4000,
        height=2000,
        scale=2,
        font_path='Hannotate.ttc',
        background_color="white",
        mask=q_mask
    ).fit_words(freq_table)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    print("Generating word cloud!")
