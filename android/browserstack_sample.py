from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials
    "browserstack.user" : "YOUR_USERNAME",
    "browserstack.key" : "YOUR_ACCESS_KEY",

    # Set URL of the application under test
    "app" : "bs://<app-id>",

    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

# Test case for the corssy app. 

#  Select language
driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="btnEnglish"]/android.view.View').click()
driver.implicitly_wait(30)
#driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="btnArabic"]/android.view.ViewGroup').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.View').click()
driver.implicitly_wait(30)



#  Select already have an account
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView').click()
driver.implicitly_wait(30)


#  Login with facebook
driver.find_element_by_class_name('android.view.View').click()
driver.implicitly_wait(30)
driver.find_element_by_class_name('android.widget.Button').click()
driver.implicitly_wait(30)


# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
