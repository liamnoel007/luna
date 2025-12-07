from playwright.sync_api import Page, expect


class AuthPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.url = "https://demo.sedmax.ru/sedmax/web/ui/login"

        self.input_login_field = page.locator("#Login")
        self.input_password_field = page.locator("#Password")
        self.enter_btn = page.get_by_test_id("submit_button")
        self.error_message = page.locator(".ant-login-alert-message")

    def open_page(self) -> None:
        self.page.goto(self.url)
        expect(self.page).to_have_title("Авторизация | SEDMAX", timeout=10000)

    def login(self, login, password) -> None:
        expect(self.input_login_field).to_be_visible(timeout=5000)
        self.input_login_field.fill(login)

        expect(self.input_password_field).to_be_visible(timeout=5000)
        self.input_password_field.fill(password)

        expect(self.enter_btn).to_be_visible(timeout=5000)
        self.enter_btn.click()

    def check_error_message(self) -> None:
        expect(self.error_message).to_be_visible(timeout=5000)

    def get_error_message(self) -> str:
        return self.error_message.inner_text()
