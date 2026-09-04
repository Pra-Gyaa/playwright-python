import re
from playwright.sync_api import expect

def test_google_search(page):
    print("Opening Google...")

    page.goto("https://www.google.com")
    print("Google opened")

    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
        print("Cookie popup accepted")
    except:
        print("No popup")

    print("Typing search...")
    page.get_by_role("combobox", name="Search").fill("Playwright python")

    print("Pressing Enter...")
    page.keyboard.press("Enter")

    print("Waiting for title...")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))

    print("✅ Test Passed")