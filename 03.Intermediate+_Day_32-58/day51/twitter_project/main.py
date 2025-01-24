from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.promised_down = 100
        self.promised_up = 10
        self.driver = webdriver.Firefox()

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(5)
        go = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go.click()
        time.sleep(60)

        down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        print(f"down: {down.text}")
        print(f"up: {up.text}")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        signin = self.driver.find_element(By.CSS_SELECTOR, "a.css-175oi2r:nth-child(2)")
        signin.click()
        time.sleep(15)
        email_input = self.driver.find_element(By.CSS_SELECTOR, ".r-30o5oe")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        password_input = self.driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        post = self.driver.find_element(By.CSS_SELECTOR, ".r-1fkl15p")
        post.click()
        time.sleep(5)
        # todo it worked until here, need to figure out how to make it work
        tweet = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet.send_keys("test")

        # post = self.driver.find_element(By.XPATH, "html body div#react-root div.css-175oi2r.r-13awgt0.r-12vffkv div.css-175oi2r.r-13awgt0.r-12vffkv div#layers.r-zchlnj.r-1d2f490.r-u8s1d.r-ipm5af div.css-175oi2r.r-aqfbo4.r-zchlnj.r-1d2f490.r-1xcajam.r-12vffkv div.css-175oi2r.r-12vffkv div.css-175oi2r.r-12vffkv div.css-175oi2r.r-1p0dtai.r-1adg3ll.r-1d2f490.r-bnwqim.r-zchlnj.r-ipm5af div.r-1oszu61.r-1niwhzg.r-vqxq0j.r-deolkf.r-1mlwlqe.r-eqz5dr.r-1ebb2ja.r-crgep1.r-ifefl9.r-bcqeeo.r-t60dpp.r-13wfysu.r-417010.r-1p0dtai.r-1adg3ll.r-1d2f490.r-bnwqim.r-zchlnj.r-ipm5af div.css-175oi2r.r-1pz39u2.r-16y2uox.r-1wbh5a2 div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1habvwh div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-rsyp9y.r-1pjcn9w.r-1potc6q div.css-175oi2r.r-kemksi.r-16y2uox.r-1867qdf.r-1wbh5a2 div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-f8sm7e.r-13qz1uu.r-1ye8kvj div.css-175oi2r.r-dq6lxq.r-hucgq0.r-16y2uox.r-1wbh5a2.r-1dqxon3 div.css-175oi2r div.css-175oi2r.r-1h8ys4a.r-dq6lxq.r-hucgq0 div div.css-175oi2r div.css-175oi2r div.css-175oi2r.r-3pj75a div.css-175oi2r.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c div div.css-175oi2r div.css-175oi2r.r-1awozwy.r-kemksi.r-18u37iz.r-1wtj0ep.r-13qz1uu.r-184en5c div.css-175oi2r.r-1awozwy.r-18u37iz.r-knv0ih button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        # post.click()

twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
