from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Robert\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe')
browser.get('http://127.0.0.1:8000')

assert 'http://127.0.0.1:8000' in browser.title

