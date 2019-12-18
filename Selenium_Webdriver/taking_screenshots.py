from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
from time import sleep


class Screenshot(object):
    def __init__(self):
        self.url = "http://stackoverflow.com/"
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")   # disable the pop ups
        self.driver = webdriver.Chrome(options=chrome_options)    # creating chrome driver instance
        self.driver.get(self.url)                                 # opening the page
        sleep(2)
        self.driver.maximize_window()                             # maximizing the chrome window

    def get_screenshot(self):
        element = self.driver.find_element_by_css_selector('._glyph')  # stack overflow image
        location = element.location                             # The location of the element in the renderable canvas
        size = element.size                                     # The size of the element

        png = self.driver.get_screenshot_as_png()               # taking the screen shot of the page

        im = Image.open(BytesIO(png))                           # uses PIL library to open image in memory

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        im = im.crop((left, top, right, bottom))                 # defines crop points
        im.save('screenshot.png')                                # saves new cropped image

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    obj = Screenshot()
    obj.get_screenshot()
    obj.teardown()
