from setup.setup import Setting

from screenshot.screenshots import Screenshot


setting = Setting("Visual regression test")


screenshot = Screenshot()


class TestRegression:

    def test_should_take_screenshots(self):
        setting.setUp()

        driver = setting.driver

        driver.get("https://ecommerce-playground.lambdatest.io/")

        screenshot.take_screenshot(driver)

        setting.tearDown()


TestRegression().test_should_take_screenshots()
