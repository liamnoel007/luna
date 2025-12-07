import pytest


params = [
    ("test", "test", "Неверные логин или пароль"),
    ("test2", "test2", "Неверные логин или пароль"),
    ("test3", "test3", "Неверные логин или пароль"),
]


@pytest.mark.negative
@pytest.mark.parametrize("login, password, error_message", params)
def test_auth_with_wrong_login_and_pass(
    auth_page, login, password, error_message
) -> None:

    # Открытие страницы авторизации
    auth_page.open_page()

    # Ввод логина и пароля
    auth_page.login(login, password)

    # Получение и проверка сообщения об ошибке
    auth_page.check_error_message()

    assert auth_page.get_error_message() == error_message
