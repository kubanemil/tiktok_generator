import urllib
import os
from time import sleep
import pickle

def tiktok_download_hashtags(browser, links, i):
    video = browser.find_element_by_css_selector("video")
    video_src = video.get_attribute("src")
    urllib.request.urlretrieve(video_src, f'{i}.mp4')
    sleep(3)
    print(os.path.getsize(f"{i}.mp4")/10**3, "KB")
    os.replace(f"{i}.mp4", f"tiktoks/{i}.mp4")
    print(f"Downloaded {i}.mp4 into 'tiktoks/'")


    #TO get hashtags
    sleep(2)
    hashtag_a = browser.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div[2]/a")
    video_tags = []
    for a in hashtag_a:
        hashtag_text = a.find_element_by_css_selector("strong").text
        video_tags.append(hashtag_text)
    tags_text = ""
    for tag in video_tags:
        tags_text += tag + " "
    with open(f"{i}.txt", "w") as file:
        pickle.dump(tags_text, file)
    print(video_tags)
    print("\n")
