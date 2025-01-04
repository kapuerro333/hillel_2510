"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
@pytest.mark.parametrize("username, status, expected_message", [
    ("Yurii", "success", "Login event - Username: Yurii, Status: success"),
    ("Yurii", "expired", "Login event - Username: Yurii, Status: expired"),
    ("Yurii", "failed", "Login event - Username: Yurii, Status: failed"),
])
def test_log_event(username, status, expected_message):
    log_event(username, status)

    with open('login_system.log', 'r') as file:
        log_contents = file.readlines()

    assert any(expected_message in line for line in log_contents)