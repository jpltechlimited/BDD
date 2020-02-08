import time

from src.d365.d365Client import D365Client


def before_all(context):
    context.d365Client = D365Client(True)


def after_all(context):
    time.sleep(10)
    context.d365Client.dispose()
