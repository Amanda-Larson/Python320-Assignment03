"""
Classes for user information for the social network project
"""
# pylint: disable=R0903

from loguru import logger
import peewee as pw
import socialnetworkmodel as sn

logger.info("Let's get to debugging users.py")
logger.add("users_and_status.log", backtrace=True, diagnose=True)


#
# class Users(sn.BaseModel):
#     """
#     Contains user information
#     """


# def __init__(self, user_id, email, user_name, user_last_name):
#     self.user_id = user_id
#     self.user_name = user_name
#     self.user_last_name = user_last_name
#     self.email = email
#     logger.info("User class instantiated")

# def show(self):
#     """display an instance"""
#     print(self.user_id, self.user_name, self.user_last_name)
#     print(type(self.user_name))


class UserCollection(sn.BaseModel):
    """
    Contains a collection of Users objects
    """

    logger.info("notice peewee data type")

    user_id = pw.CharField(primary_key=True, max_length=30)
    user_name = pw.CharField(max_length=30)
    user_last_name = pw.CharField(max_length=100)

    @staticmethod
    def db_connect():
        logger.info("Set up the database.")
        sn.db.connect()
        sn.db.execute_sql('PRAGMA foreign_keys = ON;')
        sn.db.create_tables([UserCollection])
        logger.info('db is connected')

    @staticmethod
    def add_user(user_id, email, user_name, user_last_name):
        """
        Adds a new user to the collection
        """
        if user_id in [UserCollection]:
            logger.info("Reject new status  -  status_id already exists")
            return False
        new_user = (user_id, email, user_name, user_last_name)
        [UserCollection][0] = new_user
        return True

    @staticmethod
    def modify_user(user_id, email, user_name, user_last_name):
        """
        Modifies an existing user
        """
        if user_id not in sn.db:
            logger.info(f'{user_id} not in the database')
            return False
        sn.db[user_id].email = email
        sn.db[user_id].user_name = user_name
        sn.db[user_id].user_last_name = user_last_name
        return True


    @staticmethod
    def delete_user(user_id):
        """
        Deletes an existing user
        """
        if user_id not in self.database:
            logger.info(f'{user_id} not in the database')
            return False
        del self.database[user_id]
        return True

    @staticmethod
    def search_user(user_id):
        """
        Searches for user data
        """
        if user_id not in sn.db:
            logger.info(f'{user_id} not in the database')
            return Users(None, None, None, None)
        return self.database[user_id]