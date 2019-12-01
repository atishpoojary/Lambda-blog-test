# from ..Resources.helpers import webDriver
from Resources.Blog import Blog


a = Blog("/Users/apoojary/PycharmProjects/WeBTest/")
a.Initialize("chrome")
a.Go_to_url("https://grofers.com/blog")
a.capture_screenshot()
a.click_header()



