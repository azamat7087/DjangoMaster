cd $1 || exit
python -m pip install -U pip
python -m pip install -U pip setuptools
python -m pip install django
django-admin startproject $2