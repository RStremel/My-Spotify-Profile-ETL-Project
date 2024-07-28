from sqlalchemy import create_engine
import pandas as pd

from utils import connect_to_database

class SpotifyLoader:
    def __init__(self) -> None:
        self.database_uri = connect_to_database(env_file_path="config/.env")

    def load_to_database(self, df: pd.DataFrame, table_name: str, if_exists: str):
        engine = create_engine(self.database_uri)

        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
        print(f"Data loaded into {table_name} table successfully.")