#!/bin/bash


tianrannlp_version=`cat setup.py | grep  -o "\d\.\d\.\d"`

echo "tianrannlp version: ${tianrannlp_version}"

python3 setup.py bdist_wheel --universal

ls -lth ./dist/ | grep ${tianrannlp_version}
pip install twine
twine upload ./dist/tianrannlp-${tianrannlp_version}-py2.py3-none-any.whl

echo "finished!"
exit 0