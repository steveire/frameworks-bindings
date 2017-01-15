
cmake_minimum_required(VERSION 3.4)

project(frameworks-bindings)

include(ExternalProject)
include(CTest)

enable_testing()

macro(add_repo name DEPENDS_keyword)
  ExternalProject_Add(${name}
    SOURCE_DIR "${CMAKE_SOURCE_DIR}/${name}"
    DOWNLOAD_COMMAND ""
    CMAKE_GENERATOR "${CMAKE_GENERATOR}"
    CMAKE_ARGS "-DCMAKE_INSTALL_PREFIX=${CMAKE_BINARY_DIR}/prefix;-DKDE_INSTALL_PYTHONBINDINGSDIR=packageprefix"
    DEPENDS "${ARGN}"
  )
  set(pythontest "${CMAKE_SOURCE_DIR}/${name}/autotests/pythontest.py")
  if (EXISTS ${pythontest})
    add_test(NAME Py2${name} COMMAND python2 ${pythontest} ${CMAKE_BINARY_DIR}/prefix/lib/python2.7/packageprefix)
    add_test(NAME Py3${name} COMMAND python3 ${pythontest} ${CMAKE_BINARY_DIR}/prefix/lib/python3.5/packageprefix)
  endif()
endmacro()

add_repo(extra-cmake-modules DEPENDS "")

add_repo(kitemmodels DEPENDS extra-cmake-modules)
add_repo(kitemviews DEPENDS extra-cmake-modules)
add_repo(kcoreaddons DEPENDS extra-cmake-modules)
add_repo(kdbusaddons DEPENDS extra-cmake-modules)
add_repo(kguiaddons DEPENDS extra-cmake-modules)
add_repo(kwidgetsaddons DEPENDS extra-cmake-modules)
add_repo(kjobwidgets DEPENDS kcoreaddons kwidgetsaddons)
add_repo(kconfig DEPENDS extra-cmake-modules)
add_repo(kcompletion DEPENDS kconfig kwidgetsaddons)
add_repo(kauth DEPENDS kcoreaddons)
add_repo(kcodecs DEPENDS extra-cmake-modules)
add_repo(ki18n DEPENDS extra-cmake-modules)
add_repo(kconfigwidgets DEPENDS kcodecs kwidgetsaddons kconfig kauth)
