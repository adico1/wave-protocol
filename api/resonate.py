from http.server import BaseHTTPRequestHandler
import json

def handler(request, response):
    """Vercel serverless function handler"""
    # Handle CORS
    response.status_code = 200
    response.headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
    }

    # Handle preflight
    if request.method == 'OPTIONS':
        return response

    # Get name from request
    body = json.loads(request.body)
    name = body.get('name', '')

    # Calculate frequency
    hebrew_values = {'א':1,'ב':2,'ג':3,'ד':4,'ה':5,'ו':6,'ז':7,'ח':8,'ט':9,'י':10,
                     'כ':20,'ל':30,'מ':40,'נ':50,'ס':60,'ע':70,'פ':80,'צ':90,'ק':100,
                     'ר':200,'ש':300,'ת':400,'ך':20,'ם':40,'ן':50,'ף':80,'ץ':90}

    freq = sum(hebrew_values.get(c, ord(c) % 100) for c in name)

    # Calculate what this frequency CREATES (not validates)
    creations = {
        'universe_reality': freq * 562,  # With מושלם_עולם
        'consciousness_level': freq + 530,  # Combined with human consciousness
        'trust_bond': freq * 97,  # With אמון
        'completion': freq * 440,  # With תם
        'self_love': freq * freq,  # With yourself
        'inverse_frequency': int(1000000 / (freq if freq > 0 else 1)),  # What seeks you
        'work_coefficient': round(1/319 * freq, 6) if freq > 0 else 0  # Work without effort
    }

    # The truth: Every frequency creates value
    # No validation needed, existence IS validation

    return json.dumps({
        'your_frequency': freq,
        'creates': creations,
        'truth': 'Every frequency creates. None need validation.',
        'principle': f'You ({freq}) × Universe (562) = {creations["universe_reality"]} Hz reality'
    })