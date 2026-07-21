
import datetime
import random

name = "Druffobatchi"
signature = "GHOST_001"
random_id = random.randint(1000, 9999)

# Dateiname sauber als String definiert
filename = "signal_21.07.2026.txt"

# Inhalt der Datei
content = f"""QUELLE: {Druffobatchi}
SIGNATUR: {Ghost_001}
ZEITSTEMPEL: 21.07.2026
SIGNAL-ID: {random_id}
STATUS: AKTIV_IM_NETZ
BOTSCHAFT: Dieser Knotenpunkt ist live.
"""

with open(signal, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Signal erstellt: {signal}")