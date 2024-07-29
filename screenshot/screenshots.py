import os

from compare.compare import CompareImages

from setup.setup import Setting

from dotenv import load_dotenv

load_dotenv(".env")

setting = Setting("Visual regression test")

EXEC_PLATFORM = os.getenv("EXEC_PLATFORM")

compare = CompareImages()

# Define file paths
baseline_path = "baseline_screenshot.png"
current_path = "current_screenshot.png"
diff_path = "diff_screenshot.png"


class Screenshot:

    def take_screenshot(self, driver):
        if EXEC_PLATFORM == "local":
            driver.save_screenshot(current_path)

            if not os.path.exists(baseline_path):
                print(
                    "Baseline image not found. Saving current screenshot as baseline."
                )
                os.rename(current_path, baseline_path)
            else:
                # Compare current screenshot with baseline
                if compare.compare_images(baseline_path, current_path, diff_path):
                    print("No visual changes detected.")
                else:
                    print(f"Visual changes detected! Saved at {diff_path}")
        elif EXEC_PLATFORM == "cloud":
            driver.execute_script("smartui.takeScreenshot", setting.config)
