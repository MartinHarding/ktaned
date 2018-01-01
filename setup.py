from setuptools import setup, find_packages

setup(
    name='ktaned',
    version='0.0.0',
    description='Diffuser library for Keep Talking and Nobody Explodes bombs',
    url='https://github.com/MartinHarding/ktaned/',
    author='Martin Harding, Julian Norton',
    license='MIT',
    author_email='martin@martinharding.com, julian@juliannorton.com',
    keywords='ktane game bomb diffuser',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'pathfinding',
        'PyYAML'
    ],
    python_requires='>=3.6',
    zip_safe=True,
    include_package_data=True,
    package_data={'': '*.yml'})
