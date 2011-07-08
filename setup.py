from setuptools import setup, find_packages

setup(
    name='django-mongoviews',
    version='0.1',
    description='A Django-ClassViews for mongoengine',
    author='Wilson JR',
    author_email='wilsonpjunior@gmail.com',
    url='http://github.com/wpjunior/django-mongoviews/',
    packages=find_packages(exclude=['examples', 'examples.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
