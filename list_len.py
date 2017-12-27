__author__ = 'songqi'

def list_len(lists):
    lens = len(lists)
    i = 0
    j = 0
    while i < lens:
        tmp = lists[i]
        if tmp = 0:
            if i = lens - 1
                flg = 'ture'
            else:
                flg = 'false'
        else:
            j = i + 1
            i = i + tmp
            print i
    if j == lens:
        flg = 'ture'
    else:
        flg = 'false'
    print flg

a = [2, 6, 3, 1, 1, 4, 1, 1, 1, 1]
b = [2, 2, 0, 0, 1, 1, 1, 1, 4]
list_len(b)