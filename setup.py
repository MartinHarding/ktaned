from setuptools import setup

setup(name='ktaned',
      description='Solve Keep Talking and Nobody Explodes bombs',
      license='MIT',
      author='Martin Harding',
      author_email='martin@martinharding.com',
      packages=['ktaned'],
      install_requires=[
        'pathfinding',
        'PyYAML'
      ],
      zip_safe=True,
      include_package_data=True,
      package_data={'': '*.yml'})
