import re

with open('test.md', 'r') as f:
    content = f.readlines()

for x in content:
    ret = re.findall('^#', x, re.I)
    if ret:
        num = x.count('#')
        res = ' ' * num * 2 + '* [' + x[num:].replace("\n", "").replace(" ", "") + '](#' + x[num:].replace("\n", "").replace(" ", "") + ')'
        print(res[2:])
