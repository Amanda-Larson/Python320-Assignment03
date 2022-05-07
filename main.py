"""
# Title: main driver for a simple social network project
# Who: ALarson
# What/When: 4/24/2022 - started assignment
"""
import csv

import socialnetworkmodel
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
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
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


def save_users(user_collection):
    """
    Saves all users in user_collection into
    a database table

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    """

    for user in users.UserCollection: #This gives an error about not being iterable
        try:
            with sn.db.transaction():
                new_user = user_collection.create(
                    user_id=user[0],
                    email=user[1],
                    user_name=user[2],
                    user_last_name=user[3], )
                new_user.save()
                logger.info('Got to here')

        except Exception as e:
            logger.info(f'Error creating user = {user[0]}')
            logger.info(e)


def load_status_updates(filename, status_collection):
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
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            file_users = csv.DictReader(file)
            for row in file_users:
                status_collection.add_status(row['STATUS_ID'], row['USER_ID'],
                                             row['STATUS_TEXT'])
    except FileNotFoundError:
        print('File not found')


def save_status_updates(filename, status_collection):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    """


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
    return new_user


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    updated_user = user_collection.modify_user(user_id, email, user_name, user_last_name)
    return updated_user


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    del_user = user_collection.delete_user(user_id)
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
