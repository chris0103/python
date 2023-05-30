from parse_util import *
from plot_util import *

words_freq_table = {}
trivial_words = ['的', '不', '和', '是', '用', '在', 'the', 'and', '（', '）', '(', ')', '/', '\\']
highlights = ['ChatGPT']

slides = get_slides("slides")
for slide in slides:
    if slide.name.endswith(".pdf"):
        print('Parsing slide ' + slide.name)
        contents = parse_pdf(slide)
        words = extract_words(contents, trivial_words + highlights)
        for word in words:
            if word in words_freq_table:
                words_freq_table[word] += 1
            else:
                words_freq_table[word] = 1

print(words_freq_table)
generate_cloud(words_freq_table)
