"""
                    === Основной файл приложения ===

                          === Версия 0.0.9 ===
"""

from storege import load_tasks, save_tasks
from view import show_menu, show_collection
from core import add_task, edit_task, delete_tasks
from config import NAME_FILE_SAVES
import app

if __name__ == "__main__":
    app.app()