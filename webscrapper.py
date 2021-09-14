'''
Python code to scrap Web based on url and column name -> create a dataframe -> create a csv 
credits : https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def web_scrapper():
    driver = webdriver.Chrome('C:/Users/Admin/OneDrive/Documents/chromedriver')
    driver.get('https://hoopshype.com/salaries/players/')
    players = driver.find_elements_by_xpath('//td[@class="name"]')
    salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]')
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)

    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
       
    driver.close()
    return salaries_list,players_list


salaries_list,players_list = web_scrapper()

players_salaries = list(zip(players_list,salaries_list))
player_data = pd.DataFrame(players_salaries,columns=['Player','Salary'])
print(player_data)
player_data.to_csv('Player_salary_data.csv')
