from setuptools import setup, find_packages


setup(name='rocket-python',
      version='1.2.3',
      description="RocketChat API with Python",
      long_description=open("README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Utilities",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='rocketchat',
      author='Derek Stegelman',
      url='http://github.com/dstegelman/rocket-python',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests>=2.0.0,<3.0'
      ]
    )
