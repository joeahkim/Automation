from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service class
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your chromedriver.exe (make sure it matches your installed Chrome version)
driver_path = r"C:\Users\ADMIN\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Replace with the actual path

# Create a Service object
service = Service(driver_path)

# Initialize WebDriver using the Service object
driver = webdriver.Chrome(service=service)

# Navigate to Instagram Login Page
driver.get("https://www.instagram.com/accounts/login/")

# Pause for a moment to allow the page to load
time.sleep(3)

# Find the username and password fields
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Enter your credentials
username_input.send_keys('')  # Replace with your Instagram username
password_input.send_keys('')  # Replace with your Instagram password

# Submit the login form
password_input.send_keys(Keys.RETURN)

# Pause to allow time for login to complete
time.sleep(5)

# Handle "Save Info" pop-up (if it appears)
try:
    not_now_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
    not_now_btn.click()
except:
    pass

# Handle "Turn on Notifications" pop-up (if it appears)
try:
    not_now_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
    not_now_btn.click()
except:
    pass

# Navigate to Instagram Home Page (to view stories)
driver.get("https://www.instagram.com/")
time.sleep(3)

# Locate the first story and click to start viewing stories
try:
    first_story = driver.find_element(By.XPATH, "//*[@style='transform: translateX(82px);']")  # This selector might need updating
    first_story.click()
    time.sleep(2)
except:
    print("No stories available or could not locate the story element")

# Function to automate story viewing at a faster speed
def view_stories(fast_speed=3):
    while True:
        try:
            # Wait for fast_speed seconds between stories
            time.sleep(fast_speed)
            
            # Find and click the "Next Story" button (right side of the screen)
            next_button = driver.find_element(By.XPATH, "//svg[@aria-label='Next']")
            next_button.click()

            try:
                like_button = driver.find_element(By.CLASS_NAME, "x1ypdohk")
                like_button.click()
                print("Liked the story!")
            except:
                print("No like button found, might already be liked or not available.")

            next_button.click()
        except:
            print("No more stories to view or an error occurred")
            break

# Set the speed (faster viewing by decreasing the sleep time)
view_stories(fast_speed=3)

# Quit the driver after completing story viewing
driver.quit()
