from setup.setup import Setting

from screenshot.smartui_screenshot import SmartuiScreenshot

setting = Setting("Visual regression test")

screenshot = SmartuiScreenshot()


class TestLocalRegression:

    def test_should_take_screenshots(self):
        try:
            setting.setUp()

            driver = setting.driver

            driver.get("https://ecommerce-playground.lambdatest.io/")

            screenshot.take_screenshot(driver)
            setting.tearDown()
        except Exception as error:
            print(f"Failed: {error}")
            setting.tearDown()
