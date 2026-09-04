# from playwright.sync_api import Page, expect

# def test_youtube_search(page: Page):

#     page.goto(
#         "https://www.youtube.com/",
#         wait_until="commit",
#         timeout=30000
#     )

#     print("YouTube navigation started")

#     search_box = page.locator('input[name="search_query"]')

#     expect(search_box).to_be_visible(timeout=30000)

#     print("Search box found")

#     search_box.fill("Nepali songs 2026")
#     search_box.press("Enter")

#     page.wait_for_timeout(5000)

#     print("URL:", page.url)



from playwright.sync_api import Page, expect


def test_youtube_search(page: Page):

    # 1. Open YouTube
    page.goto(
        "https://www.youtube.com/",
        wait_until="commit",
        timeout=60000
    )

    # 2. Verify YouTube opened
    expect(page).to_have_title(
        "YouTube",
        timeout=30000
    )

    # 3. Find search box
    search_box = page.locator(
        'input[name="search_query"]'
    )

    expect(search_box).to_be_visible(
        timeout=30000
    )

    # 4. Search
    search_box.fill("Nepali songs 2026")

    # 5. Press Enter
    search_box.press("Enter")

    # 6. Wait for results
    page.wait_for_timeout(5000)

    # 7. Verify URL
    expect(page).to_have_url(
        lambda url: "search_query=" in url
    )

    # 8. Find video results
    videos = page.locator(
        "ytd-video-renderer"
    )

    expect(videos.first).to_be_visible(
        timeout=30000
    )

    # 9. Print first 5 video titles
    titles = page.locator(
        "ytd-video-renderer #video-title"
    )

    count = min(titles.count(), 5)

    for i in range(count):
        print(
            f"Video {i + 1}: "
            f"{titles.nth(i).inner_text()}"
        )

    # 10. Screenshot
    page.screenshot(
        path="screenshots/search_results.png",
        full_page=True
    )