winvers
------

Definitive Windows version checker for Python

This module provides
~~~~~~~~~~~~~~~~~~~~

-  A list of Windows versions constants (comparable between them)
-  A function to get the Windows OS version running on the machine

Compatibility
~~~~~~~~~~~~~

-  Python 2.7.x
-  Python 3.x and newer

Constants list
~~~~~~~~~~~~~~

::

    NO_WIN
    WIN_10_1709
    WIN_10_1703
    WIN_10_1607
    WIN_10_1511
    WIN_10_1507
    WIN_10
    WIN_8_1
    WIN_8
    WIN_7_SP1
    WIN_7
    WIN_VISTA_SP1
    WIN_VISTA
    WIN_XP_X64_SP2
    WIN_XP_X64_SP1
    WIN_XP_X64
    WIN_XP_SP3
    WIN_XP_SP2
    WIN_XP_SP1
    WIN_XP
    WIN_2000
    WIN_SERVER_2016_1709
    WIN_SERVER_2016_1607
    WIN_SERVER_2016
    WIN_SERVER_2012_R2
    WIN_SERVER_2012
    WIN_SERVER_2008_R2
    WIN_SERVER_2008
    WIN_SERVER_2003_SP2
    WIN_SERVER_2003_SP1
    WIN_SERVER_2003

Example
~~~~~~~

::

    import winvers

    if winvers.get_version() >= winvers.WIN_VISTA:
        print('Your OS is newer than Windows XP')

    if winvers.get_version() >= winvers.WIN_10:
        print('Your OS is Windows 10')

Sources
~~~~~~~

-  https://docs.python.org/2/library/sys.html#sys.getwindowsversion
-  https://docs.python.org/3/library/sys.html#sys.getwindowsversion
-  https://en.wikipedia.org/wiki/Windows\_10\_version\_history
-  https://en.wikipedia.org/wiki/Windows\_Server\_2016#Version\_history
-  https://msdn.microsoft.com/en-us/library/windows/desktop/ms724832(v=vs.85).aspx
