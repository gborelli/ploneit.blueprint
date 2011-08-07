from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ploneit.blueprint',
      version=version,
      description="plone.it migration blueprint",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'simplejson',
          'collective.transmogrifier',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [collective.transmogrifier]
      ploneit.blueprint=ploneit.blueprint
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
