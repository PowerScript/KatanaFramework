#! /usr/bin/env python

import rarfile, os, os.path, time, sys

def show_fds():
    fdir = "/proc/%d/fd" % os.getpid()
    if os.path.isdir(fdir):
        os.system('printf "fds = "; ls -l %s | wc -l' % fdir)

def do_seek(f, pos, lim):
    ofs = pos*4
    fsize = lim*4

    if ofs < 0:
        exp = 0
    elif ofs > fsize:
        exp = fsize
    else:
        exp = ofs

    f.seek(ofs)

    got = f.tell()

    if got != exp:
        raise Exception('seek failed (got=%d, exp=%d)' % (got, exp))
    ln = f.read(4)
    if got == fsize and ln:
        raise Exception('unexpected read')
    if not ln and got < fsize:
        raise Exception('unexpected read failure')
    if ln:
        spos = int(ln)
        if spos*4 != got:
            raise Exception('unexpected pos: spos=%d pos=%d' % (spos, pos))

def test_seek(rf, fn):
    inf = rf.getinfo(fn)
    cnt = int(inf.file_size / 4)
    f = rf.open(fn)

    do_seek(f, int(cnt/2), cnt)
    do_seek(f, 0, cnt)

    for i in range(int(cnt/2)):
        do_seek(f, i*2, cnt)

    for i in range(cnt):
        do_seek(f, i*2 - int(cnt / 2), cnt)

    for i in range(cnt + 10):
        do_seek(f, cnt - i - 5, cnt)

    f.close()

    print('OK')

def test_arc(arc, desc):
    files = ['stest1.txt', 'stest2.txt']
    rf = rarfile.RarFile(arc, crc_check=0)
    for fn in files:
        sys.stdout.write('%s | test/seek %s .. ' % (desc, fn))
        sys.stdout.flush()
        test_seek(rf, fn)

def main():
    arc = 'files/seektest.rar'
    data = open(arc, 'rb').read()

    # filename
    test_arc(arc, "fn")

    # filelike: cStringIO
    try:
        import cStringIO
        test_arc(cStringIO.StringIO(data), "cStringIO")
    except ImportError:
        pass

    # filelike: io.BytesIO, io.open()
    try:
        import io
        test_arc(io.BytesIO(data), "io.BytesIO")
        test_arc(io.open(arc, 'rb'), "io.open")
    except ImportError:
        pass

    # filelike: StringIO
    try:
        import StringIO
        test_arc(StringIO.StringIO(data), "StringIO")
    except ImportError:
        pass

    # filelike: file()
    test_arc(open(arc, 'rb'), "file")

    time.sleep(1)
    show_fds()

if __name__ == '__main__':
    main()

