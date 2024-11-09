from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from crawler_method import webDriverHelper, dataHelper, setupDriver
from locator_config import LocatorConfig
import time
import math

def process_vessel_data(helper, count, vessel_name_list, target_data, ship_type):
    
    total_pages_to_scroll = math.ceil(len(vessel_name_list) / 20) + 2   # every page scrolled will load 20 ships
    total_target_data = count + target_data

    while count < total_target_data:
        print(f"Total Vessel collected = {count - 1}, search for vessel number {count}")
        """Processes each vessel's data on the website."""
        
        # Start interacting with the site
        print('Start interacting with the site, navigate to ABS search')
        driver.get("https://absrecord.eagle.org/#/absrecord/search")
        helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_DROPDOWN_SHIP_TYPE['xpath'])
        helper.waitForElementUntilClickableAndClick(LocatorConfig.OPT_SHIP_TYPE['xpath'].format(ship_type))
        helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_SEARCH['xpath'])
        
        new_vessel_search = True
        attempt_first_vessel_search = 0

        while True:
            print('Outer while')
            try:
                if new_vessel_search:
                    time.sleep(4)
                    # Scroll through pages to load data
                    for i in range(total_pages_to_scroll):
                        print('Scrolling to bottom to seach vessel: {0}'.format(i+1))
                        helper.scrollIntoBottom()
                        time.sleep(5)

                vessel_name = helper.waitForElementVisibilityAndGetText(
                    LocatorConfig.VESSEL_NAME['xpath'].format(count),
                    LocatorConfig.VESSEL_NAME['name']
                ).strip()

                first_vessel_name = helper.waitForElementVisibilityAndGetText(
                    LocatorConfig.VESSEL_NAME['xpath'].format(1),
                    LocatorConfig.VESSEL_NAME['name']
                ).strip()
                print('First vessel name found')

                if first_vessel_name == 'None':
                    print(f"First vessel not found, attempt {attempt_first_vessel_search}")
                    helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_DROPDOWN_SHIP_TYPE['xpath'])
                    helper.waitForElementUntilClickableAndClick(LocatorConfig.OPT_SHIP_TYPE['xpath'].format(ship_type))
                    helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_SEARCH['xpath'])
                    time.sleep(3)

                    if attempt_first_vessel_search > 3:
                        break
                    else:
                        attempt_first_vessel_search += 1
                        continue
                elif first_vessel_name != 'None' and vessel_name == 'None':
                    for i in range(3):
                        print(f'Scrolling to bottom to seach vessel: {i+1}')
                        helper.scrollIntoBottom()
                        time.sleep(5)

                if vessel_name in vessel_name_list:
                    helper.scrollIntoView(LocatorConfig.VESSEL_NAME['xpath'].format(count))
                    time.sleep(0.5)
                    print(f"Vessel {vessel_name} already processed. Skipping...")
                    print(f"Total Vessel collected = {count - 1}, search for vessel number {count}")
                    count += 1
                    target_data += 1
                    continue

                # If new vessel, retrieve detailed information
                print(f"Processing new vessel: {vessel_name}")
                imo_number = helper.waitForElementVisibilityAndGetText(
                    LocatorConfig.IMO_NUMBER['xpath'].format(count),
                    LocatorConfig.IMO_NUMBER['name']
                ).split(":")[-1].strip()

                # Get vessel details
                time.sleep(5)
                helper.scrollIntoView(LocatorConfig.VESSEL_NAME['xpath'].format(count))
                helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_VESSEL_NAME['xpath'].format(count))
                helper.waitForElementVisibility(LocatorConfig.COL_VESSEL_DETAIL['xpath'])
                vessel_details = data_helper.get_vessel_details(helper, count)

                # Get vessel engine
                helper.waitForElementUntilClickableAndClick(LocatorConfig.BTN_ASSETS['xpath'].format(count))
                helper.waitForElementVisibility(LocatorConfig.COL_VESSEL_MACHINERY['xpath'])
                engine_details = data_helper.get_engine_details(helper)

                # Combine all data
                vessel_data = {**vessel_details, **engine_details}
                vessel_data['Vessel Name'] = vessel_name
                vessel_data['IMO Number'] = imo_number

                # Save the vessel data to xlsx
                print('Prepare to save to csv and excel...')
                data_helper.appendToXlsx("vessel_data.xlsx", [vessel_data])
                data_helper.appendNameToFile("vessel_name.txt", vessel_name)

                time.sleep(5)
                count += 1
                new_vessel_search = True
                break

            except Exception as e:
                print(f"Error processing vessel. Retry vessel...")
                continue
        
        print(count)
        return count

if __name__ == "__main__":
    ship_type = 'Bulk Carrier'

    chrome_driver_version = '130.0.6723.92'
    driver = setupDriver(headless=True).setup()
    helper = webDriverHelper(driver)
    data_helper = dataHelper()

    vessel_name_list = data_helper.getNameFromFile('vessel_name.txt')
    target_data_daily = 100
    count_vessel_data = len(vessel_name_list)
    total_target_data = count_vessel_data + target_data_daily
    print(vessel_name_list)

    while count_vessel_data < total_target_data:
        print(f"Last Vessel Name : {vessel_name_list[-2]}, with total : {count_vessel_data - 1}, target acquiring = {total_target_data}")
        count_vessel_data = process_vessel_data(helper, count_vessel_data + 1, vessel_name_list, target_data_daily, ship_type)  # Process each vessel, update count, and check list
        vessel_name_list = data_helper.getNameFromFile('vessel_name.txt')   # Re-load the vessel list after processing (in case new vessels are appended)
        print(vessel_name_list)
        
    print('Vessel data gathered : {0}'.format(count_vessel_data))
    driver.quit()
