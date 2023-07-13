from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

'''
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
'''

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("https://www.google.com/")
