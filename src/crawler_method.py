from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locator_config import *

class webDriverHelper:
        
    '''
    # Example usage:
    if __name__ == "__main__":
        # Configure options (e.g., headless mode if needed)
        options = Options()
        # options.add_argument("--headless")  # Uncomment if you want headless mode

        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)
        driver.get("https://example.com")  # Replace with your target URL

        # Initialize helper class with driver
        helper = WebDriverHelper(driver)
    '''

    def __init__(self, driver, wait_time = 20):
        self.driver = driver
        self.wait_time = wait_time

    def waitForElementUntilClickableAndClick(self, element_xpath):
        try:
            WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable((By.XPATH, element_xpath))).click()
        except:
            print("Element seems not found for {0}".format(element_xpath))

    def waitForElementVisibilityAndGetText(self, element_xpath, element_name=None):
        try:
            element = WebDriverWait(self.driver, self.wait_time).until(
                   EC.visibility_of_element_located((By.XPATH, element_xpath))
            )
            text = element.text

            if element_name:
                print(f"Retrieved text for '{element_name}': {text}")
            return text
        
        except Exception as e:
            print(f"Error retrieving text for '{element_name}' ")
            return "None"
        
    def waitForElementVisibility(self, element_xpath, element_name=None):
        attempts = 0
        max_attempts = 6  # You can set this to whatever number you prefer

        while attempts < max_attempts:
            try:
                WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
                return f'Element visible, name = {element_name}'  # Element is visible
            
            except Exception as e:
                print(f"Attempt {attempts + 1}: Element with xpath '{element_xpath}' is not visible. Refreshing and Retrying...")
                time.sleep(1)  # Wait before retrying
                self.driver.refresh()
                attempts += 1

        print(f"Element with xpath '{element_xpath}' did not become visible after {max_attempts} attempts.")
        return False  # Element is not visible after max attempts

    
    def waitForElementVisibilityAndGetLength(self, element_xpath):
        try:
            element = self.driver.find_elements(By.XPATH, element_xpath)
            count = len(element)
            return count
        except Exception as e:
            return "None"
    
    def scrollIntoView(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scrollIntoBottom(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    

class dataHelper:

    def __init__(self) -> None:
        pass

    def getNameFromFile(self, file_name):
        with open(file_name, "r") as file:
            name_text = file.read().strip()

        name_array = [name.strip() for name in name_text.split(",")]

        return name_array
    
    def writeNameToFile(self, file_name, text):
        with open(file_name, "w") as file:
            file.write("{0},".format(text))

    def appendNameToFile(self, file_name, text):
        with open(file_name, "a") as file:  # change "w" to "a" for appending
            file.write("{0},".format(text))  # append text to the file
            file.close()
        print('Saved to csv')


    def saveToXlsx(self, list):
        df = pd.DataFrame(list)
        output_file = 'vessel_data.xlsx'  # Specify your desired filename
        df.to_excel(output_file, index=False, engine='openpyxl')  # Save without the index column

    def appendToXlsx(self, file_name, new_data_list):
        df = pd.read_excel(file_name)   #read old excel
        new_row_df = pd.DataFrame(new_data_list)    #convert new list to df
        df = pd.concat([df, new_row_df], ignore_index=True) #concat to old df
        df.to_excel(file_name, index=False) #save the new concattede xlsx
        print('Saved to excel')

    def get_vessel_details(self, helper, count):
        """Retrieve detailed vessel information."""
        return {
            "Flag": helper.waitForElementVisibilityAndGetText(LocatorConfig.FLAG['xpath'], LocatorConfig.FLAG['name']).split(":")[-1].strip(),
            "Launch Date": helper.waitForElementVisibilityAndGetText(LocatorConfig.LAUNCH_DATE['xpath'], LocatorConfig.LAUNCH_DATE['name']),
            "Design Deadweight": helper.waitForElementVisibilityAndGetText(LocatorConfig.DESIGN_DWT['xpath'], LocatorConfig.DESIGN_DWT['name']),
            "Gross Tonnage": helper.waitForElementVisibilityAndGetText(LocatorConfig.GROSS_TONNAGE['xpath'], LocatorConfig.GROSS_TONNAGE['name']),
            "Displacement (tonnes)": helper.waitForElementVisibilityAndGetText(LocatorConfig.DISPLACEMENT['xpath'], LocatorConfig.DISPLACEMENT['name']),
            "Design Speed Ahead": helper.waitForElementVisibilityAndGetText(LocatorConfig.DESIGN_SPEED['xpath'], LocatorConfig.DESIGN_SPEED['name']),
            "Length Overall (LOA)": helper.waitForElementVisibilityAndGetText(LocatorConfig.LOA['xpath'], LocatorConfig.LOA['name']),
            "Calculated Freeboard (mm)": helper.waitForElementVisibilityAndGetText(LocatorConfig.FREEBOARD['xpath'], LocatorConfig.FREEBOARD['name']),
            "Breadth Overall": helper.waitForElementVisibilityAndGetText(LocatorConfig.BREADTH['xpath'], LocatorConfig.BREADTH['name']),
            "Depth Overall": helper.waitForElementVisibilityAndGetText(LocatorConfig.HEIGHT['xpath'], LocatorConfig.HEIGHT['name']),
            "Length Between Perpendicular (LPP)": helper.waitForElementVisibilityAndGetText(LocatorConfig.LPP['xpath'], LocatorConfig.LPP['name']),
            "Design Draft": helper.waitForElementVisibilityAndGetText(LocatorConfig.DRAFT_DESIGN['xpath'], LocatorConfig.DRAFT_DESIGN['name']),
            "Draft Molded": helper.waitForElementVisibilityAndGetText(LocatorConfig.DRAFT_MOLDED['xpath'], LocatorConfig.DRAFT_MOLDED['name']),
            "Draft Scantling": helper.waitForElementVisibilityAndGetText(LocatorConfig.DRAFT_SCANTLING['xpath'], LocatorConfig.DRAFT_SCANTLING['name']),
        }

    def get_engine_details(self, helper):
        """Retrieve engine-related information."""
        return {
            "Generator Number": helper.waitForElementVisibilityAndGetLength(LocatorConfig.NUMBER_GENERATOR['xpath']),
            "Auxiliary Engine Rated Power": helper.waitForElementVisibilityAndGetText(LocatorConfig.AE_RATED_POWER['xpath'], LocatorConfig.AE_RATED_POWER['name']).split(':')[-1].strip().split()[0],
            "Auxiliary Engine Manufacturer": helper.waitForElementVisibilityAndGetText(LocatorConfig.AE_MANUFACTURER['xpath'], LocatorConfig.AE_MANUFACTURER['name']).split(':')[-1].strip(),
            "Main Engine Manufacturer": helper.waitForElementVisibilityAndGetText(LocatorConfig.ME_MANUFACTURER['xpath'], LocatorConfig.ME_MANUFACTURER['name']).split(':')[-1].strip(),
            "Main Engine Rated Power": helper.waitForElementVisibilityAndGetText(LocatorConfig.ME_RATED_POWER['xpath'], LocatorConfig.ME_RATED_POWER['name']).split(':')[-1].strip().split()[0]
        }
    
class setupDriver:
    def __init__(self, headless, chrome_driver_version=None) -> None:
        self.headless = headless
        self.chrome_driver_version = chrome_driver_version
        
    def setup(self):
        """Sets up the WebDriver with the required options."""
        # chrome_driver_version = '130.0.6723.92'  # Specify desired version here
        # service = Service(ChromeDriverManager().install())
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        if self.headless == True:
            chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver