# Autodesk Construction Cloud (BIM 360) Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** Autodesk 3-Legged / 2-Legged OAuth (Bearer token)
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /construction/v1/projects`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
