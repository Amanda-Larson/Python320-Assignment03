"""
classes to manage the user status messages
"""
# pylint: disable=R0903
from loguru import logger
import peewee as pw
import users as u
import socialnetworkmodel as sn

logger.info("Let's get to debugging user_status/py")
logger.add("users_and_status.log", backtrace=True, diagnose=True)


class UserStatusCollection(sn.BaseModel):
    """
    Collection of UserStatus messages
    """

    logger.info("notice peewee data type")

    user_id = pw.ForeignKeyField(u.UserCollection, related_name='the user', null=False)
    status_id = pw.CharField(primary_key=True)
    status_text = pw.CharField()

    @staticmethod
    def db_connect():
        logger.info("Set up the database.")
        # sn.db.connect()
        sn.db.execute_sql('PRAGMA foreign_keys = ON;')
        sn.db.create_tables([UserStatusCollection])
        logger.info('db is connected')

    @staticmethod
    def add_status(status_id, user_id, status_text):
        """
        add a new status message to the collection
        """
        if status_id in [UserStatusCollection]:
            logger.info("Rejects new status if status_id already exists")
            return False
        new_status = (status_id, user_id, status_text)
        sn.db[status_id] = new_status
        return True

    @staticmethod
    def modify_status(status_id, user_id, status_text):
        """
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        """
        if status_id not in [UserStatusCollection]:
            logger.info("Status_id {status_id} does not exist")
            return False
        [UserStatusCollection].user_id = user_id
        [UserStatusCollection].status_text = status_text
        return True

    def delete_status(self, status_id):
        """
        deletes the status message with id, status_id
        """
        if status_id not in [UserStatusCollection]:
            logger.info(f"Failed - status ({status_id}) does not exist")
            return False
        del self.database[status_id]
        return True

    def search_status(self, status_id):
        """
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        """
        if status_id not in self.database:
            logger.info("Failed - status does not exist")
            return UserStatus(None, None, None)
            # return False
        return self.database[status_id]
