 # djangorestframework-API #
https://d9-drf-api.herokuapp.com/

download/git clone

python -m venv

env\Scripts\activate.bat

pip install -r requirements.txt

cd blog

python manage.py runserver

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin/

пользователь-администратор:

логин: pws_admin

пароль: sf_password

пользователь:

логин: guest

пароль: skillfaktory

API: /categories/

Allow: GET, POST, HEAD, OPTIONS

API: /categories/<cat_id>

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

API: /<post_id>

Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

API: /authors/

API: /authors/<author_id>

Allow: GET, HEAD, OPTIONS

