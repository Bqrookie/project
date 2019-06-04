with open('all.txt', 'r') as f:
    cont = f.readlines()

for i in cont:
    print(str(i).split(' ')[0])