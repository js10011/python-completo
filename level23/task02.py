import json
from datetime import datetime

def iso_to_datetime(iso_str):
    return datetime.fromisoformat(iso_str)

def custom_decoder(dct):
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = iso_to_datetime(value)
            except ValueError:
                pass
    return dct

json_str = '{"name": "John", "birthdate": "1990-01-01T12:00:00"}'
result = json.loads(json_str, object_hook=custom_decoder)
print(result)