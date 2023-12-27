# __main__.py
from dotenv import load_dotenv
import uvicorn

# Загрузка переменных окружения
load_dotenv()

from .settings import settings
from .app import app

if __name__ == "__main__":
    uvicorn.run(
        'accountr.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )

