import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_debugtoolbar',
    'waitress',
    'kitchen',
    'python-fedora',
    'bunch',
    'pyramid_mailer',
    'pyramid_beaker',
    'webhelpers',
    ]

setup(name='FedoraSummerOfHardware',
      version='0.0',
      description='FedoraSummerOfHardware',
      long_description=README + '\n\n',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      license='AGPLv3',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='fedorasummerofhardware',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = fedorasummerofhardware:main
      [console_scripts]
      initialize_FedoraSummerOfHardware_db = fedorasummerofhardware.scripts.initializedb:main
      """,
      )
