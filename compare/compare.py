from PIL import Image, ImageChops


class CompareImages:

    # Function to compare screenshots
    def compare_images(self, img1_path, img2_path, diff_path):
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)

        # Finding the difference
        diff = ImageChops.difference(img1, img2)

        if diff.getbbox():
            diff.save(diff_path)
            return False
        return True
