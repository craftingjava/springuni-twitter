# Managing Twitter Friends

This is a simple set of scripts for managing people you're following on Twitter.

# Usage

1. Create environment properties file `.env` with the following contents

    ```
    CONSUMER_KEY="..."
    CONSUMER_SECRET="..."
    ACCESS_TOKEN_KEY="..."
    ACCESS_TOKEN_SECRET="..."
    TWITTER_USER_ID="..."
    ```

2. Source `.env` before using the scripts

    ```
    source .env
    ```

3. Have a local *MongoDB* up and running, default setup is sufficient

4. Fetch friends with `fetch_twitter_friends.py`
 
    ```
    ./fetch_twitter_friends.sh
    ```

5. Create text index for some fields in *MongoDB*

    ```
    db.friends.createIndex(
       {
         description: "text",
         name: "text"
       }
     )
     ```

6. Un-follow everyone

    ```
    ./unfollow_twitter_friends.sh
    ```

7. Customize the query in script `refollow_twitter_friends.py` to re-follow some of them

    ```
    ./refollow_twitter_friends.sh
    ```
