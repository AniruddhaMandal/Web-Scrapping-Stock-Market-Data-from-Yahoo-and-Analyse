from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import Name

browser = webdriver.Chrome("chromedriver.exe")
main_dataset = []
try:
	for n,share_company in enumerate(Name.list):
		link = 'https://in.finance.yahoo.com/quote/'+share_company+'/history?p='+share_company
		browser.get(link)


		time.sleep(10)
		date = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/span')

		date.click()

		fiveyear = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[1]/div[1]/div/div/div/div/div/ul[2]/li[3]/button')
		fiveyear.click()

		download = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[1]/div[2]/span[2]/a')

		link = download.get_attribute('href')

		data = pd.read_csv(link)

		j = share_company.split('.')[0]
		data[j] = data.iloc[:,1:5].mean(axis = 1)
		
		main_dataset.append(data)

finally:
	browser.close()

temp = main_dataset[0]
temp = temp.iloc[:,[0,7]]


for i in main_dataset[1:]:
	data = i.iloc[:,[0,7]]
	temp = pd.merge(temp,data,on = 'Date')

print(temp)
temp.to_csv("Dataset.csv") 
	
	