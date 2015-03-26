# -*- coding: utf-8 -*-


class MongoRouther(object):

    models = ["Article"]
    database_name = "mongo"

    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to mongo_db.
        """
        if model.__name__ in self.models:
            return self.database_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to mongo_db.
        """
        if model.__name__ in self.models:
            return self.database_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1.__name__ in self.models or obj2.__name__ in self.models:
            return True
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the auth app only appears in the 'mongo_db'
        database.
        """
        if model.__name__ in self.models:
            return False
        if db == self.database_name:
            return False
        return None
