from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
chrome_driver_path = "/Users/thuan/PycharmProjects/pythonProject/chromedriver_win32"
TWITTER_EMAIL = "###"
TWITTER_PASSWORD = "###"

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP)
