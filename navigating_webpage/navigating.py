from selenium import webdriver
import os 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class Navigating(webdriver.Chrome): 
      
      def __init__(self, driver_path = r";C:\SeleniumDriver", teardown = False): 
          self.driver_path = driver_path  
          self.teardown = teardown
          os.environ['PATH']+=self.driver_path
          super(Navigating, self).__init__()   
          
      def __exit__(self, exc_type, exc, traceback): 
          if self.teardown:
            self.quit()
          
      def landing_page(self):
          self.get('https://store.nba.com/')   
          self.maximize_window()
          WebDriverWait(self, 5) 
          
      def choose_team(self, teamName):  
          WebDriverWait(self, 10).until(EC.invisibility_of_element((By.XPATH, "//div[@class='modal-backdrop']")))
          team_element = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[@title='{teamName} Team Shop']"))).click() 
     
      def choose_category(self, category = None): 
          WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@class = 'responsive-image']/img[@alt = '{category}']"))).click()  
          
      def select_jersey(self): 
          WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Jerseys"))).click()  
          
     
         
      
     
