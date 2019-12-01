from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from robot.api import logger
from robot.utils import get_link_path


class CreateWebDriver:
    def __init__(cls,outputdir,browser,url):
        '''
        Instantiate a webdriver and go to the URL
        :param outputdir:  The Log Folder
        :param browser: The browser on the which the test needs to run
        :param url: Test URL
        '''
        cls.outputdir = outputdir
        cls.count = 0
        cls.Initialize(browser)
        cls.Go_to_url(url)

    def Initialize(cls,browser):
        '''
        Method that initialize the webdriver
        :param browser: Browser Info
        :return:
        '''
        if browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == "firefox":
            cls.driver = webdriver.Firefox()
        elif browser == "safari":
            cls.driver = webdriver.Safari()
        return cls


    def Go_to_url(cls,url):
        '''
        browse the URL
        :param url: URL to be browsed
        :return:
        '''
        cls.driver.get(url)
        return cls


    def capture_screenshot(cls):
        '''
        Taking screenshots and attaching the screenshot to the
        Robot Report
        :return:
        '''
        cls.count+=1
        cls.driver.get_screenshot_as_file(cls.outputdir+ "/" + "screenshot-{}.png".format(cls.count))
        cls._embed_screenshot(cls.outputdir+ "/" + "screenshot-{}.png".format(cls.count))
        cls._link_screenshot(cls.outputdir+ "/" + "screenshot-{}.png".format(cls.count))
        return cls

    def browser_quit(cls):
        '''
        Closing the Browser as a part of Teardown
        :return:
        '''
        cls.driver.close()

    def browser_go_back(cls):
        '''
        Browser action to go back to the Last Page
        :return:
        '''
        cls.driver.execute_script("window.history.go(-1)")
        return cls

    def get_tilte_of_page(cls):
        '''
        Get The Title of the page
        :return:
        '''
        title  = cls.driver.title
        return title

    def switch_to_tab(cls):
        '''
        Switch to the Latest opened window in the browser Instance
        :return:
        '''
        handle = cls.driver.window_handles
        if handle:
            cls.driver.switch_to.window(handle[-1])
            return cls
        else:
            logger.error("No window handle to be selected")



    def get_status_of_page(cls,url):
        '''
        INCOMPLETE API,
        The API helps to get the status code of the Page
        :param url:
        :return:
        '''
        JS = "fetch(new Request('{}')).then(function(response) {{console.log(response.status);response.blob().then(function(myBlob) {{var objectURL = URL.createObjectURL(myBlob); document.querySelector('href').src = objectURL;}});}});".format(url)
        print(JS)
        Stats=  cls.driver.execute_async_script(JS)
        status_code = cls.driver.execute_script(JS)
        return Stats,status_code



    #support Function(Please dont Edit)
    def _embed_screenshot(cls, path, width=100):
        '''Support functions to edit the robot Logger to add screenshot from the Selenium-Python
        :param path:
        '''
        link = get_link_path(path, cls.outputdir)
        logger.info('<a href="%s"><img src="%s" width="%s"></a>'
                    % (link, link, width), html=True)

    def _link_screenshot(cls, path):
        '''Support functions to edit the robot Logger to add screenshot from the Selenium-Python
        :param path:
        '''
        link = get_link_path(path, cls.outputdir)
        logger.info("Screenshot saved to '<a href=\"%s\">%s</a>'."
                    % (link, path), html=True)











