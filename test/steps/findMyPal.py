from behave import *
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import html5lib

''' Reachablity to website feature '''
@given(u'i am at browser')
def step_impl(context):
    context.driver = webdriver.Chrome()   
    pass	

@when(u'i enter "http://findmypal.pythonanywhere.com/" url')
def step_impl(context):
    context.driver.get("http://findmypal.pythonanywhere.com/login?")
    pass

@then(u'i should see findmypal signin page')
def step_impl(context):
    assert "Find My Pal" in context.driver.title
	

''' signin to website feature  '''	
 
  #user login with valid kent e-mail scenario
  
@given(u'i am at Find My Pal signin page')
def step_impl(context):
    context.driver = webdriver.Chrome()    
    driver = context.driver
    driver.get("http://findmypal.pythonanywhere.com/login?")
    pass

@when(u'i click on "signin with google" option')
def step_impl(context):
    window_before = context.driver.window_handles[0]
    context.driver.find_element_by_id("signin-google").click()
    time.sleep(2)
    window_after = context.driver.window_handles[1]
    context.driver.switch_to_window(window_after)
    #print(context.driver.page_source)
    pass
	
@when(u'i enter valid kent e-mail and password')
def step_impl(context):
    context.elem = context.driver.find_element_by_id("Email")
    context.elem.send_keys("abhoomre@kent.edu")
    time.sleep(2)
    context.driver.find_element_by_id("next").click()
    time.sleep(2)
    context.elem = context.driver.find_element_by_id("Username")
    context.elem.send_keys("abhoomre")
    context.elem = context.driver.find_element_by_id("Password")
    context.elem.send_keys("Abhilash!0")
    context.driver.find_element_by_id("Button1").click()
    context.driver.switch_to_window(context.driver.window_handles[0])
    time.sleep(5)
    #print(context.driver.page_source)
	
@then(u'the page should show "My name"')
def step_impl(context):
    assert "Abhi" in context.driver.page_source
	
	
	#user signin with non-kent e-mail scenario

@when(u'i enter non-kent e-mail and password')
def step_impl(context):
    context.elem = context.driver.find_element_by_id("Email")
    context.elem.send_keys("abhilashreddy396@gmail.com")
    time.sleep(2)
    context.driver.find_element_by_id("next").click()
    time.sleep(2)
    context.elem = context.driver.find_element_by_id("Passwd")
    context.elem.send_keys("abhilash396")
    context.driver.find_element_by_id("signIn").click()
    time.sleep(2)
    context.driver.switch_to_window(context.driver.window_handles[0])
    time.sleep(5)

@then(u'the page should display "Please try logging in with Kent Email Address" message')
def step_impl(context):
    display = context.driver.find_element_by_id("login_error")
    assert display.is_displayed()

	

''' Profile page feature  '''

# navigating to profile page scenario

@given(u'signed in with valid kent e-mail')
def step_impl(context):
    window_before = context.driver.window_handles[0]
    context.driver.find_element_by_id("signin-google").click()
    time.sleep(2)
    window_after = context.driver.window_handles[1]
    context.driver.switch_to_window(window_after)
    context.elem = context.driver.find_element_by_id("Email")
    context.elem.send_keys("abhoomre@kent.edu")
    time.sleep(2)
    context.driver.find_element_by_id("next").click()
    time.sleep(2)
    context.elem = context.driver.find_element_by_id("Username")
    context.elem.send_keys("abhoomre")
    context.elem = context.driver.find_element_by_id("Password")
    context.elem.send_keys("Abhilash!0")
    context.driver.find_element_by_id("Button1").click()
    context.driver.switch_to_window(context.driver.window_handles[0])
    time.sleep(5)

@when(u'i click on "profile area" option')
def step_impl(context):
    context.driver.find_element_by_id("profile_picture").click()
    time.sleep(3)
    pass


@then(u'i should see "proile info" page')
def step_impl(context):
    assert "Profile Info" in context.driver.title



# displaying user profile scenario

@then(u'i should see "My personal details" and "interests"')
def step_impl(context):
    first_name  = context.driver.find_element_by_id("firstname").get_attribute('value')
    middle_name = context.driver.find_element_by_id("middlename").get_attribute('value')
    last_name   = context.driver.find_element_by_id("lastname").get_attribute('value')
    nick_name   = context.driver.find_element_by_id("nickname").get_attribute('value')
    graduate_status = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[1]/input[2]").get_attribute('checked')
    education_year = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[2]/input[5]").get_attribute('checked')
    interested_category1 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[1]").get_attribute('checked')
    interested_category2 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[2]").get_attribute('checked')
    interested_category3 = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[3]").get_attribute('checked')
    
    assert first_name == 'Abhilash reddy'
    assert middle_name== ''
    assert last_name  == 'Bhoomreddy'
    assert nick_name  == 'Abhilash'
    assert graduate_status == 'true'
    assert education_year == 'true'
    assert interested_category1 == 'true'
    assert interested_category2 == 'true'
    assert interested_category3 == 'true'



# updating user profile scenario

@when(u'i update "My presonal details" and "interest"')
def step_impl(context):
    
    #Changing first_name "Abhilash reddy to Abhilash"
    context.elem = context.driver.find_element_by_id("firstname")
    context.elem.clear()
    context.elem.send_keys("Abhilash")
    
    #Changing nick_name "Abhilash to Abhi
    context.elem = context.driver.find_element_by_id("nickname")
    context.elem.clear()
    context.elem.send_keys("Abhi")
    
    #setting gender to "Male"
    context.driver.find_element_by_xpath("//*[@id='gender']/option[2]").click()
    
    
    #adding "pool to interested catogiry""
    if (context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").get_attribute('checked') != 'true'):
        context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").click()


@when(u'click on "save changes" button')
def step_impl(context):
    
    context.driver.find_element_by_id("update_profile").click()

@then(u'page should display "Your Profile has been Updated!!!" message')
def step_impl(context):
    display = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[1]")
    print(display.is_displayed())
    assert display.is_displayed()

@then(u'i should see updated "personal details" and "interests"')
def step_impl(context):
    first_name  = context.driver.find_element_by_id("firstname").get_attribute('value')
    nick_name   = context.driver.find_element_by_id("nickname").get_attribute('value')
    gender = context.driver.find_element_by_xpath("//*[@id='gender']/option[2]").get_attribute('value')
    updated_category = context.driver.find_element_by_xpath("//*[@id='profilePic']/div[3]/div[3]/input[4]").get_attribute('checked')
    assert first_name == 'Abhilash'
    assert nick_name == 'Abhi'
    assert gender == 'Male'
    assert updated_category == 'true'





