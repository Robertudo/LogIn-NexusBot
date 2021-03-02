from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as ac
import os

try:
	with open('data.txt', 'r') as fname:
		data = list()
		for line in fname:
			splitLine = line.split(":")
			data.append(splitLine)
		
		matricula = data[0][1].strip()
		password = data[1][1].strip()

		fname.close()

	# get PATH
	path = os.getcwd() + "\driver\chromedriver.exe"

	driver = webdriver.Chrome(path)

	driver.get("https://www.uanl.mx/enlinea/")

	driver.switch_to.frame('loginbox')

	driver.find_element_by_xpath('//*[@id="cuenta"]').send_keys(matricula)

	driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)

	logIn = driver.find_element_by_xpath("/html/body/div/form/fieldset/div[4]/button")
	logIn.click()

	selectNexus = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/table/tbody/tr[3]/td/a/img')
	enterNexus = driver.find_element_by_xpath('//*[@id="linkNexus"]')

	actions = ac(driver)
	actions.move_to_element(selectNexus).move_to_element(enterNexus).click().perform()

except Exception as e:
	print('Agregar de manera correcta su matricula y contraseña al archivo "data.txt"')