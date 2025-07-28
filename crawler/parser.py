import json
import os

def parse_leaks(keyword):
    leaks = {
        "emails": [],
        "passwords": []
    }

    # Load from your fake_leaks.json
    with open('dumps/fake_leaks.json', 'r') as f:
        data = json.load(f)
        for entry in data:
            if entry.get('email') == keyword or entry.get('phone') == keyword:
                leaks["emails"].append(entry.get('email', entry.get('phone')))
                leaks["passwords"].append(f"Leaked on {entry['leaked_platform']} ({entry['date']})")

    return leaks
