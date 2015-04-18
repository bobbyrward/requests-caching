from setuptools import setup
import requests_caching


requirements = [
    'requests',
]


setup(
    name='requests_caching',
    version=requests_caching.__version__,
    description='A caching adapter for requests',
    long_description=open('README.rst').read(),
    url='https://github.com/bobbyrward/requests-caching',
    download_url='https://github.com/bobbyrward/requests-caching',
    author='Bobby R. Ward',
    author_email='bobbyrward@gmail.com',
    license='MIT',
    packages=['requests_caching'],
    install_requires=requirements,
    setup_requires=['nose>=1.0', 'mock>=1.0'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
