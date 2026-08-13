from playwright.sync_api import Page, expect


def test_youtube_search(page: Page):

    page.goto(
        "https://www.youtube.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    search_box = page.locator('input[name="search_query"]')

    expect(search_box).to_be_visible(timeout=3000000)

    search_box.fill("Nepali songs 2026")

    search_box.press("Enter")

    page.wait_for_timeout(5000)

    print("Current URL:", page.url)

    assert "search_query=" in page.url