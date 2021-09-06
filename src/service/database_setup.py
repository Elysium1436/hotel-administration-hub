import mongoengine


def global_init():
    mongoengine.connect(alias='core', db='jasmin_db')
