from setuptools import setup

setup(name='qasi',
      version='0.1',
      description='A web app for when you need to Quickly Annotate Some Images.',
      url='https://github.com/joshualockhart/qasi',
      author='Flying Circus',
      author_email='joshualockhart@gmail.com',
      license='GPLv3',
      packages=['qasi'],
      install_requires=[
          'certifi',
          'click',
          'cycler',
          'Flask',
          'Flask-SQLAlchemy',
          'itsdangerous',
          'Jinja2',
          'MarkupSafe',
          'matplotlib',
          'numpy',
          'olefile',
          'Pillow',
          'pyparsing',
          'python-dateutil',
          'pytz',
          'six',
          'SQLAlchemy',
          'Werkzeug'
          ],
      zip_safe=False)
