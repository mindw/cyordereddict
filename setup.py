import os.path
import sys
from setuptools import setup, Extension

if sys.version_info[0] == 2:
    base_dir = 'python2'
elif sys.version_info[0] == 3:
    base_dir = 'python3'

tests_require = ['nose']
if sys.version_info < (3,):
    tests_require.append('unittest2')
    
source = os.path.join(base_dir, 'cyordereddict', '_cyordereddict.pyx')
ext_modules = [Extension('cyordereddict._cyordereddict', [source])]

if __name__ == '__main__':
    setup(
        name='cyordereddict',
        description="Cython implementation of Python's collections.OrderedDict",
        long_description=(open('README.rst').read()
                          if os.path.exists('README.rst')
                          else ''),
        use_scm_version={
            'version_scheme': 'guess-next-dev',
            'local_scheme': 'dirty-tag',
            'write_to': os.path.join(
                base_dir, 
                'cyordereddict', 
                '_version.py'
            )
        },
        setup_requires=[
            'setuptools>=18.0',
            'setuptools-scm>1.5.4'
            'nose'
        ],
        tests_require=tests_require,
        license='MIT',
        url='https://github.com/shoyer/cyordereddict',
        author='Stephan Hoyer',
        author_email='shoyer@gmail.com',
        packages=['cyordereddict',
                  'cyordereddict.benchmark',
                  'cyordereddict.test'],
        package_dir={'': base_dir},
        ext_modules=ext_modules,
        classifiers = [
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Cython',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Scientific/Engineering',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Utilities',
        ],
    )
