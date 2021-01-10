from selenium import webdriver
from time import sleep
from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint


class Bot():

    links = []

    comments = [
        'Great Post!', 'Awesome!'
    ]

    accounts = [
        'google', 'twitter', 'googledevs'
    ]

    def __init__(self):
        self.login('benscstutorials')
        self.like_comment_by_hashtag('technology')
        self.comment_on_account()

    def login(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.send_keys(pw)
        submit_btn = self.driver.find_element_by_xpath(
            "//button[@type='submit']")
        submit_btn.click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            pass

    def comment_on_account(self):
        for account in self.accounts:
            # get to profile page
            self.driver.get('https://www.instagram.com/{}/'.format(account))
            # get most recent photo
            links = self.driver.find_elements_by_tag_name('a')

            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            last_photo_url = valid_links[0].get_attribute('href')
            self.driver.get(last_photo_url)
            # comment on the photo
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0, 1)])
            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[@type='submit']").click()
            sleep(2)

    def like_comment_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath(
            "//input[@placeholder='Search']")
        search_box.send_keys('#'+hashtag)
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').send_keys(Keys.ENTER)
        sleep(5)

        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)

            # like
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/section[1]/span[1]/button').click()
            sleep(3)

            # comment
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0, 8)])
            sleep(2)
            self.driver.find_element_by_xpath(
                "//button[@type='submit']").click()
            sleep(2)


def main():
    my_bot = Bot()


if __name__ == '__main__':
    main()
