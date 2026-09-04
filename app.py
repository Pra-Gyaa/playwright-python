from playwright.sync_api import sync_playwright

print("Script started")

with sync_playwright() as p:
    print("Launching browser...")

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://playwright.dev/python/")

    print("Page title:", page.title())

    page.wait_for_timeout(5000)

    browser.close()

print("Script finished")