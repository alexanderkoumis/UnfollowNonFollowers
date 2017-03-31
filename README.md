# Unfollow Non-Followers

This is a Python 3 script that unfollows people that don't follow you. Use it like this:
```bash
./unfollow.py config.json [--confirm]
```
The config.json file should contains your Twitter app credentials in this format:
```json
{
    "consumer_key": "<consumer_key>",
    "consumer_secret": "<consumer_secret>",
    "access_token": "<access_token>",
    "access_token_secret": "<access_token_secret>""
}
```
The confirm flag is optional. If you don't pass it the script will unfollow everybody that doesn't folow you. If you do the script will ask you if you want to keep following each user.
