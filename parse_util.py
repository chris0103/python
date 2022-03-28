import os

import jieba
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def get_slides(path):
    return os.scandir(path)


def parse_pdf(file):
    opened_file = open(file, "rb")
    parser = PDFParser(opened_file)
    doc = PDFDocument(parser)
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed

    laparams = LAParams()
    pr_manager = PDFResourceManager()
    device = PDFPageAggregator(pr_manager, laparams=laparams)
    interpreter = PDFPageInterpreter(pr_manager, device)

    contents = []
    for i, page in enumerate(PDFPage.create_pages(doc)):
        interpreter.process_page(page)
        layout = device.get_result()
        for element in layout:
            if isinstance(element, LTTextBox) or isinstance(element, LTTextLine):
                text = element.get_text()
                if text.isdigit():
                    break
                contents.append(text)
    return contents


def extract_words(contents, ignored_words):
    all_words = []
    for content in contents:
        words = jieba.cut(content, cut_all=False)
        for word in words:
            trimmed_word = word.lstrip().rstrip()
            if trimmed_word == "":
                del word
            elif trimmed_word.isdigit() or trimmed_word.isspace():
                del word
            elif trimmed_word in ignored_words:
                del word
            else:
                all_words.append(word)
    return all_words
