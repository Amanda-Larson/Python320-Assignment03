"""
Classes for user information for the social network project
"""
# pylint: disable=R0903

from loguru import logger
import peewee as pw
import socialnetworkmodel as sn
import users

logger.info("Let's get to debugging users.py")
logger.add("users_and_status.log", backtrace=True, diagnose=True)


class UserCollection(sn.BaseModel):
    """
    Contains a collection of Users
    """

    logger.info("notice peewee data type")

    user_id = pw.CharField(primary_key=True, max_length=30, constraints=[pw.Check("LENGTH(user_id) < 30")])
    user_name = pw.CharField(max_length=30)
    user_last_name = pw.CharField(max_length=100)
    email = pw.CharField()

    @staticmethod
    def db_connect():
        logger.info("Set up the database.")
        sn.db.connect()
        # sn.db.execute_sql('PRAGMA foreign_keys = ON;')
        sn.db.create_tables([UserCollection])
        logger.info('db is connected, UserCollection table is created')

    @staticmethod
    def add_user(user_id, email, user_name, user_last_name):
        """
        Adds a new user to the collection
        """
        try:
            new_user = UserCollection.create(user_id=user_id,
                                             email=email,
                                             user_name=user_name,
                                             user_last_name=user_last_name)
            new_user.save()
            return True
        except pw.IntegrityError as e:
            logger.info(e)
            return False


    @staticmethod
    def modify_user(user_id, email, user_name, user_last_name):
        """
        Modifies an existing user
        """
        if user_id not in [UserCollection]:
            logger.info(f'{user_id} not in the database')
            return False
        UserCollection.email = email
        UserCollection.user_name = user_name
        UserCollection.user_last_name = user_last_name
        return True

    @staticmethod
    def delete_user(user_id):
        """
        Deletes an existing user
        """
        del_user = users.UserCollection.select().where(users.UserCollection.user_id == user_id).get()
        del_user.delete_instance()
        return del_user

        del_user = users.UserCollection.select().where(users.UserCollection.user_id == user_id).get()
        del_user.delete_instance()
        return del_user

    @staticmethod
    def search_user(user_id):
        """
        Searches for user data
        """
        # try:
        #     if UserCollection.user_id not in UserCollection:
        #         logger.info(f'{user_id} not in the database')
        #         return None
        # except pw.DoesNotExist as e:
        #     logger.info(e)
        # user_search = UserCollection.get(UserCollection.user_id == user_id)
        # return user_search
        try:
            find_user = users.UserCollection.select().where(users.UserCollection.user_id == user_id).get()
            return find_user
        except pw.DoesNotExist:
            # logger.info(e)
            print('User does not exist, please try again.')