import pytest
from page.auth_page import AuthPage
from playwright.sync_api import Page


@pytest.fixture()
def auth_page(page: Page) -> AuthPage:
    return AuthPage(page)
