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

filters = {
  "java-influencers": {
    "$and": [
      {"$text": {"$search": "java #java @java spring"}},
      {"followers_count": {"$gt": 3000}},
      {"follow_status": {"$ne": "refollowed"}}
    ]
  },
  "java-ee": {
    "$and": [
      {"$text": {"$search": "j2ee javaee jee \"java ee\""}},
      {"follow_status": {"$ne": "refollowed"}}
    ]
  },
  "spring-framework": {
    "$and": [
      {"$text": {"$search": "spring springboot springframework"}},
      {"follow_status": {"$ne": "refollowed"}}
    ]
  },
}

for list_name, query in filters.items():
  print "Processing list %s list_name ... " % list_name
  for friend in collection_friends.find(query):
    friend_id = friend["_id"]
    api.CreateFriendship(user_id=friend_id, follow=True)
    api.CreateListsMember(slug=list_name, user_id=friend_id, owner_id=TWITTER_USER_ID)
    collection_friends.update({"_id": friend_id}, {"$set": {"follow_status": "refollowed"}})
    print "Updated friend #%s" % friend_id
