from playwright.sync_api import Page, expect
def test_toolsqa(page: Page) :
    page.goto(
        "https://demoqa.com/text-box",
        wait_until="commit",
        timeout=30000
    )

    expect (page).to_have_title("ToolsQA")
    page.get_by_placeholder("fullName").fill("John Doe  ")