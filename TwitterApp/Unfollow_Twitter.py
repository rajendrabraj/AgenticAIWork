import tweepy
from datetime import datetime

import logging
import os
from datetime import datetime

# ==== CONFIGURATION ====
BEARER_TOKEN = "XXXXXXXXXXXXX"
API_KEY = "XXXXXXXXXXXXX"
API_SECRET = "XXXXXXXXXXXXX"
ACCESS_TOKEN = "XXXXXXXXXXXXX"
ACCESS_SECRET = "XXXXXXXXXXXXX"

YEAR_THRESHOLD = 2019 # Unfollow if account created before this year




# construct a format for log file name
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", log_file)
os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, log_file)
print(log_file_path)


# Handles logging information
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
    
)
logging.info('This is the first message.')



# ==== AUTHENTICATION ====
client = tweepy.Client(
bearer_token=BEARER_TOKEN,
consumer_key=API_KEY,
consumer_secret=API_SECRET,
access_token=ACCESS_TOKEN,
access_token_secret=ACCESS_SECRET
)

response = client.get_me()
print(response.data.name)

print("Configuration and Authentication done")       

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api_v1 = tweepy.API(auth)




print("Authentication done")       


# ==== GET MY USER ID ====
my_user = client.get_me().data
#my_user_id= "@rajthinker"
my_user_id = my_user.id
print ("Show Twtter User ID")

print(my_user)
print(my_user_id)


# ==== FETCH FOLLOWING USERS ====
following = client.get_users_following(
id=my_user_id,
user_fields=["created_at"],
max_results=1000 # Adjust if needed
)

print("FOR Loop started")       

# ==== PROCESS ====
for user in following.data:
    created_year = user.created_at.year
    if created_year < YEAR_THRESHOLD:
        print(f"Unfollowing {user.username} (created in {created_year})")   
        print("Updating the log file")        
        logging.info({user.username} + {created_year} )             
    try:
        client.unfollow_user(target_user_id=user.id)
        target_user_id=user.id
        print(f"Unfollowed {target_user_id}")        
    except Exception as e:
        print(f"Error unfollowing {user.username}: {e}")

print("All Users Unfollowed Done!")
