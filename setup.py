import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'arrow',
    'bcrypt',
    'docutils',
    'gunicorn',
    'marshmallow',
    'passlib',
    'plaster_pastedeploy',
    'psycopg2',
    'pyramid >= 1.9',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_jwt',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'sqlalchemy_utils',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'click'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='apflow',
    version='0.0',
    description='Accounts Payable Workflow',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = apflow:main',
        ],
        'console_scripts': [
            'apflow = apflow.scripts.cli:main',
        ],
    },
)
