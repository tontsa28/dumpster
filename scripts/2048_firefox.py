import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# This is a bot script for oispakaljaa.com
#

# Mute webdriver audio
profile = webdriver.FirefoxProfile()
profile.set_preference("media.volume_scale", "0.0")

# Initialize Firefox webdriver
driver = webdriver.Firefox(firefox_profile=profile, service_log_path=os.devnull)

# Arrow key variables
rightarrow = Keys.ARROW_RIGHT
leftarrow = Keys.ARROW_LEFT
uparrow = Keys.ARROW_UP
downarrow = Keys.ARROW_DOWN

# Space key variable
spacekey = Keys.SPACE

# Open oispakaljaa.com
driver.get("https://play2048.co")

# Find html body xpath
game = driver.find_element_by_xpath("/html/body")

# Find try again button xpath
try_again = driver.find_element_by_css_selector(".retry-button")

# While process is alive
while True:

    # Press arrow keys in the following order
    game.send_keys(leftarrow)
    game.send_keys(downarrow)
    game.send_keys(rightarrow)
    game.send_keys(uparrow)

    # If game is over, start again
    if try_again.is_displayed():
        try_again.click()