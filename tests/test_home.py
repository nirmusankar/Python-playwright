from playwright.sync_api import sync_playwright, expect
import pytest
@pytest.mark.home
def test_amazon_homepage(page):
    # Navigate to Amazon
    page.goto("https://www.amazon.in")
    page.get_by_role("searchbox",name="Search Amazon.in").wait_for(state='visible',timeout=50000)
    expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    
