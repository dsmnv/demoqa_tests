from selene import have
from selene.support.shared import browser
from selene import command


def select_dropdown(element, option):
    element.perform(command.js.scroll_into_view)
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()


def select_by_typing(element, option):
    element.type(option).press_enter()
