#FirstDjango_28102024

##Инструкция по развертыванию проекта
1. 'python3 -m venv django_venv'
2. 'source django_venv/bin/activate'
3. 'pip install -r requirements.txt'
4. 'python manage.py migrate'
5. 'python manage.py runserver'

##запуск ipython в контексте приложений django:
'''
python manage.py shell_plus --ipython
'''

##Дополнительно для шаблонов:
1. Полезное дополнение для шаблонов 'Django' (в VSCode - Django Baptiste Darthenay)
'''
ext install batisteo.vscode-django
'''
Добавить в 'settings.json'
'''
"emmet.includeLanguages": {
    "django-html": "html",
},
"files.associations": {
    "*.html": "django-html"
}
'''