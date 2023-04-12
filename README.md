# GitHub Codespaces ♥️ Django

https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/ —> steps to deploy:

cd ~/.ssh
ssh-keygen -t ed25519 -C "your@mail.com"
ls
cat .pup —> Github Settings SSH

git clone git@github.com:user/reponame.git
mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv
pip install django (oder pip install -r requirements.txt)

(pip freeze oder pip list / lsvirtualenv -b / workon mysite-virtualenv / ‚python -m site‘ listet den Pfad der Pakete - wichtig für static files: e.g. /home/djangoerni/.virtualenvs/dangotest-virtualenv/lib/python3.10/site-packages/)

Create a Web app with Manual Config
Enter your virtualenv name
Edit your WSGI file (the one on phythonanywhere web app, not the local one)
./manage.py migrate

in settings.py: ALLOWED_HOSTS = ['djangoerni.pythonanywhere.com']
—> reload webapp

serving static files: https://help.pythonanywhere.com/pages/DjangoStaticFiles:
STATIC_ROOT = os.path.join(BASE_DIR, "static") in settings.py
(python manage.py collectstatic) - nur bei Inizialisiurng für die css styles des admin Bereichs

setting environment variables: https://help.pythonanywhere.com/pages/environment-variables-for-web-apps
(siehe andierni.pythonanywhere.com)

******************************************************************************************************

für updates: git pull (in bash console - im virtualenv)

To run this application:

```python
python manage.py runserver
```
