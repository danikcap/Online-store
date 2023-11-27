from selenium.webdriver.common.by import By


def test_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "No button"
