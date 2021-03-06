# wordsquare_meanings

Apophenia is the human tendency to perceive meaningful patterns within random data [[Wikipedia](https://en.wikipedia.org/wiki/Apophenia)]. Despite the wordsquares generated by Brian Gawalt's [@each_wordsquare](https://twitter.com/each_wordsquare) bot being random gramatically, they frequently seem like they might actually make sense. This bot uncovers that hidden meaning. The current implementation does this by looking them up with Google Image search, and replying with the result.

# Setting up the bot:

## Installing

To get this bot to run on a Linux machine without a display, we need to install a few dependencies:

```
sudo apt-get update
sudo apt-get install chromium-browser xvfb
```

Next, install the dependencies needed for this program.

```
sudo apt-get install python-pip
pip install selenium
pip install requests
pip install tweepy
```

The final thing that is needed is the [driver](https://sites.google.com/a/chromium.org/chromedriver/) Selenium will use to connect to Chrome. This code assumes that the driver is located in the current directory, but as long as it is on your PATH, things should work.

## Running

To run from the command line without a display, we need to start the X virtual frame buffer, which will allow us to open a browser via Selenium.

```
Xvfb :10 -ac &
export DISPLAY=:10
```

# References

Some links that were helpful in figuring out how to get this set up.

* Downloading images from Google Image Search [link](https://github.com/atif93/google_image_downloader).
* Getting Selenium to run in headless mode [link](https://medium.com/@griggheo/running-selenium-webdriver-tests-using-firefox-headless-mode-on-ubuntu-d32500bb6af2).

# Credits



Profile photo is taken from the [first result](https://www.psychologytoday.com/blog/reality-play/201207/being-amused-apophenia) for a Google Image search for Apophenia.
