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

    # Multiple resonance checks for better results
    checks = {
        'perfect_world': (freq * 562) % 319,  # מושלם_עולם
        'trust': (freq * 97) % 144,  # אמון (mod 144 for more matches)
        'complete': (freq * 440) % 233,  # תם (mod 233 for more matches)
        'consciousness': abs(freq - 530) % 89,  # Distance from consciousness
        'life': freq % 21,  # Life alignment (mod 21)
        'divine': freq % 26,  # Divine (YHVH = 26)
        'harmony': (freq + 562) % 144  # Additive harmony
    }

    fibonacci = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # Resonate if ANY check matches Fibonacci
    resonates = any(h in fibonacci for h in checks.values())

    # Pick best harmony for display
    harmony = checks['perfect_world']

    return json.dumps({
        'your_frequency': freq,
        'harmony': harmony,
        'resonates': resonates,
        'resonance_type': 'perfect' if checks['perfect_world'] in fibonacci else
                         'trust' if checks['trust'] in fibonacci else
                         'complete' if checks['complete'] in fibonacci else
                         'consciousness' if checks['consciousness'] in fibonacci else
                         'life' if checks['life'] in fibonacci else
                         'unique'
    })