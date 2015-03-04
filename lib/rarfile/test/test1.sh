#! /bin/sh

PYTHONPATH=..:$PYTHONPATH
export PYTHONPATH

JAVA_OPTIONS="-Dpython.path=`pwd`/.."
export JAVA_OPTIONS

plist="python2.4 python2.5 python2.6 python2.7 python3.1 python3.2 python3.3 python3.4 pypy jython jython2.7"

rm -f test.diffs

for py in $plist; do
  if which $py > /dev/null; then
    for f in files/*.rar; do
      printf "%s -> %-30s .. " $py $f
      $py ../dumprar.py -t -t -v -ppassword $f > $f.$py
      if diff -uw $f.exp $f.$py > /dev/null; then
        echo "ok"
      else
        echo "FAIL"
        echo "#### $py ####" >> test.diffs
        diff -uw $f.exp $f.$py >> test.diffs
      fi
    done
    echo ""
  else
    echo $py not available
    echo ""
  fi
done

