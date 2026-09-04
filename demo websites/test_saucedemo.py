from playwright.sync_api import Page, expect
def test_saucedemo(page: Page) -> None:

    # go to page

    page.goto(
            "https://www.saucedemo.com/",
            wait_until="commit",
            timeout=60000
        )

    
    # search by title

    expect(page).to_have_title(
          "Swag Labs",
          timeout=30000
      )

    page.get_by_placeholder("Username").fill("standard_user")

    # ------------------------------------------------
    # 3. Enter password
    # ------------------------------------------------
    page.get_by_placeholder("Password").fill("secret_sauce")

    # ------------------------------------------------
    # 4. Click Login
    # ------------------------------------------------
    page.get_by_role("button", name="Login").click()

    # ------------------------------------------------
    # 5. Verify Products page
    # ------------------------------------------------
    expect(page.get_by_text("Products")).to_be_visible(
        timeout=30000
    )
    page.get_by_role(
        "button",
        name="Add to cart"
    ).first.click()

    page.get_by_role("button", name="Checkout").click()

    page.get_by_placeholder("First Name").fill("abc")
    page.get_by_placeholder("Last Name").fill("xyz")
    page.get_by_placeholder("Zip/Postal Code").fill("44600")

    page.get_by_role("button", name="Continue").click()

    expect(
        page.get_by_text("Checkout: Overview")
    ).to_be_visible()

    # ------------------------------------------------
    # 13. Finish order
    # ------------------------------------------------
    page.get_by_role("button", name="Finish").click()

    # ------------------------------------------------
    # 14. Verify successful order
    # ------------------------------------------------
    expect(
        page.get_by_text("Thank you for your order!")
    ).to_be_visible()