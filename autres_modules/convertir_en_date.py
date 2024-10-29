

from datetime import date
from dateutil.parser import parse

def convertir_en_date(date_:str):
    return parse(date_)
