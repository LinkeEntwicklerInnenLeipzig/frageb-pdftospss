from __future__ import print_function
from __future__ import unicode_literals
from os import path
import pdfformread


def main():
    basepath = path.dirname(__file__)
    pdf_folder = path.join(basepath ,'files')
    example_sav_filename = path.join(basepath, 'example_spss.sav')
    out_sav_filename = path.join(basepath, 'out_spss.sav')

    sav_settings = get_sav_settings_from_file(example_sav_filename)

    for filename in gather_pdfs(pdf_folder):
        data = read_pdf(filename)

    writer = create_sav_writer(out_sav_filename, sav_settings)
    writer.close()

def gather_pdfs(folder):
    # foldername -> [filename]
    import glob
    return glob.glob(path.join(folder, '*.pdf'))

def read_pdf(filename):
    # filename -> dict
    return pdfformread.load_form(filename)

def new_spss(filename):
    # filename -> SavWriter
    return None

def get_sav_settings_from_file(filename):
    from savReaderWriter import SavHeaderReader
    with SavHeaderReader(filename) as sav:
        return sav.dataDictionary()

def create_sav_writer(filename, settings):
    from savReaderWriter import SavWriter
    return SavWriter(filename, **settings)

if __name__ == "__main__":
    main()
