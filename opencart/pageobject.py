from selenium.webdriver.common.by import By
class loginpage:
    myaccountlink="My Account"
    loginlink="Login"
    emailid="input-email"
    password="input-password"
    submitbutton="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def clickonmyaccount(self):
        self.driver.find_element(By.LINK_TEXT,self.myaccountlink).click()
    def clickonloginlink(self):
        self.driver.find_element(By.LINK_TEXT,self.loginlink).click()
    def enteremail(self,username):
        self.driver.find_element(By.ID,self.emailid).send_keys(username)
    def enterpassword(self,password):
        self.driver.find_element(By.ID,self.password).send_keys(password)
    def clickonsubmit(self):
        self.driver.find_element(By.XPATH,self.submitbutton).click()
