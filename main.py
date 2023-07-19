#  from webdriver_manager.chrome import ChromeDriverManager
#  from selenium import webdriver

# code from https://www.geeksforgeeks.org/python-script-to-open-a-web-browser/
# first import the module
import webbrowser
# then make a url variable
url = "https://magento.Softwaretestingboard.Com"
# then call the default open method described above
webbrowser.open(url)

'''
# my code worked but closes immediately 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
executable_path = ChromeDriverManager().install()
driver = webdriver.Chrome()
driver.get("http://www.google.com/")
print(driver.title)
'''
# code from ppt
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("https://www.google.com/")
'''
