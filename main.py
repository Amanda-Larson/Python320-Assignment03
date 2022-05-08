"""
# Title: main driver for a simple social network project
# Who: ALarson
# What/When: 4/24/2022 - started assignment
"""
import csv

import user_status
import users
import socialnetworkmodel as sn
from loguru import logger
import pysnooper


def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    user = users.UserCollection
    return user


def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    status = user_status.UserStatusCollection
    return status


# @pysnooper.snoop
def load_users(filename):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    """
    users.UserCollection.db_connect()
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            file_users = csv.DictReader(file)
            for row in file_users:
                try:
                    with sn.db.transaction():
                        new_user = users.UserCollection.create(
                            user_id=row['USER_ID'],
                            email=row['EMAIL'],
                            user_name=row['NAME'],
                            user_last_name=row['LASTNAME'])
                        new_user.save()
                        logger.info('Got to here')

                except Exception as e:
                    logger.info(f'Error creating user')
                    logger.info(e)
    except FileNotFoundError:
        print('File not found')


def load_status_updates(filename):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """

    user_status.UserStatusCollection.db_connect()
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            file_status = csv.DictReader(file)
            for row in file_status:
                try:
                    with sn.db.transaction():
                        new_status = user_status.UserStatusCollection.create(
                            user_id=row['USER_ID'],
                            status_id=row['STATUS_ID'],
                            status_text=row['STATUS_TEXT'])
                        new_status.save()
                        logger.info('Got to here')

                except Exception as e:
                    logger.info('Error creating status')
                    logger.info(e)
    except FileNotFoundError:
        print('File not found')


def add_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    new_user = user_collection.add_user(user_id, email, user_name, user_last_name)
    user_collection.save()
    return new_user


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    updated_user = user_collection.modify_user(user_id, email, user_name, user_last_name)
    user_collection.save()
    return updated_user


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    del_user = user_collection.delete_user(user_id)
    user_collection.save()
    return del_user


def search_user(user_id, user_collection):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    find_user = user_collection.search_user(user_id)
    return find_user


def add_status(status_id, user_id, status_text, status_collection):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    add_new_status = status_collection.add_status(status_id, user_id, status_text)
    return add_new_status


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    updated_status = status_collection.modify_status(status_id, user_id, status_text)
    return updated_status


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    del_status = status_collection.delete_status(status_id)
    return del_status


def search_status(status_id, status_collection):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    find_status = status_collection.search_status(status_id)
    return find_status
