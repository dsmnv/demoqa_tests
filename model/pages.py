from selene.support.shared import browser
from selene import have
import os.path


def open_form():
    browser.open_url('https://demoqa.com/automation-practice-form')


def set_firstname(firstname):
    browser.element('#firstName').type(firstname)


def set_lastname(lastname):
    browser.element('#lastName').type(lastname)


def set_email(email):
    browser.element('#userEmail').type(email)


def set_gender(gender):
    browser.all('[for^=gender-radio]').by(
        have.exact_text(gender)
    ).first.click()


def set_phone_number(number):
    browser.element('#userNumber').type(number)


def set_date_of_birth(month, year):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(month)
    browser.element('.react-datepicker__year-select').type(year)
    browser.element('[aria-label="Choose Sunday, November 5th, 1995"]').click()


def set_subjects(subject1, subject2):
    browser.element('#subjectsInput').type(subject1).press_enter().type(subject2).press_enter()


def set_hobbies():
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()


def upload_picture():
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/donut.png'))


def set_current_address(address):
    browser.element('#currentAddress').type(address)


def set_state():
    browser.element('#react-select-3-input').type('ncr').press_enter()


def set_city():
    browser.element('#react-select-4-input').type('gurgaon').press_enter()


def submit_form():
    browser.element('#submit').click()






























































