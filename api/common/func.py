import hashlib, hmac
from spbhackgtcase3 import settings


def Hash(password):
    password = hmac.new(settings.SALT.encode('UTF-8'), password.encode('UTF-8'), hashlib.sha512)
    return (password.hexdigest())
