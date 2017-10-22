import os
import twitter
from pymongo import MongoClient


CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN_KEY = os.environ["ACCESS_TOKEN_KEY"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
TWITTER_USER_ID = os.environ["TWITTER_USER_ID"]

api = twitter.Api(
  consumer_key=CONSUMER_KEY,
  consumer_secret=CONSUMER_SECRET,
  access_token_key=ACCESS_TOKEN_KEY,
  access_token_secret=ACCESS_TOKEN_SECRET
)

client = MongoClient()
db = client["twitter"]
collection_friends = db["friends"]

for friend in collection_friends.find({"follow_status": {"$ne": "unfollowed"}}):
  friend_id = friend["_id"]
  api.DestroyFriendship(user_id=friend_id)
  collection_friends.update({"_id": friend_id}, {"$set": {"follow_status": "unfollowed"}})
  print "Updated friend #%s" % friend_id
