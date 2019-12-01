from helpers.CreateWebDriver import CreateWebDriver
from selenium.webdriver.common.keys import Keys
from robot.api import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Blog(CreateWebDriver):
    def __init__(self,output,browser,url):
        super().__init__(output,browser,url)

    '''
    XPATH INFO
    Can be moved outsid of this function
    But currently for the ease of development 
    i am using it here
    '''
    selectors= {
        "header"                 : "//*[@title='Go to Lambda']/h1",
        "txt"                    :"//*[@class='collectionHeader-nameAndDescription']/h2",
        "header_link_list"       :"//*[contains(text(),'{}')]",
        "header_meata_content"   : "/html/head/title",
        "github"                 :"//*[contains(text(),'Open Source')]",
        "twitter"                :"//*[contains(@title, 'Visit “Lambda” on Twitter')]",
        "search_tab"             :"//*[@title='Search Lambda']",
        "href"                   :"//*[contains(@data-source,'collection_home')]/div/a",
        "href_text"              :"//*[contains(@data-source,'collection_home')]/div/a/span"
    }


    def click_header(self):
        logger.info("Clicking on the header of the page")
        try:
            z = self.driver.find_element_by_xpath(self.selectors["header"])
            z.click()
        except:
            logger.error("Unable to find the Element")
        return self

    def get_header_txt(self):
        value = self.driver.find_element_by_xpath(self.selectors["txt"]).text
        logger.info("The Header Text is : {}".format(value))
        return value


    def click_header_links(self,link):
        logger.info("Clicking on the header links of the page")
        try:
            el = self.driver.find_element_by_xpath(self.selectors["header_link_list"].format(link))
            el.click()
        except:
            logger.error("Unable to find the Element")
        return self


    def click_github(self):
        logger.info("Clicking on the GitHub link on the page")
        try:
            el = self.driver.find_element_by_xpath(self.selectors["github"])
            el.click()
        except:
            logger.error("Unable to find the Element")
        return self

    def click_twitter(self):
        logger.info("Clicking on the Twitter link on the page")
        try:
            el = self.driver.find_element_by_xpath(self.selectors["twitter"])
            el.click()
        except:
            logger.error("Unable to find the Element")
        return self

    def input_search_tab(self,what_you_want_to_search):
        logger.info("Inputting {} into the search Tab".format(what_you_want_to_search))
        el = self.driver.find_element_by_xpath(self.selectors["search_tab"])
        el.send_keys(what_you_want_to_search)
        logger.info("Clicking Enter")
        el.send_keys(Keys.ENTER)
        return self

    def find_all_links_on_page(self):
        lis = {}
        logger.info("Getting all the Href links & the Text aligned for the Blogs")
        el = self.driver.find_elements_by_xpath(self.selectors["href"])
        for j in range(len(el)):
            lis[el[j].get_attribute("href")]= el[j].text[0:20]
        return lis







