from selenium.webdriver.common.by import By
class registerpage:
    myaccountlink="My Account"
    registerlink="Register"
    firstname="input-firstname"
    lastname="input-lastname"
    emailid="input-email"
    password="input-password"
    yerorno="//*[@id='input-newsletter-yes']"
    checkbox="//*[@id='form-register']/div/div/div/input"
    submitbutton="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def clickonmyaccount(self):
        self.driver.find_element(By.LINK_TEXT,self.myaccountlink).click()
    def clickonregisterlink(self):
        self.driver.find_element(By.LINK_TEXT,self.registerlink).click()
    def enterfname(self,nameone):
        self.driver.find_element(By.ID,self.firstname).send_keys(nameone)
    def enterlname(self,nametwo):
        self.driver.find_element(By.ID,self.lastname).send_keys(nametwo)
    def enteremail(self,username):
        self.driver.find_element(By.ID,self.emailid).send_keys(username)
    def enterpassword(self,password):
        self.driver.find_element(By.ID,self.password).send_keys(password)
    def clickyesorno(self):
        self.driver.find_element(By.XPATH,self.yerorno).click()
    def clickcheckbox(self):
        self.driver.find_element(By.XPATH,self.checkbox).click()
    def clickonsubmit(self):
        self.driver.find_element(By.XPATH,self.submitbutton).click()
