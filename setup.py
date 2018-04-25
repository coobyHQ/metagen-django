from setuptools import setup, find_packages

setup(
    name='django-metagen',
    packages=find_packages(exclude='example'),
    include_package_data=True,
    zip_safe=False,
    version='0.0.2',
    description='Metagen authentication app for django',
    author='Gridworkz',
    author_email='dave@gridworkz.com',
    url='https://github.com/gridworkz/metagen-django',
    keywords=['django', 'authentication', 'metagen', 'gridworkz'],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
)
