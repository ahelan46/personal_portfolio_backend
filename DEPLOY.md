Quick deployment notes

Heroku (or similar PaaS)

- Ensure `requirements.txt` includes `gunicorn` and `whitenoise` (already present).
- Set config vars:
  - `DJANGO_SETTINGS_MODULE=mysite.settings_prod`
  - `DJANGO_SECRET_KEY` (strong secret)
  - `DJANGO_DEBUG=False`
  - `DJANGO_ALLOWED_HOSTS=yourdomain.com` (comma-separated)
- Push repo, then run:

```bash
heroku run python manage.py migrate
heroku run python manage.py collectstatic --noinput
heroku ps:scale web=1
```

VPS (Ubuntu) — Gunicorn + systemd + Nginx

- On server:

```bash
sudo apt update && sudo apt install python3-pip python3-venv nginx
cd /srv/myproject
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export DJANGO_SETTINGS_MODULE=mysite.settings_prod
export DJANGO_SECRET_KEY='(set securely)'
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS=example.com
python manage.py migrate
python manage.py collectstatic --noinput
```

- systemd service example (`/etc/systemd/system/myproject.service`):

```ini
[Unit]
Description=gunicorn daemon for mysite
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/srv/myproject
Environment="DJANGO_SETTINGS_MODULE=mysite.settings_prod"
Environment="PATH=/srv/myproject/venv/bin"
ExecStart=/srv/myproject/venv/bin/gunicorn mysite.wsgi:application --bind unix:/run/myproject.sock

[Install]
WantedBy=multi-user.target
```

- Nginx site snippet (proxy to socket):

```nginx
server {
    listen 80;
    server_name example.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /srv/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/myproject.sock;
    }
}
```

Notes
- Use `collectstatic` after code changes affecting static assets.
- Keep `SECRET_KEY` out of source; use environment variables or a secrets manager.
- Consider moving from SQLite to Postgres for production.
