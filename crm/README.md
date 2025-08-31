# Celery + Celery Beat for Weekly CRM Report

## 1) Install Redis and deps
- Ubuntu: `sudo apt-get update && sudo apt-get install -y redis-server`
- Start Redis: `sudo systemctl enable --now redis-server`
- Python deps: `pip install -r requirements.txt`

## 2) Django setup
- Run migrations: `python manage.py migrate`
- (Optional) Run the dev server so GraphQL is reachable:
  - `python manage.py runserver` (keeps `http://localhost:8000/graphql` alive)

## 3) Start Celery
Open two terminals:

**Terminal A (worker):**
```bash
celery -A crm worker -l info
