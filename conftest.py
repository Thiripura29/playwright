import pytest
import os

# from playwright.async_api import Playwright

PASSWORD = os.environ['PASSWORD']


@pytest.fixture
def set_up(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")

    yield page


@pytest.fixture
def login_set_up(set_up):
    page = set_up
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_label("Password").press("Enter")

    yield page


@pytest.fixture
def go_to_newpage(page):
    page.goto("/shop")
    page.wait_for_load_state("networkidle")

    yield page
