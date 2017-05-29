import tweepy
import os

import credentials
import webdriver


IMAGE = 'ou'
SUMMARY = 's'
PAGE_TITLE = 'pt'



def _get_api():
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.TOKEN, credentials.SECRET)
    return tweepy.API(auth)

API = _get_api()


def send_tweet(image_filename, text, reply_to=None, reply_id=None):

    tweet_text = '@%s %s' % (reply_to, text)

    if len(tweet_text) > 140:
        tweet_text = tweet_text[:137] + '...'

    print tweet_text

    API.update_with_media(filename=image_filename,
        status=tweet_text, in_reply_to_status_id=reply_id)


def get_tweets(username):

    return API.user_timeline(username)


def main():
    them = 'each_wordsquare'
    me = 'square_meaning'

    dir_path = os.path.dirname(os.path.realpath(__file__))
    download_path = os.path.join(dir_path, "downloaded_images")
    try:
        os.makedirs(download_path)
    except OSError as exc:
        pass

    my_tweets = get_tweets(me)
    their_tweets = get_tweets(them)

    wordsquare_tweets_by_id = {x.id: x for x in wordsquare_tweets}
    previous_tweets = set(x.in_reply_to_status_id for x in my_tweets
        if x.in_reply_to_status_id is not None)

    new_tweets = set(wordsquare_tweets_by_id.keys()) - previous_tweets

    for tweet in sorted(new_tweets):
        text = wordsquare_tweets_by_id[tweet].text
        image_meta = webdriver.load_image_info(text, 5)

        for image in image_meta:
            if image.get(SUMMARY):
                image_name = os.path.join(download_path, os.path.basename(image.get(IMAGE)))
                webdriver.download_image(image.get(IMAGE), image_name)

                send_tweet(image_name, image.get(SUMMARY), them, tweet)
                break
        else:
            for image in image_meta:
                if image.get(PAGE_TITLE):
                    image_name = os.path.join(download_path, os.basename(image.get(IMAGE)))
                    webdriver.download_image(image.get(IMAGE), image_name)


if __name__ == '__main__':
    main()
