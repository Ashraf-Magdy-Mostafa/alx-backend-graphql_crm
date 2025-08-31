# crm/cron.py
import datetime


def log_crm_heartbeat():
    """
    Logs: DD/MM/YYYY-HH:MM:SS CRM is alive
    Also tries to ping the GraphQL hello field (optional).
    """
    now_str = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    line = f"{now_str} CRM is alive\n"
    with open("/tmp/crm_heartbeat_log.txt", "a", encoding="utf-8") as f:
        f.write(line)

    # Optional GraphQL ping
    try:
        import requests
        r = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5,
        )
        # Not strictly used, but you could check r.json() here
        _ = r.status_code
    except Exception:
        # Keep heartbeat tolerant: never crash on network hiccups
        pass
