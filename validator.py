# Example custom module to be imported

import re

def validate_email(email):
    if(len(email) > 7):
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(regex, email))
    return False