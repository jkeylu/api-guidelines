src_file = open('./Guidelines.md')
dest_file = open('./Guidelines.zh-cn.md', 'w')
translate_file = open('./Guidelines.zh-cn.translation')

buf = ''
a = ''
b = ''

while True:
    chunk = src_file.read(10)

    if chunk == '':
        dest_file.write(buf)
        break

    buf += chunk

    while a == '':
        a = translate_file.readline()
        if a == '':
            break
        a = a.strip()
        if a == '':
            continue
        b = translate_file.readline()
        b = b.strip()

    i = buf.find(a)
    if i >= 0:
        end = i + len(a)
        tmp = buf[0:end]
        tmp = tmp.replace(a, b, 1)
        buf = buf[end:]
        dest_file.write(tmp)
        a = ''
        b = ''

src_file.close()
dest_file.close()
translate_file.close()
