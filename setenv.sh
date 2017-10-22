#!/usr/bin/env bash

source ./.env

export CONSUMER_KEY
export CONSUMER_SECRET
export ACCESS_TOKEN_KEY
export ACCESS_TOKEN_SECRET
export TWITTER_USER_ID

if [ ! -d venv ]; then
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi

source venv/bin/activate
