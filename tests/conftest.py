import pytest
from selenium import webdriver


#   Adding hook for command line fetching
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser_name")  # to read the browser name in command line
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="../chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="../geckodriver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver # cls.driver (Class level "to access this user self keyword") = driver (local driver)
    yield
    driver.quit()





