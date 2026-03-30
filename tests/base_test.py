import pytest
import os

class Base_Test:
    @pytest.fixture(autouse=True)
    def init_website(self,setup,request):
        self.driver=setup
        self.driver.get("https://automationexercise.com/")
        yield
        if request.node.rep_call.failed:
            self.take_screenshot(request.node.name)

    def take_screenshot(self, test_name):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir = os.path.join(base_dir, 'screenshots')

        os.makedirs(screenshot_dir, exist_ok=True)

        file_name = f"{test_name}.png"
        file_path = os.path.join(screenshot_dir, file_name)

        self.driver.save_screenshot(file_path)

