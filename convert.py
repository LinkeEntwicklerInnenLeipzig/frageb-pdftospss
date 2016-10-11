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
        writer.writerow(row)

    writer.close()

def gather_pdfs(folder):
    # foldername -> [filename]
    import glob
    return glob.glob(path.join(folder, '*.pdf'))

def pdf_data_to_row(data):
    ['q1a', 'q1b', 'q1c', 'q1d', 'q1e', 'q1f', 'q1g', 'q1h', 'q2a', 'q2b', 'q2b1', 'q2b2', 'q2b3', 'q2c', 'q2c1', 'q2c2', 'q2c3', 'q2d', 'q2e', 'q2e1', 'q2e2', 'q2e3', 'q2e4', 'q3a', 'q3b', 'q3c', 'q3d', 'q4a', 'q4b', 'q4b1', 'q4b2', 'q4b3', 'q4b4', 'q4b5', 'q4b6', 'q4b7', 'q4b8', 'q5a', 'q5b', 'q5c', 'q5d', 'q5e', 'q5f', 'q6', 'q7a', 'q7b', 'q7c', 'q7d', 'q7e', 'q7f', 'q7g', 'q7h', 'q7i', 'q7j', 'q7k', 'q7l', 'q7m', 'q7n', 'q7o', 'q7p', 'q7q', 'q7r', 'q7s', 'q7t', 'q7u', 'q7v', 'q7w', 'q7x', 'q7y', 'q8a', 'q8b', 'q8c', 'q8d', 'q8e', 'q8f', 'q8g', 'q8h', 'q9', 'q10a', 'q10b', 'q10c', 'q10d', 'q10e', 'q10f', 'q10g', 'q10h', 'q10i', 'q10j', 'q10k', 'q10l', 'q10m', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17a', 'q17b', 'q17c', 'q17d', 'q17e', 'q17f', 'q18', 'q19a', 'q19b', 'q19c', 'q19c1', 'q19c2', 'q19c3', 'q19c4', 'q20a', 'q20b', 'q20c', 'q20d', 'q20e', 'q20f', 'q20g', 'q20g1', 'q20g2', 'q20g4', 'q20g5', 'q20g6', 'q20g7', 'q21a', 'q21b', 'q21c', 'q21d', 'q21e', 'q21f', 'q21g', 'q21h', 'q21i', 'q21i1', 'q22', 'q22a', 'q23a', 'q23b', 'q23c', 'q23d', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47']

    def check(f):
        if f == u'Off':
            return 0.0
        if f == u'Yes':
            return 1.0
        raise NotImplementedError(sel, f)

    def num(f):
        try:
            return float(f)
        except:
            return 99999.0

    def zufr(f):
        if '?' in f:
            return 11.0
        if f == u'':
            return 99999.0
        return float(f)

    def sel(f):
        if f == u'Off':
            return 99999.0
        return float(f)

    def radio(*fs):
        for cnt, f in enumerate(fs):
            if f == u'Yes':
                return float(cnt + 1)
        return 99999.0

    return [
    check(data['Markierfeld 1']), check(data['Markierfeld 2']), check(data['Markierfeld 3']), check(data['Markierfeld 4']), check(data['Markierfeld 5']), check(data['Markierfeld 6']), check(data['Markierfeld 7']), data['Textfeld 1'],
    check(data['Markierfeld 9']), check(data['Markierfeld 10']), check(data['Markierfeld 11']), check(data['Markierfeld 12']), check(data['Markierfeld 13']),
    check(data['Markierfeld 14']), check(data['Markierfeld 15']), check(data['Markierfeld 16']), check(data['Markierfeld 17']), check(data['Markierfeld 18']), check(data['Markierfeld 19']), check(data['Markierfeld 20']), check(data['Markierfeld 21']), check(data['Markierfeld 22']), data['Textfeld 1'],
    # wo bist du engagiert
    check(data['Markierfeld 24']), check(data['Markierfeld 25']), check(data['Markierfeld 26']), check(data['Markierfeld 27']),
    # wahlkampf
    check(data['Markierfeld 28']), check(data['Markierfeld 29']), check(data['Markierfeld 30']), check(data['Markierfeld 31']), check(data['Markierfeld 32']), check(data['Markierfeld 33']), check(data['Markierfeld 34']), check(data['Markierfeld 35']), check(data['Markierfeld 36']), check(data['Markierfeld 37']),
    # unterstuetzung
    check(data['Markierfeld 38']), check(data['Markierfeld 39']), check(data['Markierfeld 40']), check(data['Markierfeld 41']), check(data['Markierfeld 42']), data['Textfeld 10'],
    # regierungsbeteiligung
    radio(data['Markierfeld 44'], data['Markierfeld 45'], data['Markierfeld 46'], data['Markierfeld 47']),
    # interessen
    check(data['Markierfeld 48']), check(data['Markierfeld 49']), check(data['Markierfeld 50']), check(data['Markierfeld 51']), check(data['Markierfeld 52']), check(data['Markierfeld 53']), check(data['Markierfeld 54']), check(data['Markierfeld 55']), check(data['Markierfeld 56']), check(data['Markierfeld 57']), check(data['Markierfeld 58']), check(data['Markierfeld 59']), check(data['Markierfeld 60']), check(data['Markierfeld 61']), check(data['Markierfeld 62']), check(data['Markierfeld 63']), check(data['Markierfeld 64']), check(data['Markierfeld 65']), check(data['Markierfeld 66']), check(data['Markierfeld 67']), check(data['Markierfeld 68']), check(data['Markierfeld 69']), check(data['Markierfeld 70']), check(data['Markierfeld 71']), data['Textfeld 11'],
    # bereitstellen
    check(data['Markierfeld 73']), check(data['Markierfeld 74']), check(data['Markierfeld 75']), check(data['Markierfeld 76']), check(data['Markierfeld 77']), check(data['Markierfeld 78']), check(data['Markierfeld 79']), data['Textfeld 12'],
    # wie oft
    sel(data['aktiv']),
    # gremien
    check(data['Markierfeld 87']), check(data['Markierfeld 88']), check(data['Markierfeld 89']), check(data['Markierfeld 90']), check(data['Markierfeld 91']), check(data['Markierfeld 92']), check(data['Markierfeld 93']), check(data['Markierfeld 94']), check(data['Markierfeld 95']), check(data['Markierfeld 96']), check(data['Markierfeld 97']), check(data['Markierfeld 98']), data['Textfeld 13'],
    # kollegen
    radio(data['Markierfeld 100'], data['Markierfeld 101']),
    sel(data['ArbeitStavo']),
    sel(data['ErgStavo']),
    sel(data['AnlStavo']),
    sel(data['PresStavo']),
    data['Textfeld 14'],
    check(data['Markierfeld 102']), check(data['Markierfeld 103']), check(data['Markierfeld 104']), check(data['Markierfeld 105']), check(data['Markierfeld 106']), data['Textfeld 15'],
    num(data['Textfeld 16']), # veranst
    # engagemtn
    check(data['Markierfeld 108']), check(data['Markierfeld 109']), check(data['Markierfeld 110']), check(data['Markierfeld 111']), check(data['Markierfeld 112']), check(data['Markierfeld 113']), check(data['Markierfeld 114']),
    # informationen
    check(data['Markierfeld 115']), check(data['Markierfeld 116']), check(data['Markierfeld 117']), check(data['Markierfeld 118']), check(data['Markierfeld 119']), check(data['Markierfeld 120']), check(data['Markierfeld 121']), check(data['Markierfeld 122']), check(data['Markierfeld 123']), check(data['Markierfeld 124']), check(data['Markierfeld 125']), check(data['Markierfeld 126']), data['Textfeld 17'],
    # informationen
    check(data['Markierfeld 128']), check(data['Markierfeld 129']), check(data['Markierfeld 130']), check(data['Markierfeld 131']), check(data['Markierfeld 132']), check(data['Markierfeld 133']), check(data['Markierfeld 134']), check(data['Markierfeld 135']), check(data['Markierfeld 136']), data['Textfeld 18'],
    check(data['Markierfeld 137']), data['Textfeld 6'],
    # engagement
    check(data['Markierfeld 139']), check(data['Markierfeld 140']), check(data['Markierfeld 141']), data['Textfeld 19'],
    # Zufriedenheit Partei
    num(data['Textfeld 20']),
    num(data['Textfeld 21']),
    num(data['Textfeld 22']),
    num(data['Textfeld 23']),
    num(data['Textfeld 24']),
    num(data['Textfeld 25']),
    # Zufriedenheit Parlament
    num(data['Textfeld 26']),
    num(data['Textfeld 27']),
    num(data['Textfeld 28']),
    num(data['Textfeld 29']),
    num(data['Textfeld 30']),
    # Schluss
    num(data['Textfeld 31']),
    radio(data['Markierfeld 207'], data['Markierfeld 208']), # geschlecht
    data['Textfeld 32'],
    num(data['Textfeld 33']),
    num(data['Textfeld 34']),
    num(data['Textfeld 35']),
    sel(data['abschl']),
    num(data['Textfeld 36']),
    data['Textfeld 37'],
    data['Textfeld 38'],
    data['Textfeld 39'],
    data['Textfeld 40'],
    data['Textfeld 41']
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
    return SavWriter(filename, ioUtf8=True, **settings)

if __name__ == "__main__":
    main()
