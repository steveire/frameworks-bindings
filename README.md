
PyKF5 bindings proving ground
=============================

Dependencies

    Ubuntu
    
        sudo apt install qtbase5-dev        # For QtCore
        sudo apt install python-sphinx      # For Sphinx documentation generator
        sudo apt-install python3-sip-dev    # For sip.h

Build with

    git clone --recursive git@github.com:steveire/frameworks-bindings.git
    cd frameworks-bindings
    mkdir build
    cd build
    cmake ..
    cmake --build .

Then run the tests

    $ ctest
    Test project /tmpframeworks-bindings/build
          Start  1: Py2kitemmodels
          Start  2: Py3kitemmodels
          Start  3: Py2kcoreaddons
          Start  4: Py3kcoreaddons
          Start  5: Py2kdbusaddons
          Start  6: Py3kdbusaddons
    1/24 Test  #4: Py3kcoreaddons ...................   Passed    0.18 sec
    2/24 Test  #5: Py2kdbusaddons ...................   Passed    0.18 sec
    3/24 Test  #1: Py2kitemmodels ...................   Passed    0.18 sec
    4/24 Test  #3: Py2kcoreaddons ...................   Passed    0.18 sec
    5/24 Test  #2: Py3kitemmodels ...................   Passed    0.19 sec
          Start  7: Py2kguiaddons
          Start  8: Py3kguiaddons
          Start  9: Py2kwidgetsaddons
          Start 10: Py3kwidgetsaddons
          Start 11: Py2kjobwidgets
    6/24 Test  #7: Py2kguiaddons ....................   Passed    0.07 sec
    7/24 Test  #9: Py2kwidgetsaddons ................   Passed    0.13 sec
    8/24 Test  #6: Py3kdbusaddons ...................   Passed    0.31 sec
    9/24 Test #11: Py2kjobwidgets ...................   Passed    0.12 sec
    10/24 Test #10: Py3kwidgetsaddons ................   Passed    0.13 sec
    11/24 Test  #8: Py3kguiaddons ....................   Passed    0.13 sec
          Start 12: Py3kjobwidgets
          Start 13: Py2kconfig
          Start 14: Py3kconfig
          Start 15: Py2kcompletion
          Start 16: Py3kcompletion
          Start 17: Py2kauth
    12/24 Test #17: Py2kauth .........................   Passed    0.20 sec
    13/24 Test #14: Py3kconfig .......................   Passed    0.20 sec
    14/24 Test #15: Py2kcompletion ...................   Passed    0.20 sec
    15/24 Test #12: Py3kjobwidgets ...................   Passed    0.21 sec
          Start 18: Py3kauth
          Start 19: Py2kcodecs
          Start 20: Py3kcodecs
          Start 21: Py2ki18n
    16/24 Test #13: Py2kconfig .......................   Passed    0.21 sec
    17/24 Test #21: Py2ki18n .........................   Passed    0.10 sec
    18/24 Test #19: Py2kcodecs .......................   Passed    0.10 sec
    19/24 Test #16: Py3kcompletion ...................   Passed    0.31 sec
    20/24 Test #18: Py3kauth .........................   Passed    0.13 sec
          Start 22: Py3ki18n
          Start 23: Py2kconfigwidgets
          Start 24: Py3kconfigwidgets
    21/24 Test #20: Py3kcodecs .......................   Passed    0.23 sec
    22/24 Test #22: Py3ki18n .........................   Passed    0.10 sec
    23/24 Test #23: Py2kconfigwidgets ................   Passed    0.13 sec
    24/24 Test #24: Py3kconfigwidgets ................   Passed    0.15 sec


Then run the test app:

    python2 ../testapp.py prefix/lib/python2.7/dist-packages

    python3 ../testapp.py prefix/lib/python3.5/dist-packages
