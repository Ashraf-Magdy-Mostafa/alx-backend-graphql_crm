# CRM Weekly Report — Quick Setup & Run (Celery + Beat)

1. **Install Redis & Python dependencies**
   ```bash
   # Ubuntu/Debian
   sudo apt-get update && sudo apt-get install -y redis-server
   sudo systemctl enable --now redis-server

   # From your project root (where requirements.txt lives)
   pip install -r requirements.txt
   ```

2. **Run Django migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start the Celery worker**
   ```bash
   celery -A crm worker -l info
   ```

4. **Start Celery Beat (scheduler)**
   ```bash
   celery -A crm beat -l info
   ```

5. **Verify the report logs**
   ```bash
   tail -n 50 /tmp/crm_report_log.txt
   ```
