import os
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

#import utils.secret_config


@pytest.mark.smoke
def test_login(set_up):
    page =set_up

    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    #page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(os.environ['PASSWORD'])
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")

    #Every test should have assertions at the end of it
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    #page.pause()
    #alllinks=page.get_by_role("link").all()
    #for link in alllinks:
      #  if '$85' in link.text_content():
         #   print("$85 present")
         #   assert 'socks' not in link.text_content().lower()
    print("Hello Thiripura!!")

@pytest.mark.regression
#@pytest.mark.parametrize("email",["thiripura29@gmail.com",
#                              pytest.param("thiripura30@gmail.com",marks=pytest.mark.xfail),
#                                pytest.param("thiripura31@gmail.com",marks=pytest.mark.xfail)])
#@pytest.mark.parametrize("passwrd",["Test@1234",
#                                          pytest.param("Test@123",marks=pytest.mark.xfail),
#                                        pytest.param("Test@124",marks=pytest.mark.xfail)])
def test_login3(set_up):
    page =set_up
    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    #page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(os.environ['PASSWORD'])
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")

    #Every test should have assertions at the end of it
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    #page.pause()
    #alllinks=page.get_by_role("link").all()
    #for link in alllinks:
      #  if '$85' in link.text_content():
         #   print("$85 present")
         #   assert 'socks' not in link.text_content().lower()
    print("Hello Thiripura!!")

@pytest.mark.xfail(reason="URL Not ready")
def test_login1(set_up):
        page=set_up

        # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
        page.wait_for_load_state("networkidle")

        page.get_by_role("button", name="Log In").click()
        page.get_by_test_id("signUp.switchToSignUp").click()
        page.get_by_role("button", name="Log in with Email").click()
        page.get_by_test_id("emailAuth").get_by_label("Email").click()
        page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
        page.get_by_label("Password").click()
        #page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
        page.get_by_label("Password").fill(os.environ['PASSWORD'])
        page.get_by_label("Password").press("Enter")
        page.wait_for_load_state("networkidle")

        # Every test should have assertions at the end of it
        expect(page.get_by_role("button", name="Log In")).to_be_hidden()
        # page.pause()
        # alllinks=page.get_by_role("link").all()
        # for link in alllinks:
        #  if '$85' in link.text_content():
        #   print("$85 present")
        #   assert 'socks' not in link.text_content().lower()
        print("Hello Thiripura!!")

@pytest.mark.regression
def test_login2(set_up):
    page=set_up
    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    #page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(os.environ['PASSWORD'])
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")

    # Every test should have assertions at the end of it
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()
    # page.pause()
    # alllinks=page.get_by_role("link").all()
    # for link in alllinks:
    #  if '$85' in link.text_content():
    #   print("$85 present")
    #   assert 'socks' not in link.text_content().lower()
    print("Hello Thiripura!!")

