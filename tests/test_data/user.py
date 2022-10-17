from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physic'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class user:
    gender: Gender
    name: str = 'Dmitry'
    last_name: str = 'Sem'
    email: str = 'demotest@tete.com'
    mobile: str = '9570000000'
    birth_day: str = '5'
    birth_month: str = 'November'
    birth_year: str = '1995'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths, )
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    current_address: str = 'Saint - P'
    picture_file: str = 'donut.png'
    state: str = 'Haryana'
    city: str = 'Karnal'