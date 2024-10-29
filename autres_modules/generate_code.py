import datetime
import random
import string

# =================================================================================
# FONCTION POUR GENERER LE CODE ALEATOIRE AVEC DATE,
# =================================================================================

def generate_code():
    current_datetime = datetime.datetime.now()
    date_part = current_datetime.strftime("%Y-%m-%d")
    time_part = current_datetime.strftime("%H%M%S")
    random_part = ''.join(random.choices(string.digits, k=2))
    code = f"MB-{date_part}-{time_part}-{random_part}"
    return code

# =================================================================================
# FONCTION POUR GENERER LE CODE ALEATOIRE AVEC ASCII
# =================================================================================
used_codes = set()

def generate_code_ascii():
    while True:
        code = ''.join(random.choices(string.digits, k=6))
        if code not in used_codes:
            used_codes.add(code)
            return code