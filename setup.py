from setuptools import setup, find_packages

setup( name='infrastruction',
    version = '0.0.1',
    description = 'Infrastructure bootstrapping for Modern Django applications',
    author = 'Daryl Antony',
    author_email = 'daryl@commoncode.com.au',
    url = 'https://github.com/commoncode/infrastruction',
    keywords = ['django',],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'Django>=1.4',
        'ipdb',
        'django-extenstions',
        'django-devserver',
        'django-debugtoolbar',
    ]
)