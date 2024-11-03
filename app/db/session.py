from django.db import connections


def get_db_connection(alias="default"):
    connection = connections[alias]
    return connection
