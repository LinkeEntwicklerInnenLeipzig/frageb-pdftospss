from savReaderWriter import SavHeaderReader

f = "example_spss.sav"

data = SavHeaderReader(f)
d = data.dataDictionary()
for k in d:
    print(k, d[k])
data.close()
