import pytest

class Base_Test:
    @pytest.fixture(autouse=True)
    def init_website(self,setup):
        self.driver=setup
        self.driver.get("https://automationexercise.com/")