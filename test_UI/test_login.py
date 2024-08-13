import os

import pytest
from playwright.sync_api import expect

from Elements.Homepage1 import homepage

PASSWORD = os.environ['PASSWORD']


# import utils.secret_config
# try:
#   PASSWORD=os.environ['PASSWORD']
# except KeyError:
#   import utils.secret_config
#   PASSWORD=utils.secret_config.PASSWORD

@pytest.mark.regression
# @pytest.mark.parametrize("email",["thiripura29@gmail.com",
#                              pytest.param("thiripura30@gmail.com",marks=pytest.mark.xfail),
#                                pytest.param("thiripura31@gmail.com",marks=pytest.mark.xfail)])
# @pytest.mark.parametrize("passwrd",["Test@1234",
#                                          pytest.param("Test@123",marks=pytest.mark.xfail),
#                                        pytest.param("Test@124",marks=pytest.mark.xfail)])
def test_logged_user_can_view_orders(login_set_up):
    page = login_set_up
    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")
    page.get_by_label("thiripura29 account menu").click()
    page.get_by_role("link", name="My Orders").click()
    page.wait_for_load_state("networkidle")
    expect(page.locator("text=My Orders")).to_be_visible()
    print("Hello Thiripura!!")


def test_logged_user_can_view_newpage(go_to_newpage):
    page = go_to_newpage
    # expect(page.)
    print("Hello Thiripura!!")


@pytest.mark.smoke
@pytest.mark.xfail(reason="URL Not ready")
def test_login3(set_up):
    page = set_up

    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    # page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_label("Password").press("Enter")
    page.wait_for_load_state("networkidle")

    # Every test should have assertions at the end of it

    # page.pause()
    # alllinks=page.get_by_role("link").all()
    # for link in alllinks:
    #  if '$85' in link.text_content():
    #   print("$85 present")
    #   assert 'socks' not in link.text_content().lower()
    print("Hello Thiripura!!")


@pytest.mark.regression
def test_login4(set_up):
    page = set_up
    # it takes sometimes whole page to be loaded and to perform action . So we need to add wait_for_load_state()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("thiripura29@gmail.com")
    page.get_by_label("Password").click()
    # page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(PASSWORD)
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


@pytest.mark.integration
def test_run(login_set_up):
    page = login_set_up
    page.wait_for_load_state("networkidle")
    home_page = homepage(page)
    expect(home_page.celebrate_body).to_be_visible()
    expect(home_page.celebrate_header).to_be_visible()
