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

friend_ids = api.GetFriendIDs(user_id=TWITTER_USER_ID, count=400)
print "Fetched %s friends" % len(friend_ids)

client = MongoClient()
db = client["twitter"]
collection_friends = db["friends"]

for friend_id in friend_ids:
  friend = collection_friends.find_one({"_id": friend_id})
  if friend is None:
    friend = api.GetUser(user_id=friend_id).AsDict()
    friend["_id"] = friend_id
    friend["follow_status"] = "following"
    collection_friends.update({"_id": friend_id}, friend, upsert=True)
    print "Saved friend #%s" % friend_id
  else:
    print "Friend #%s is up-to-date" % friend_id
