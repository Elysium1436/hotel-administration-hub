import mongoengine


def global_init():
    mongoengine.connect("default", name="jasmin_db")
