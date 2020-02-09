from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('S M Vaidhyanathan')


searchbtn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbtn.click()


driver.get('https://github.com')

searchbox = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
searchbox.send_keys('smv1999')

searchbtn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]')
searchbtn.send_keys(u'\ue007')