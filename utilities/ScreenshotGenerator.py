import os
# from datetime import datetime

class Screenshot:

    @staticmethod
    def take_screenshot(driver,test_name):
        base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir=os.path.join(base_dir,'screenshots')

        os.makedirs(screenshot_dir,exist_ok=True)

        file_name=f"{test_name}.png"
        file_path=os.path.join(screenshot_dir,file_name)

        driver.save_screenshot(file_path)

        # return file_path



