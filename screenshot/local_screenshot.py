import os
from compare.compare import CompareImages

compare = CompareImages()

# Define file paths
baseline_path = "baseline_screenshot.png"
current_path = "current_screenshot.png"
diff_path = "diff_screenshot.png"


class LocalScreenshot:

    def local_screenshot(self, driver):

        try:

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
        except Exception as error:
            return f"{error}, an error occured"
