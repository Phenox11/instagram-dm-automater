# instagram-dm-automater

## Automatically DMs preditermined message to a list a users using Selenium.

## requirements:
- firefox browser
- geckodriver
- Python 3.8
- Selenium

## Steps:
1. rename config_example.py to config.py
2. fill in the required information into config.py
3. if you would like to see what's happening you can remove "options=options" in dm.py

### Example Setup:

    class info ():
        username = 'your username'
        password = 'your password'
        message = "Hey, this is a test message"
        usernames = ['person1 you want to DM', 'person2 you want to DM']
        path = "path to file"