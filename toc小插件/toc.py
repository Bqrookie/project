import re

with open('a.md', 'rb') as f:
    content = f.readlines()

# print(type(content))

for x in content:
    # print(x.decode('utf-8'))
    # continue
    res = x.decode('utf-8')
    ret = re.findall('^#', res)
    if ret:
        num = res.count('#')
        result = ' ' * num * 2 + '* [' + res.split(' ')[1].replace('\r\n', '') + '](#' + res.split(' ')[1].replace('\r\n', '') + ')'
        print(result[2:])
        # print(res[2:])
