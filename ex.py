from savReaderWriter import SavReader

f = "example_spss.sav"

with SavReader(f, returnHeader=True) as reader:
    header = reader.next()
    for record in reader:
        print(record)

data = SavReader(f)
list_of_lists = data.all()
data.close()
print(list_of_lists)
