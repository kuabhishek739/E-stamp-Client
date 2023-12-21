copies = 1000 # Enter number of copies you want
paid_by="MASTER CAPITAL SERVICES LTD" # Enter Stamp Duty Paid By Party Name
first_party= "MASTER CAPITAL SERVICES LTD" # Enter First Party Name
second_party = "" # Enter Second Party Name
number1='0000000000' # Enter Number of First Party
number2='' # Enter Number of Second Party
des= "" # Enter Description
#paid_by = "IFFCO KISAN FINANCE LTD" # Enter Stamp Duty Paid By Party Name if applicable
password = "password" # Enter Password
user_id = "username" # Enter Username
amt='50'   # Enter Stamp paper Value Amount



ga= "//*[@id=\"RegSD\"]/option[41]" # General Agreement
aff= "//*[@id=\"RegSD\"]/option[5]" # Affidavit
ind ='//*[@id=\"RegSD\"]/option[44]' # Indemnity
undertaking ='//*[@id=\"RegSD\"]/option[94]' # Undertaking
memo = '//*[@id=\"RegSD\"]/option[6]' # Memorandum or Agreement
other = "//*[@id=\"RegSD\"]/option[63]" # Others
art48 = "//*[@id=\"RegSD\"]/option[49]" # Article 48
partnership = "//*[@id=\"RegSD\"]/option[65]" # Partnership
car = "//*[@id=\"RegSD\"]/option[20]" # Car Loan/ Loan Agreement
poa48c = "//*[@id=\"RegSD\"]/option[69]" # POA 48C
adoption = "//*[@id=\"RegSD\"]/option[4]" # Adoption Deed



import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.shcilestamp.com/eStampIndia/useradmin/UserAdminLoginServlet?rDoAction=LoadLoginPage")
user_id = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[3]/td[2]/input").send_keys(user_id)
paswd= driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[1]/td/table[3]/tbody/tr/td/table/tbody/tr[4]/td[2]/input").send_keys(password)

start = input("PRESS ENTER TO START SAVING")

if(start):
    ##Create
    for i in range(copies):
        create_button= driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[1]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[1]/a").click()
        driver.find_element(By.XPATH,"//*[@id=\"RegSD\"]").click()
        driver.find_element(By.XPATH,other).click()
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr[1]/td/table[3]/tbody/tr[1]/td[2]/form/table/tbody/tr[4]/td/table/tbody/tr/td/input").click()

        driver.find_element(By.XPATH,"//*[@id=\"TextField6Mand\"]").send_keys(paid_by)
        driver.find_element(By.XPATH,"//*[@id=\"TextArea8Mand\"]").send_keys(des)#description
        driver.find_element(By.XPATH,"//*[@id=\"TextField11Mand\"]").send_keys(first_party)
        driver.find_element(By.XPATH,"//*[@id=\"TextField18Mand\"]").send_keys(second_party)
##    driver.find_element(By.XPATH,"//*[@id=\"TextField24Mand\"]").send_keys(paid_by) #Stamp duty paid by

##    driver.find_element_by_xpath("//*[@id=\"TextField24Mand\"]").send_keys(paid_by)
        driver.find_element(By.XPATH,"//*[@id=\"TextField28Mand\"]").send_keys(amt)
        driver.find_element(By.XPATH,"//*[@id=\"fpMobNo\"]").click()
        time.sleep(0.00001)
        alert = Alert(driver)
      

        alert.accept()

        driver.find_element(By.XPATH,"//*[@id=\"fpMobNo\"]").send_keys(number1)
        driver.find_element(By.XPATH,"//*[@id=\"spMobNo\"]").send_keys(number2)
        driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[3]/tbody/tr[2]/td[2]/input[2]").click()

        time.sleep(0.00001)
        alert = Alert(driver)

        alert.accept()
        print(f"Saved Papers {i+1}")
