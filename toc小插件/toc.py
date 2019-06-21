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
        tmp_str = res.split(' ')[1].replace('\r\n', '').lstrip().rstrip()
        result = ' ' * num * 2 + '* [' + tmp_str + '](#' + tmp_str + ')'
        print(result[2:])
        # print(res[2:])
