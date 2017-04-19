from django.test import LiveServerTestCase
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class SignupTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox(executable_path='/opt/firefox-geckodriver/geckodriver')
        super(SignupTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SignupTestCase, self).tearDown()

    def invalid_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://localhost:8000/login/')
         #find the form element
        # first_name = selenium.find_element_by_id('id_username')
        # last_name = selenium.find_element_by_id('id_last_name')
        # email = selenium.find_element_by_id('id_email')
        # password2 = selenium.find_element_by_id('id_password2')
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        # first_name.send_keys('Yusuf')
        # last_name.send_keys('Unary')
        # email.send_keys('yusuf@qawba.com')
        # password2.send_keys('123456')
        username.send_keys('kantanand@insmartapps.com')
        password.send_keys('abcd@1234s')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        # print '--------------------'
        # print selenium.page_source
        # print '--------------------'
        assert 'Username/Password is not valid. Please try again' in selenium.page_source

    def valid_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://localhost:8000/login/')
        username = selenium.find_element_by_id('id_username')
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_name('login')
        username.send_keys('kantanand@insmartapps.com')
        password.send_keys('abcd@1234')
        #submitting the form
        submit.send_keys(Keys.RETURN)
        assert 'signup page' in selenium.page_source