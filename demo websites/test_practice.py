from playwright.sync_api import Page, expect
def test_practice(page: Page)  -> None:

    page.goto(
            "https://practicetestautomation.com/practice-test-login/",
            wait_until="commit",
            timeout=30000
    )

    expect(page).to_have_title(
         "Test login"
        )

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    expect(
        page.get_by_role("heading", name="Logged In Successfully")
    ).to_be_visible()

    # 7. Verify success message
    expect(
        page.get_by_text("Congratulations student")
    ).to_be_visible()