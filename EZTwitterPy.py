import pickle
import configparser
import argparse
from twython import Twython

def post_tweet(message, media_fname=None):
    config = configparser.ConfigParser()
    config.read("auth.conf")

    twitter = Twython(
        config['KEYS']['consumer_key'],
        config['KEYS']['consumer_secret'],
        config['KEYS']['access_token'],
        config['KEYS']['access_token_secret']
    )

    if media_fname is None:
        twitter.update_status(status=message)
    else:
        photo = open(media_fname)
        response = twitter.upload_media(media=photo)
        twitter.update_status(status=message, media_ids=[response['media_id']])

def main():
    parser = argparse.ArgumentParser(description="Simple tool/API for tweeting in python")
    parser.add_argument('--message', dest='message', type=str,
                        help='The text to add to the tweet')
    parser.add_argument('--image', dest='fname', type=str,
                        help='Path to the single image or video to post')
    args = parser.parse_args()

    post_tweet(args.message, media_fname=args.fname)

if __name__ == "__main__":
    main()

