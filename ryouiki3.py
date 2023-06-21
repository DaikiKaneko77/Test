import os

directory='sample'
sum = 0

for file_name in os.listdir(directory):
    if file_name.startswith('kitamura_')and file_name.endswith("kgu.txt"):
        number_part=file_name[len("kitamura_"):-len("_kgu.txt")]
        if int (number_part) % 2 != 0:
            with open(os.path.join(directory,file_name),'r') as file:
                    sum+=int(file.read().strip())
print("合計は:", sum)