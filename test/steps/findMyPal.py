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

	
	

	
	
    
