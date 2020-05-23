from bs4 import BeautifulSoup
from selenium import webdriver


def get_twitter_stats():
    twitter_url = "https://twitter.com/benscstutorials"
    driver = webdriver.Chrome()
    driver.get(twitter_url)
    content = driver.page_source.encode("utf-8").strip()
    twitter_soup = BeautifulSoup(content, "lxml")
    stats = twitter_soup.findAll(
        "span",
        class_="css-901oao css-16my406 r-1qd0xha r-vw2c0b r-ad9z0x r-bcqeeo r-qvutc0",
    )
    following = stats[0].text.strip()
    followers = stats[1].text.strip()
    print("Twitter Stats: {} followers and {} following".format(followers, following))


def get_instagram_stats():
    instagram_url = "https://www.instagram.com/benscstutorials/"
    driver = webdriver.Chrome()
    driver.get(instagram_url)
    content = driver.page_source.encode("utf-8").strip()
    instagram_soup = BeautifulSoup(content, "lxml")
    stats = instagram_soup.findAll("span")
    posts = stats[1].text.strip()
    followers = stats[2].text.strip()
    following = stats[3].text.strip()
    print(
        "Instagram Stats: {} posts, {} followers, and {} following".format(
            posts, followers, following
        )
    )


def get_youtube_stats():
    youtube_url = "https://www.youtube.com/channel/UCLMdmCCRFGWt7rktx6tMErw/about?view_as=subscriber"
    driver = webdriver.Chrome()
    driver.get(youtube_url)
    content = driver.page_source.encode("utf-8").strip()
    youtube_soup = BeautifulSoup(content, "lxml")
    views = youtube_soup.findAll(
        "yt-formatted-string", class_="style-scope ytd-channel-about-metadata-renderer"
    )
    for view in views:
        if "views" in view.text:
            views = view.text.strip()
    subscribers = youtube_soup.find(id="subscriber-count").text.strip()
    print("YouTube Stats: {} and {}".format(subscribers, views))


get_twitter_stats()
get_instagram_stats()
get_youtube_stats()
