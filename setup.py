# -*- coding: utf-8 -*-
# @Time    : 5/25/23 3:13 PM
# @Author  : LIANYONGXING
# @FileName: setup.py

from setuptools import setup, find_packages

tianrannlp_packages = find_packages()

if 'test' in tianrannlp_packages:
    tianrannlp_packages.remove('test')

setup(
    name='tianrannlp',
    version='0.0.4',
    author='tianran',
    author_email='512796933@qq.com',
    url='https://github.com/lianyongxing/',
    description=u'文本处理',
    # install_requires=['flashtext', 'jieba-fast', 'tqdm'],
    packages=tianrannlp_packages,
    py_modules=list(),
    # package_dir={'': 'src'},  # 必填
    include_package_data=True
)

