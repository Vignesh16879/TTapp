import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.keys import Keys

# Models, Forms, Utils, Serializers
from .models import teacher, student


def test_login():
    
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/login")
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id", "password")
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")
    password_input.send_keys(Keys.RETURN)
    time.sleep(2)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    

def test_add_holiday():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/add-holiday")
    time.sleep(1)

    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    

def test_add_teacher():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/add-teacher/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

def test_add_student():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/add-student/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"

    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    


def test_edit_student():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/edit-student/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    
def test_edit_teacher():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/edit-teacher/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    
def test_edit_holiday():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/edit-holiday/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

def test_all_student():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/all-students/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    
def test_all_teachers():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/all-teachers/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"

def test_all_holiday():
    service = Service("/home/dv/Desktop/sdos/testing/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get("http://127.0.0.1:8000/")
    
    driver.get("http://127.0.0.1:8000/all-holiday/")
    time.sleep(1)
    
    actual_title = driver.title
    expected_title = "EduSchedula"
    
    driver.quit()
    assert actual_title == expected_title, f"Expected title: {expected_title}, Actual title: {actual_title}"
    
# database tests

# def test_add_teacher():

# def test_add_teacher():
#     user = CustomUser.objects.create_user(username='newuser', password='password123')
#     user.age = 25
#     user.save()
# # def test_add_teacher():

# # def test_add_teacher():