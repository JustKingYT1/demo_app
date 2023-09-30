from server.database.db_manager import db_manager
import settings 

db_manager.create_base(f"{settings.SCRIPTS_DIR}/base.sql")
