from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Create login and webpage url details in a class


url = "https://opensource-demo.orangehrmlive.com"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
time.sleep(3)

#create login cerdentials

def login(self):
            username = 'Admin'
            password = 'admin123'
            self.driver.get(self.url)
            time.sleep(2)

#assign the values to their X-Path
      class HR(self):
      my_username = self.driver.find_element(by=By.Xpath, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div')
      my_username.send_keys(username)
      my_password = self.driver.find_element(by=By.Xpath, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
      my_password.send_keys(password)
      submit_button = self/driver.find_element(by=By.Xpath, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
      submit_button.click()
      time.sleep(5)

      #creating New employee and updating their details

      def create_employee(self):
            create_employee = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
            create_employee_new = self.driver.find_element(by=By.Xpath, value = create_employee)
            create_employee_new.click()
            time.sleep(5)

      def employee_credentials:
            employee_firstname = 'input[name="firstname"]'
            employee_firstname_new = self.driver.find_element(by=By.CSS_SELECTOR, value=employee_firstname)
            employee_firstname_new.send_keys("MADANKUMAR")
            time.sleep(2)

            employee_middlename = 'input[name="middlename"]'
            employee_middlename_new = self.driver.find_element(by=By.CSS_SELECTOR, value=employee_middlename)
            employee_middlename_new.send_keys(" ")
            time.sleep(2)

            employee_lastname = 'input[name="lastname"]'
            employee_lastname_new = self.driver.find_element(by=By.CSS_SELECTOR, value=employee_lastname)
            employee_lastname_new.send_keys("SUBRAMANIAN")
            time.sleep(2)

            new_username = ' #app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(4) > div > div:nth-child(1) > div > div:nth-child(2) > input'
            new_username_1 = self.driver.find_element(by=By.CSS_SELECTOR, value=new_username)
            new_username_1.send_keys("Madankumar")
            time.sleep(2)


            new_password = ' #app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div.oxd-form-row.user-password-row > div > div.oxd-grid-item.oxd-grid-item--gutters.user-password-cell > div > div:nth-child(2) > input'
            new_password_1 = self.driver.find_element(by=By.CSS_SELECTOR, value=new_password)
            new_password_1.send_keys("Madan@123.")
            time.sleep(2)

            confirm_password = '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input '
            confirm_password_new = self.driver.find_element(by=By.CSS_SELECTOR, value=confirm_password)
            confirm_password_new.send_keys("Madan@123.")
            time.sleep(2)

            submit_button = ' //*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
            submit_button_new = self.driver.find_element(by=By.Xpath, value =submit_button )
            submit_button_new.click()

            #to verify the employee details in admin center

            admin_panel = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span '
            admin_panel_new = self.driver.find_element(by=By.Xpath, value = admin_panel)
            admin_panel_new.click()
            time.sleep(2)

            #verify the employee details have added or not

            def verify_details(self):
                  verify_username = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input'
                  verify_username_new = self.driver.find_element(by=By.Xpath, value = verify_username)
                  verify_username_new.send_keys("Madankumar")
                  time.sleep(2)

                  dropdown_ess = ''
                  dropdown_ess_new = self.driver.find_element(by=By.Xpath, value = dropdown_ess)
                  dropdown_ess_new.click()
                  time.sleep(2)

                  dropdown_select = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div '
                  dropdown_select_new = self.driver.find_element(by=By.Xpath, value = dropdown_select)
                  dropdown_select_new.click()
                  time.sleep(2)

                  dropdown_employee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i'
                  dropdown_employee_new = self.driver.find_element(by=By.Xpath, value = dropdown_employee)
                  dropdown_employee_new.send_keys("Madankumar  Subramanian")
                  time.sleep(2)
                  #for selecting enable option on rhs

                  enable_option = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'
                  enable_option_new = self.driver.find_element(by=By.Xpath, value = enable_option)
                  enable_option_new.click()
                  time.sleep(2)

                  search_button = ' //*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
                  search_button_new = self.driver.find_element(by=By.Xpath,value = search_button)
                  search_button_new.click()
                  time.sleep(2)

                  logout_scroll = self.driver.find_element(by=By.Xpath, value ='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a')
                  logout_scroll.click()
                  time.sleep(2)

            def relogin(self):
                   username_new = "Madankumar"
                   password_new = "Madan@123."
                   self.driver.get(self.url)
                   time.sleep(2)

                   username_path = ' //*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
                   username_path_new = self.driver.find_element(by=By.Xpath,value = username_path )
                   username_path_new.send_keys(username_new)
                   time.sleep(2)

                   password_path = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
                   password_path_new = self.driver.find_element(by=By.Xpath, value = password_path)
                   password_path_new.send_keys(password_new)
                   time.sleep(2)

                   submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
                   submit_button_new = self.driver.find_element(by=By.Xpath, value = submit_button)
                   submit_button_new.click()
                   time.sleep(2)

exit()



