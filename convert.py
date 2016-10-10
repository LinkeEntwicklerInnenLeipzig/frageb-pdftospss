from __future__ import print_function
from __future__ import unicode_literals
from os import path
import pdfformread


def main():
    pdf_folder = path.join(path.dirname(__file__) ,'files')
    for filename in gather_pdfs(pdf_folder):
        data = read_pdf(filename)
        print(data)

def gather_pdfs(folder):
    # foldername -> [filename]
    import glob
    return glob.glob(path.join(folder, '*.pdf'))

def read_pdf(filename):
    # filename -> dict
    return pdfformread.load_form(filename)



if __name__ == "__main__":
    main()
