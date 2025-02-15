from setup.setup import Setting

setting = Setting("Visual regression test")


class SmartuiScreenshot:
    def smartui_screenshot(self, driver):

        try:
            driver.execute_script("lambda-status=passed")
            return driver.execute_script("smartui.takeScreenshot", setting.config)
        except Exception as error:
            driver.execute_script("lambda-status=failed")
            return f"{error}, an error occured"
