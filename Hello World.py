from splinter import Browser

username = 'DN5127'
password = 'Howareyou1'
browser = Browser()
browser.visit('https://kite.zerodha.com/')
#with Browser() as browser:
# Visit URL
#url = "https://kite.zerodha.com"
	
#user_id = raw_input("DN5127")
#user_pass = raw_input("Howareyou1")
#browser.fill('q','DN5127')
#time.sleep(1)
#browser.fill('Howareyou1')
#time.sleep(2)
browser.find_by_id('action').fill(username)
