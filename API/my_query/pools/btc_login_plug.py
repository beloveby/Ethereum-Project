# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 22:32
# @Author  : Yuan Bian
# @File    : btc_login_plug.py
import os
import requests
from time import sleep
from selenium import webdriver
from pools.constants import ROOT_PATH


class BtcLoginPlug:
    url = "https://i.btc.com/"
    path = ROOT_PATH

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        req = requests.Session()
        req.headers.clear()
        wd = webdriver.Chrome()
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        wd.get(self.url)
        wd.find_element_by_name('email').send_keys(self.username)
        wd.find_element_by_xpath(
            '//*[@class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored"]').click()
        wd.find_element_by_name('password').send_keys(self.password)
        wd.find_element_by_xpath(
            '//*[@class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored"]').click()


