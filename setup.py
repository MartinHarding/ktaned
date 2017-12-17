from setuptools import setup

setup(
    name='ktaned',
    version='1.0a1',
    description='Solver for Keep Talking and Nobody Explodes bombs',
    url='https://github.com/MartinHarding/ktaned/',
    author='Martin Harding',
    license='MIT',
    author_email='martin@martinharding.com',
    keywords='KTANE, keep talking and nobody explodes'
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: KTANE Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['ktaned'],
    install_requires=[
        'random',
        'inflect',
        'pathfinding',
        'PyYAML'
    ],
    python_requires='>=3.6',
    zip_safe=True,
    include_package_data=True,
    package_data={'': '*.yml'})
