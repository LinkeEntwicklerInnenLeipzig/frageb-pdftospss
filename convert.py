from __future__ import print_function
from __future__ import unicode_literals
from os import path
import sys
import pdfformread


def main():
    basepath = path.dirname(__file__)
    pdf_folder = path.join(basepath ,'files')
    example_sav_filename = path.join(basepath, 'example_spss.sav')
    out_sav_filename = path.join(basepath, sys.argv[1] + '_spss.sav' if len(sys.argv) > 1 else 'out_spss.sav')

    sav_settings = get_sav_settings_from_file(example_sav_filename)
    writer = create_sav_writer(out_sav_filename, sav_settings)

    pdfs = gather_pdfs(pdf_folder)
    for cnt, filename in enumerate(pdfs):
        print('Processing %d of %d' % (cnt + 1, len(pdfs)))
        data = read_pdf(filename)
        row = pdf_data_to_row(data)

    writer.close()

def gather_pdfs(folder):
    # foldername -> [filename]
    import glob
    return glob.glob(path.join(folder, '*.pdf'))

def pdf_data_to_row(data):
    ['q1a', 'q1b', 'q1c', 'q1d', 'q1e', 'q1f', 'q1g', 'q1h', 'q2a', 'q2b', 'q2b1', 'q2b2', 'q2b3', 'q2c', 'q2c1', 'q2c2', 'q2c3', 'q2d', 'q2e', 'q2e1', 'q2e2', 'q2e3', 'q2e4', 'q3a', 'q3b', 'q3c', 'q3d', 'q4a', 'q4b', 'q4b1', 'q4b2', 'q4b3', 'q4b4', 'q4b5', 'q4b6', 'q4b7', 'q4b8', 'q5a', 'q5b', 'q5c', 'q5d', 'q5e', 'q5f', 'q6', 'q7a', 'q7b', 'q7c', 'q7d', 'q7e', 'q7f', 'q7g', 'q7h', 'q7i', 'q7j', 'q7k', 'q7l', 'q7m', 'q7n', 'q7o', 'q7p', 'q7q', 'q7r', 'q7s', 'q7t', 'q7u', 'q7v', 'q7w', 'q7x', 'q7y', 'q8a', 'q8b', 'q8c', 'q8d', 'q8e', 'q8f', 'q8g', 'q8h', 'q9', 'q10a', 'q10b', 'q10c', 'q10d', 'q10e', 'q10f', 'q10g', 'q10h', 'q10i', 'q10j', 'q10k', 'q10l', 'q10m', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17a', 'q17b', 'q17c', 'q17d', 'q17e', 'q17f', 'q18', 'q19a', 'q19b', 'q19c', 'q19c1', 'q19c2', 'q19c3', 'q19c4', 'q20a', 'q20b', 'q20c', 'q20d', 'q20e', 'q20f', 'q20g', 'q20g1', 'q20g2', 'q20g4', 'q20g5', 'q20g6', 'q20g7', 'q21a', 'q21b', 'q21c', 'q21d', 'q21e', 'q21f', 'q21g', 'q21h', 'q21i', 'q21i1', 'q22', 'q22a', 'q23a', 'q23b', 'q23c', 'q23d', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47']
    print(data)

    def check(f):
        if f == u'Off':
            return 0
        if f == u'Yes':
            return 1
        raise NotImplementedError(sel, f)

    def num(f):
        if f == u'':
            return 99999.0
        else:
            return float(f)

    def zufr(f):
        if '?' in f:
            return 11.0
        if f == u'':
            return 99999.0
        return float(f)

    def sel5(f):
        if f == u'Off':
            return 99999.0
        return float(f)

    return [
    check(data['Markierfeld 1']), check(data['Markierfeld 2']), check(data['Markierfeld 3']), check(data['Markierfeld 4']), check(data['Markierfeld 5']), check(data['Markierfeld 6']), check(data['Markierfeld 7']), data['Textfeld 1'],
    check(data['Markierfeld 9']), check(data['Markierfeld 10']), check(data['Markierfeld 11']), check(data['Markierfeld 12']), check(data['Markierfeld 13']),
    'q2c', 'q2c1', 'q2c2', 'q2c3', 'q2d', 'q2e', 'q2e1', 'q2e2', 'q2e3', 'q2e4', 'q3a', 'q3b', 'q3c', 'q3d', 'q4a', 'q4b', 'q4b1', 'q4b2', 'q4b3', 'q4b4', 'q4b5', 'q4b6', 'q4b7', 'q4b8', 'q5a', 'q5b', 'q5c', 'q5d', 'q5e', 'q5f', 'q6', 'q7a', 'q7b', 'q7c', 'q7d', 'q7e', 'q7f', 'q7g', 'q7h', 'q7i', 'q7j', 'q7k', 'q7l', 'q7m', 'q7n', 'q7o', 'q7p', 'q7q', 'q7r', 'q7s', 'q7t', 'q7u', 'q7v', 'q7w', 'q7x', 'q7y', 'q8a', 'q8b', 'q8c', 'q8d', 'q8e', 'q8f', 'q8g', 'q8h', 'q9', 'q10a', 'q10b', 'q10c', 'q10d', 'q10e', 'q10f', 'q10g', 'q10h', 'q10i', 'q10j', 'q10k', 'q10l', 'q10m', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17a', 'q17b', 'q17c', 'q17d', 'q17e', 'q17f', 'q18', 'q19a', 'q19b', 'q19c', 'q19c1', 'q19c2', 'q19c3', 'q19c4', 'q20a', 'q20b', 'q20c', 'q20d', 'q20e', 'q20f', 'q20g', 'q20g1', 'q20g2', 'q20g4', 'q20g5', 'q20g6', 'q20g7', 'q21a', 'q21b', 'q21c', 'q21d', 'q21e', 'q21f', 'q21g', 'q21h', 'q21i', 'q21i1', 'q22', 'q22a', 'q23a', 'q23b', 'q23c', 'q23d', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47'
    ]

def read_pdf(filename):
    # filename -> dict
    return pdfformread.load_form(filename)

def get_sav_settings_from_file(filename):
    from savReaderWriter import SavHeaderReader
    with SavHeaderReader(filename) as sav:
        return sav.dataDictionary()

def create_sav_writer(filename, settings):
    from savReaderWriter import SavWriter
    return SavWriter(filename, **settings)

if __name__ == "__main__":
    main()
