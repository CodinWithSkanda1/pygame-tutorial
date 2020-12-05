# Codin' With Skanda - Pygame Tutorial
Learning Python's 3rd Party module; PyGame

### This is PyGame's README:

pygame
======

|TravisBuild| |AppVeyorBuild| |LaunchpadBuild|
|PyPiVersion| |PyPiLicense| |Python2| |Python3| |GithubCommits|
|LGTMAlerts| |LGTMGradePython| |LGTMGradeC| |Coverity|

pygame_ is a Free and Open Source cross-platform library
for the development of multimedia applications like video games on Python.
It uses the `Simple DirectMedia Layer library`_ and several other
popular libraries to abstract most common functions and makes writing
these program a more intuitive task.

`We need your help`_ to make pygame the best it can be!


Installation
------------

::

   pip install pygame

You should definitely begin by installing a binary package for your
system.  The binary packages usually come with or give the
information needed for dependencies.  Choose an appropriate
installer for your system and version of Python from the pygame
`downloads page`_.

Installing from source is fairly automated.  The most work will
involve compiling and installing all the pygame dependencies.  Once
that is done, run the ``setup.py`` script which will attempt to
auto-configure, build, and install pygame.

Much more information about installing and compiling is available
on the `Getting Started wiki page`_.


Help
----

If you are just getting started with pygame, you should be able to
get started fairly quickly.  Pygame comes with many tutorials and
introductions.  There is also full reference documentation for the
entire library.  Browse the documentation from the documentation
index: docs/index.html.

On the pygame website, there is also an online copy of this
documentation.  You should know that the online documentation stays
up to date with the development version of pygame in hg.  This may
be a bit newer than the version of pygame you are using.

Best of all, the examples directory has many playable small programs
which can get you started playing with the code right away.


Credits
-------

Thanks to everyone who has helped contribute to this library.
Special thanks are also in order.

* Marcus Von Appen: many changes, and fixes, 1.7.1+ freebsd maintainer
* Lenard Lindstrom: the 1.8+ windows maintainer, many changes, and fixes
* Brian Fisher for svn auto builder, bug tracker and many contributions
* Rene Dudfield: many changes, and fixes, 1.7+ release manager/maintainer
* Phil Hassey for his work on the pygame.org website
* DR0ID for his work on the sprite module
* Richard Goedeken for his smoothscale function
* Ulf Ekström for his pixel perfect collision detection code
* Pete Shinners: original author
* David Clark for filling the right-hand-man position
* Ed Boraas and Francis Irving: Debian packages
* Maxim Sobolev: FreeBSD packaging
* Bob Ippolito: MacOS and OS X porting (much work!)
* Jan Ekhol, Ray Kelm, and Peter Nicolai: putting up with early design ideas
* Nat Pryce for starting our unit tests
* Dan Richter for documentation work
* TheCorruptor for his incredible logos and graphics
* Nicholas Dudfield: many test improvements
* Alex Folkner for pygame-ctypes

Thanks to those sending in patches and fixes: Niki Spahiev, Gordon
Tyler, Nathaniel Pryce, Dave Wallace, John Popplewell, Michael Urman,
Andrew Straw, Michael Hudson, Ole Martin Bjoerndalen, Herve Cauwelier,
James Mazer, Lalo Martins, Timothy Stranex, Chad Lester, Matthias
Spiller, Bo Jangeborg, Dmitry Borisov, Campbell Barton, Diego Essaya,
Eyal Lotem, Regis Desgroppes, Emmanuel Hainry, Randy Kaelber
Matthew L Daniel, Nirav Patel, Forrest Voight, Charlie Nolan,
Frankie Robertson, John Krukoff, Lorenz Quack, Nick Irvine,
Michael George, Saul Spatz, Thomas Ibbotson, Tom Rothamel, Evan Kroske,
Cambell Barton.

And our bug hunters above and beyond: Angus, Guillaume Proux, Frank
Raiser, Austin Henry, Kaweh Kazemi, Arturo Aldama, Mike Mulcheck,
Michael Benfield, David Lau

There's many more folks out there who've submitted helpful ideas, kept
this project going, and basically made our life easier.  Thanks!

Many thank you's for people making documentation comments, and adding to the
pygame.org wiki.

Also many thanks for people creating games and putting them on the
pygame.org website for others to learn from and enjoy.

Lots of thanks to James Paige for hosting the pygame bugzilla.

Also a big thanks to Roger Dingledine and the crew at SEUL.ORG for our
excellent hosting.

Dependencies
------------

Pygame is obviously strongly dependent on SDL and Python.  It also
links to and embeds several other smaller libraries.  The font
module relies on SDL_tff, which is dependent on freetype.  The mixer
(and mixer.music) modules depend on SDL_mixer.  The image module
depends on SDL_image, which also can use libjpeg and libpng.  The
transform module has an embedded version of SDL_rotozoom for its
own rotozoom function.  The surfarray module requires the Python
NumPy package for its multidimensional numeric arrays.
Dependency versions:

* CPython >= 2.7 or PyPy >= 6.0.0 (and pypy3)
* SDL >= 1.2.15
* SDL_mixer >= 1.2.13
* SDL_image >= 1.2.12
* SDL_tff >= 2.0.11
* SDL_gfx (optional, vendored in)
* NumPy >= 1.6.2 (optional)


Contribute
----------

Please see https://www.pygame.org/contribute.html


License
-------

This library is distributed under `GNU LGPL version 2.1`_, which can
be found in the file ``docs/LGPL.txt``.  We reserve the right to place
future versions of this library under a different license.

This basically means you can use pygame in any project you want,
but if you make any changes or additions to pygame itself, those
must be released with a compatible license (preferably submitted
back to the pygame project).  Closed source and commercial games are fine.

The programs in the ``examples`` subdirectory are in the public domain.

See docs/licenses for licenses of dependencies.


.. |TravisBuild| image:: https://travis-ci.org/pygame/pygame.svg?branch=master
   :target: https://travis-ci.org/pygame/pygame

.. |AppVeyorBuild| image:: https://ci.appveyor.com/api/projects/status/x4074ybuobsh4myx?svg=true
   :target: https://ci.appveyor.com/project/pygame/pygame

.. |LaunchpadBuild| image:: https://www.pygame.org/images/launchpad_build.svg?svg=true
   :target: https://code.launchpad.net/~pygame/+recipe/pygame-daily

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/pygame.svg?v=1
   :target: https://pypi.python.org/pypi/pygame

.. |PyPiLicense| image:: https://img.shields.io/pypi/l/pygame.svg?v=1
   :target: https://pypi.python.org/pypi/pygame

.. |Python2| image:: https://img.shields.io/badge/python-2-blue.svg?v=1
.. |Python3| image:: https://img.shields.io/badge/python-3-blue.svg?v=1

.. |GithubCommits| image:: https://img.shields.io/github/commits-since/pygame/pygame/1.9.6.svg
   :target: https://github.com/pygame/pygame/compare/1.9.6...master

.. |LGTMAlerts| image:: https://img.shields.io/lgtm/alerts/g/pygame/pygame.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/pygame/pygame/alerts/

.. |LGTMGradePython| image:: https://img.shields.io/lgtm/grade/python/g/pygame/pygame.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/pygame/pygame/context:python

.. |LGTMGradeC| image:: https://img.shields.io/lgtm/grade/cpp/g/pygame/pygame.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/pygame/pygame/context:cpp

.. |Coverity| image:: https://scan.coverity.com/projects/12288/badge.svg?v=2
   :target: https://scan.coverity.com/projects/pygame

.. _pygame: https://www.pygame.org
.. _Simple DirectMedia Layer library: https://www.libsdl.org
.. _We need your help: https://www.pygame.org/contribute.html
.. _downloads page: https://www.pygame.org/download.shtml
.. _Getting Started wiki page: https://www.pygame.org/wiki/Compilation
.. _GNU LGPL version 2.1: https://www.gnu.org/copyleft/lesser.html
