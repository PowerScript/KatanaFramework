#! /usr/bin/env python

import rarfile, os, os.path, time, sys

try:
    from io import BufferedReader, TextIOWrapper
except ImportError:
    print('no io module')
    sys.exit(0)
    def BufferedReader(x): return x
    def TextIOWrapper(x): return x

def test_readline(rf, fn):
    f = rf.open(fn)
    tr = TextIOWrapper(BufferedReader(f))
    while 1:
        ln = tr.readline()
        if not ln:
            break
    tr.close()

def main():
    files = ['stest1.txt', 'stest2.txt']
    arc = 'files/seektest.rar'

    rf = rarfile.RarFile(arc, crc_check=0)
    for fn in files:
        sys.stdout.write('test/readline: %s .. ' % fn)
        sys.stdout.flush()
        test_readline(rf, fn)
        print('ok')

if __name__ == '__main__':
    main()

