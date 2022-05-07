"""social network database model"""

import peewee as pw
from loguru import logger
import os


file = 'social_network.db'
if os.path.exists(file):
    os.remove(file)

db = pw.SqliteDatabase(file)


class BaseModel(pw.Model):
    logger.info("allows database to be defined or changed in one place")

    class Meta:
        database = db

    @staticmethod
    def main():
        db.connect()
        db.execute_sql('PRAGMA foreign_keys = ON;')
        db.create_tables([users.UserTable, user_status.UserStatusTable])


