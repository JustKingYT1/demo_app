from server.database.db_manager import db_manager
import settings 


print(db_manager.create_base(script_path_tables=f"{settings.SCRIPTS_DIR}/base.sql", script_path_data=f"{settings.SCRIPTS_DIR}/data.sql"))
