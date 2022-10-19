from dataclasses import dataclass
from typing import Tuple


@dataclass
class user:
    gender: str = 'Male'
    firstname: str = 'Dmitry'
    lastname: str = 'Sem'
    email: str = 'demotest@tete.com'
    phone: str = '9570000000'
    birth_day: str = '05'
    birth_month: str = 'November'
    birth_year: str = '1995'
    subject1: str = 'English'
    subject2: str = 'Maths'
    current_address: str = 'Saint - P'
    picture_file: str = 'donut.png'
    state: str = 'Haryana'
    city: str = 'Karnal'
