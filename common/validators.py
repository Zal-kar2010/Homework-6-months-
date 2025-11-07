# common/validators.py
from datetime import date
from rest_framework.exceptions import ValidationError

def validate_age_from_token(request):
    """
    Проверка возраста пользователя по birthdate из JWT токена.
    """
    if not request.user.is_authenticated:
        raise ValidationError("Пользователь не аутентифицирован.")

    # Берем дату рождения из токена, если есть
    birthdate_str = None
    if getattr(request, "auth", None):
        birthdate_str = request.auth.get("birthdate")

    if not birthdate_str:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    # Парсим строку в дату
    try:
        birthdate = date.fromisoformat(birthdate_str)
    except ValueError:
        raise ValidationError("Некорректная дата рождения в токене.")

    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
