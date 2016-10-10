from savReaderWriter import SavHeaderReader
import sys

f = "example_spss.sav"

data = SavHeaderReader(f)
d = data.dataDictionary()
print(d['varLabels'][sys.argv[1]])
data.close()
