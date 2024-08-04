import time

from playwright.sync_api import Playwright, sync_playwright, expect
from Elements.Homepage1 import homepage
import pytest
@pytest.mark.integration
def test_run(set_up):
    page=set_up
    page.wait_for_load_state("networkidle")
    home_page=homepage(page)
    expect(home_page.celebrate_body).to_be_visible()
    expect(home_page.celebrate_header).to_be_visible()