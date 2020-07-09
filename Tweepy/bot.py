import tweepy
from time import sleep
from datetime import datetime

# docs: http://docs.tweepy.org/en/latest/api.html

API_KEY = ""
API_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_SECRET_TOKEN = ""

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

FILE = "last_id.txt"


def reply_to_tweets():
    print("Searching for tweets at " + str(datetime.now()))

    def retrieve_last_id(file):
        f_read = open(file, "r")
        last_seen_id = int(f_read.read().strip())
        f_read.close()
        return last_seen_id

    def store_last_id(last_seen_id, file):
        f_write = open(file, "w")
        f_write.write(str(last_seen_id))
        f_write.close()
        return

    last_seen_id = retrieve_last_id(FILE)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")

    for mention in reversed(mentions):
        if "#100DaysOfCode" in mention.full_text:
            last_seen_id = mention.id
            store_last_id(last_seen_id, FILE)
            api.update_status(
                "@" + mention.user.screen_name + " Keep up the great work!", mention.id
            )
            print("Replied to @" + mention.user.screen_name)
            # print(mention.full_text)
            # print(mention.id)
            # print("responding back...")


while True:
    reply_to_tweets()
    sleep(15)
