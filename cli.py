import argparse
import logging

# Настраиваем логирование (как мы с вами учили!)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="My Cool Tool")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    # Здесь пока пусто — команды будем добавлять в feature-ветках!

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()

if __name__ == "__main__":
    main()