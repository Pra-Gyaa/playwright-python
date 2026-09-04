from playwright.sync_api import Playwright


def test_api(playwright: Playwright):
    # Create API request context
    request = playwright.request.new_context()

    # Send GET request
    response = request.get(
        "https://jsonplaceholder.typicode.com/posts/1" , headers={"Accept": "application/json"})
    
    # Check HTTP status
    assert response.status == 200

    # Convert response to JSON
    json_data = response.json()

    # Print response
    # print("\nAPI Response:")

    # Dispose request context
    request.dispose()

    print("API test completed successfully.")
    print(json_data)

    # Validate response data
    assert json_data["x[1].first_name"] == "Harland"
    # assert "title" in json_data
    # assert "body" in json_data
    print("All API tests passed.")