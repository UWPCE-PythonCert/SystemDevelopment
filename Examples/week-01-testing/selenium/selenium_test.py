import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

try:
    url = "http://localhost:8000/week-01-unit-testing/slides/"
    driver.get(url)
    assert "Isilon" in driver.title

    body = driver.find_element_by_xpath('//body')
    for i in xrange(55):
        body.send_keys(Keys.ARROW_RIGHT)

    time.sleep(1)
    elem = driver.find_element_by_id("selenium")
    assert "Selenium" in elem.text
    assert "UnFoundText" not in elem.text
    assert "UnFoundText" in elem.text

finally:
    driver.close()
