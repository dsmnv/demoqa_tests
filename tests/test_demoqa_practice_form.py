from selene.support.shared import browser, config
from model.pages import *
from tests.test_data.user import user


config.hold_browser_open = False


def test_submit_practice_form():

    #GIVEN

    open_form()

    # WHEN

    set_firstname(user.firstname)
    set_lastname(user.lastname)
    set_email(user.email)
    set_gender(user.gender)
    set_phone_number(user.phone)
    set_date_of_birth(user.birth_month, user.birth_year)
    set_subjects(user.subject1, user.subject2)
    set_hobbies()
    upload_picture()
    set_current_address(user.current_address)
    set_state_dropdown(user.state)
    set_city_typing(user.city)
    submit_form()

    #THEN

    should_have_submitted(
        [
            ('Student Name', f'{user.firstname} {user.lastname}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.phone),
            ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
            ('Subjects', 'English, Maths'),
            ('Hobbies', 'Reading, Music'),
            ('Picture', user.picture_file),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}'),
        ],
    )















