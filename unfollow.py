#!/usr/bin/env python3

"""

This is a Python 3 script that unfollows people that don't follow you.
Use it like this:

    ./unfollow.py config.json [--confirm]

The config.json file should contains your Twitter app credentials in this
format:

    {
        "consumer_key": "<consumer_key>",
        "consumer_secret": "<consumer_secret>",
        "access_token": "<access_token>",
        "access_token_secret": "<access_token_secret>""
    }

The confirm flag is optional. If you don't pass it the script will unfollow
everybody that doesn't folow you. If you do the script will ask you if you
want to keep following each user.

"""

import argparse
import json

import tweepy

def get_args():
    """Parse user args, get config file path and whether to confirm unfollowing"""
    parser = argparse.ArgumentParser(description='Unfollow app')
    parser.add_argument('config_filename', help='Path to JSON config file.')
    parser.add_argument('-c', '--confirm', help='confirm deletion of each user',
                        action='store_true', default=False)
    return parser.parse_args()

def load_config(config_filename):
    """Read the config file and parse the JSON"""
    with open(config_filename, 'r') as config_file:
        return json.load(config_file)

def run(api, confirm):
    """Runs the main logic"""
    my_id = api.me().id
    following_ids = api.friends_ids(my_id)
    followers_ids = api.followers_ids(my_id)
    for user_id in following_ids:
        if user_id not in followers_ids:
            user = api.get_user(user_id)
            if confirm:
                prompt = 'Keep following {}/{}? '.format(user.screen_name, user.name)
                if str(input(prompt).lower()) == 'y':
                    continue
            api.destroy_friendship(user_id)

def main():
    """Loads the config file and instantiates the Tweepy API object"""
    args = get_args()
    config = load_config(args.config_filename)
    auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth)
    run(api, args.confirm)

if __name__ == '__main__':
    # Whatever
    main()
