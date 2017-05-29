import json
import logging
import os
from PIL import Image
from StringIO import StringIO

import requests
from selenium import webdriver


if os.getcwd() not in os.environ["PATH"]:
    os.environ["PATH"] += os.pathsep + os.getcwd()


def load_image_info(search_text, number_of_images):

    url = u"https://www.google.com/search?q={}&source=lnms&tbm=isch".format(
        search_text.replace('\n', ' '))

    print url

    driver = webdriver.Chrome()
    driver.get(url)

    images = driver.find_elements_by_xpath("//div[@class='rg_meta']")
    image_info = []
    for image in images[:number_of_images]:
        image_info.append(json.loads(image.get_attribute('innerHTML')))

    return image_info


def download_image(image_url, filename):

    r = requests.get(image_url)
    i = Image.open(StringIO(r.content))
    i.save(filename)
