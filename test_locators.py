import re
from playwright.sync_api import Page, expect

def test_locator(page: Page) -> None:

    page.goto("https://playwright.dev/python/")

    expect(page).to_have_title(
        re.compile("Playwright", re.IGNORECASE)
    )

    page.wait_for_timeout(3000)