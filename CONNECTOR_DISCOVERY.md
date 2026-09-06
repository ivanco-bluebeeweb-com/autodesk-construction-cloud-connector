# Autodesk Construction Cloud (BIM 360) Connector — Connector Discovery

**Category:** C47. Construction & Field Service Management  
**Vendor:** Autodesk Construction Cloud (BIM 360)  
**Official Website:** https://construction.autodesk.com

## 1. Официальный API
- **Базовый URL API:** `https://developer.api.autodesk.com/construction/v1`
- **Поддерживаемая модель авторизации:** Autodesk 3-Legged / 2-Legged OAuth (Bearer token)

## 2. Архитектура сущностей
- Ключевые ресурсы платформы Autodesk Construction Cloud (BIM 360):
  - проекты (/projects)
  - замечания/коллизии (/issues)
  - документы/модели (/checklists)
  - спецификации

## 3. Требования к отказоустойчивости и безопасности
- Соблюдение вендорных лимитов запросов (Rate Limiting) с экспоненциальной задержкой.
- Строгая валидация Pydantic-схем на входе и выходе каждого запроса.
- Тестовая точка проверки подключения: `GET /construction/v1/projects`.
