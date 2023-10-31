import logging
import platform

from app import create_application

if __name__ == '__main__':
    application = create_application()
    logging.info(f"lee7s-group-bot start with {platform.system()}\n\n")
    application.run_polling()



