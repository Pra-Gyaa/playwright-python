# # import re
# # # from playwright.sync_api import Page, expect


#  def test_hrm(page: Page) -> None:
#     # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     # page.get_by_role("textbox", name="Username").fill("Admin")
#     # page.get_by_role("textbox", name="Password").click()
#     # page.get_by_role("textbox", name="Password").fill("admin123")
#     # page.get_by_role("button", name="Login").click()
#     # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
#     # page.get_by_role("listitem").filter(has_text="Test 5 user").locator("i").click()
#     # # page.get_by_role("menuitem", name="Logout").click()
#     # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")





from playwright.sync_api import Page, expect


def test_hrm(page: Page) -> None:

    # Open OrangeHRM login page
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    # Enter username
    page.get_by_role("textbox", name="Username").fill("Admin")

    # Enter password
    page.get_by_role("textbox", name="Password").fill("admin123")

    # Click Login
    page.get_by_role("button", name="Login").click()

    # Verify Dashboard is displayed
    expect(
        page.get_by_role("heading", name="Dashboard")
    ).to_be_visible()

    print("Login successful!")

    # Click user profile dropdown
    page.locator(".oxd-userdropdown-tab").click()

    # Click Logout
    page.get_by_role("menuitem", name="Logout").click()

    # Verify login page is displayed
    expect(
        page.get_by_role("textbox", name="Username")
    ).to_be_visible()

    print("Logout successful!")