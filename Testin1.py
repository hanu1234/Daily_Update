data_len = int(input("Enter The Data Len"))

data = 'FF'
new_data = []
for i in range(data_len):
    new_data.append(data)

data = " ".join(new_data)
required_data = '"' + data + '"'
print(required_data)
