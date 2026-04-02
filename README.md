### 1. Клонирование и установка
```bash
git clone https://github.com/t84625hsx9-del/homework-.git
cd homework-
```

### 2. Установить зависимости:
```bash
pip install -r requirements.txt
```

### 3. Запустить тесты (обязательно перед Push):
```bash
python manage.py test
```
### 4. Запустить сервер:
```bash
python manage.py runserver
```

### 5. Бонус
```bash
python3 -m coverage report
Name                               Stmts   Miss  Cover
------------------------------------------------------
core/__init__.py                       0      0   100%
core/settings.py                      21      0   100%
core/urls.py                           3      0   100%
manage.py                             11      2    82%
users/__init__.py                      0      0   100%
users/admin.py                         1      0   100%
users/apps.py                          4      0   100%
users/forms.py                        22      6    73%
users/migrations/0001_initial.py       8      0   100%
users/migrations/__init__.py           0      0   100%
users/models.py                        8      0   100%
users/tests.py                         5      0   100%
users/urls.py                          4      0   100%
users/views.py                        20      1    95%
------------------------------------------------------
TOTAL                                107      9    92%
```

