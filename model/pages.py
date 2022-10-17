from selene.support.shared import browser
from selene import have


def open_form():
    browser.open_url('https://demoqa.com/automation-practice-form')


def set_firstname(firstname):
    browser.element('#firstName').type(firstname)


def set_lastname(lastname):
    browser.element('#firstName').type(lastname)


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


def set_subjects(subjects):
    browser.element('#subjectsInput').type(subjects).press_enter().type(subjects).press_enter()
