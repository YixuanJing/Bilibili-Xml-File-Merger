import os
#Author: Yixuan Jing
def merger(file1, file2, path):
    import os
    def file_name_finder(address, houzhui='.xml'):
        n = 1
        while os.path.isfile(address + str(n) + houzhui) == True:
            n = n + 1
        return n

    new_file_path = path + '/%s.xml' % file_name_finder(path + '/')
    print(new_file_path)
    with open(new_file_path, 'w') as new_file:
        new_file.write('<?xml version="1.0" encoding="UTF-8"?><i><chatserver>chat.bilibili.tv</chatserver><chatid>49052</chatid><mission>0</mission><source>k-v</source>')
        with open(file1) as f:
            print('file1:%s' % file1)
            n, c = 0, 0
            for line in f.readlines():
                n, y = n + 1, 0
                if n > 2 and line[2] != 'i':
                    new_file.write(line)
                    y = 0
                    while line[y] != ',':
                        y = y + 1
                    if c < float(line[6:y]):
                        c = float(line[6:y])
        with open(file2) as f2:
            print('file2:%s' % file2)
            for line in f2.readlines():
                y = 0
                if line[2] != 'x' and line[2] != 'i':
                    while line[y] != ',':
                        y = y + 1
                    new_file.write(line[:6] + str(float(line[6:y]) + c) + line[y:])
        new_file.write('</i>')
        return new_file_path

def space_remover(str):
    while str[-1] == ' ':
        str = str[:-1]
    return str

n = 0
while True:
    file1, file2 = space_remover(input('Input the path of first file:')), space_remover(input('Input the path of second file:'))
    if n == 0:
        new_file_path = space_remover(input('Input the path of final file:'))
    print('success, the path of new file is:%s' % merger(file1, file2, new_file_path))
    z, n = input('Do you want to continue?(N/Y):'), n + 1
    if z == 'N':
        break
print('All Tasks Are Done. Closing.')