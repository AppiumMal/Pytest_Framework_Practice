import config 
from selenium import webdriver

# Driver factory owns the driver creation from the values of config browser

class DriverFactory:
    def __init__(self,config):
        self.config = config
        
    def get_browser(self):
        return self.config["browser"]
    
    def create_driver(self):
        if (self.config["browser"] == "Chrome"): 
           return webdriver.chrome()   
        elif (self.config["browser"] == "FireFox"):
            return webdriver.firefox()
  
factory = DriverFactory(config)    
        
