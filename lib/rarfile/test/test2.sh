#! /bin/sh

cp ../rarfile.py .

#ulimit -n 16

plist="python2.4 python2.5 python2.6 python2.7 python3.1 python3.2 python3.3 python3.4 pypy jython jython2.7"

for py in $plist; do
  if which $py > /dev/null; then
    echo "== $py =="
    $py ./testseek.py
    $py ./testio.py
    $py ./testcorrupt.py --quick
  fi
done

rm -f rarfile.py

