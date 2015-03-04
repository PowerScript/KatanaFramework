
rarfile - RAR archive reader for Python
=======================================

This is Python module for RAR_ archive reading.  The interface
is made as zipfile_ like as possible.  Licensed under ISC_
license.

.. _RAR: http://en.wikipedia.org/wiki/RAR
.. _zipfile: http://docs.python.org/library/zipfile.html
.. _ISC: http://en.wikipedia.org/wiki/ISC_license

Features:

- Supports both RAR 2.x and 3.x archives.
- Supports multi volume archives.
- Supports Unicode filenames.
- Supports password-protected archives.
- Supports archive and file comments.
- Archive parsing and non-compressed files are handled in pure Python code.
- For compressed files runs ``unrar`` utility.
- Works with both Python 2.x and 3.x.



Documentation:

.. toctree::
   :maxdepth: 1

   Module Documentation <api>
   FAQs <faq>
   Release News  <news>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

