from InstaFollower import InstaFollower

INSTA_USERNAME = '########'
INSTA_PASSWORD = '########'

CHROME_DRIVER_PATH = "/Users/thuan/PycharmProjects/pythonProject/chromedriver_win32"
SIMILAR_ACCOUNT = 'travelandleisure'

insta_follower = InstaFollower()
insta_follower.login(INSTA_USERNAME, INSTA_PASSWORD)
insta_follower.find_followers(SIMILAR_ACCOUNT)
insta_follower.follow()
