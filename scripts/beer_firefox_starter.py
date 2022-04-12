import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver

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
driver.get("http://oispakaljaa.com")

# Find html body xpath
game = driver.find_element_by_xpath("/html/body")

# Find try again button xpath
try_again = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div/a[2]")

# Find drunk count xpath
drunk_count = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]")

# Find game won button xpath
game_won = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div/a[1]")

# While process is alive
while True:

    # Press arrow keys in the following order
    game.send_keys(leftarrow)
    game.send_keys(downarrow)
    game.send_keys(rightarrow)
    game.send_keys(uparrow)

    # If game is over, start again
    if try_again.is_displayed():
        game.send_keys(spacekey)
        driver.implicitly_wait(5)
        print(drunk_count)

        # If xp exceeds 1000, stop the script
        if drunk_count.get_attribute("") == "1000":
            exit()

    # If game is won, stop the script
    if game_won.is_displayed():
        exit()