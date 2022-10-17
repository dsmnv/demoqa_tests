from selene.support.shared import browser


def select_gender_male():
    select_gender = browser.element('#gender-radio-1').double_click()
    select_gender.double_click()
