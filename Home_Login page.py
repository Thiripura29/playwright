import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    with page.expect_popup() as page1_info:
        page.get_by_label("Sign Up").click()
    page1 = page1_info.value
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Test@1234")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.locator("#comp-kqx72yrn1").click()
    print("Hi Thiripura")
    page1.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
