# coding=utf-8
from setuptools import setup


setup(name='WopiValidatorExecutor',
      version='0.1.0',
      description="WopiValidator Executor",
      long_description="WopiValidatorExecutor is an automated tool that executes tests which verify the target host's WOPI implementation",
      install_requires=[
          'colorama==0.3.7',
          'configparser==3.5.0',
          'requests==2.20.0'
      ],
      packages=['WopiValidatorExecutor'],
      package_data={
          '': ['*.ini', '*.md', '*.txt']
      },
      include_package_data=True,
      data_files=[
          ('WopiValidatorExecutor', ['WopiValidatorExecutor/ExecutorConfig.ini']),
          ('', ['LICENSE.txt'])
      ],
      entry_points={
          'console_scripts': ['WopiValidatorExecutor = WopiValidatorExecutor.__main__:main']
      },
      license='MIT',
      url='https://wopi.readthedocs.io/en/latest/build_test_ship/validator.html',
      author="Microsoft Corporation",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Environment :: Console',
          'Topic :: Software Development :: Testing',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3'
      ])
