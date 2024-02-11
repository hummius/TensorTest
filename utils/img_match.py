import re


class MatchFalseException(Exception):
    pass


def img_matching(browser, block):
    html = browser.execute_script("return arguments[0].outerHTML;", block)
    width = re.findall(r'width="(\d{1,5})"', html)
    height = re.findall(r'height="(\d{1,5})"', html)
    print(width, height)

    for num in width:
        for num_2 in width:
            if num != num_2:
                raise MatchFalseException("Photos on the page https://tensor.ru/about "
                                          "in the 'Работаем' block of different sizes")
    for num in height:
        for num_2 in height:
            if num != num_2:
                raise MatchFalseException("Photos on the page https://tensor.ru/about "
                                          "in the 'Работаем' block of different sizes")

    return True
