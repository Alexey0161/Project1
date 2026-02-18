import logging


def main():
    print("--- Мой Супер Проект (Project1) ---")
    print("Выберите действие:")
    print("1. Запустить копировальщик файлов")
    print("2. Запустить счетчик файлов")
    print("3. Запустить поисковик файлов")
    print("4. Запустить установщик даты в имя файла")


# Магическая проверка: запущен ли файл напрямую
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("\nПрограмма принудительно завершена пользователем.")
    except Exception as e:
        logging.error(f"Упс! Произошла непредвиденная ошибка: {e}")