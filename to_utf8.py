import sys
import os


origin_name = sys.argv[1]
if len(sys.argv) == 3:
    to_name = sys.argv[2]
elif len(sys.argv) == 2:
    to_name = origin_name
else:
    print("ERROR: wrong arg number")
    os._exit(0)


def write_to_file(data, filename):
    with open(filename, 'wb') as f:
        data = data.encode('utf-8')
        f.write(data)
        f.close()
        return
    print('ERROR: fail to create and write file:  ' + filename)


with open(origin_name, 'rb') as f:
    data = f.read()
    try:
        data = data.decode('utf-8')
        print('the original file is utf-8')
        print('no need to change')
        os._exit(0)
    except:
        pass

    try:
        data = data.decode('gb2312')
        f.close()
        write_to_file(data, to_name)
        print('the original encoding is gb2312')
        print('already changed to UTF-8 to: ' + to_name)
        os._exit(0)
    except:
        pass

    try:
        data = data.decode('gbk')
        f.close()
        write_to_file(data, to_name)
        print('the original encoding is gbk')
        print('already changed to UTF-8 to: ' + to_name)
        os._exit(0)
    except:
        pass

    try:
        data = data.decode('gb18030')
        f.close()
        write_to_file(data, to_name)
        print('the original encoding is gb18030')
        print('already changed to UTF-8 to: ' + to_name)
        os._exit(0)
    except:
        pass

print('sorry, transfer failed')
