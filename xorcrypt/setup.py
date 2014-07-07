#!/usr/bin/python

from distutils.core import setup, Extension

__version__ = "0.2"

macros = [('MODULE_VERSION', '"%s"' % __version__)]

setup(name         = "xorcrypt2",
      version      = __version__,
      author       = "fk",
      author_email = "gf0842wf@gmail.com",
      url          = "",
      download_url = "",
      description  = "Fast XOR encrypt/decrypt for Python",
      long_description = open('README').read(),
      license      = "LGPL",
      platforms    = ["Win/Linux"],
      ext_modules  = [
        Extension(name='xorcrypt2', sources=['xorcrypt2.c'], define_macros=macros)
      ]
)
