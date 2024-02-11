from time import sleep

def check_title(browser, title):
    sleep(2)
    html = browser.execute_script("return arguments[0].outerHTML;", title)
    if "Камчатский край" in html:
        return True
    return False