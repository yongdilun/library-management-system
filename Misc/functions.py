import hashlib, binascii
import re
import timeago, datetime
from werkzeug.security import check_password_hash, generate_password_hash

salt=b'$#0x--.\'/\\98'
LEGACY_PASSWORD_HASH = "025db420560617303c2ba988d050ec62562343bc0fb0358d31d2f0bae8dbede8"


def legacy_hash(string):
    """Return the original project hash so old seed accounts can still be verified."""
    dk = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)
    return binascii.hexlify(dk).decode("utf-8")


def hash_password(string):
    return generate_password_hash(str(string), method="pbkdf2:sha256", salt_length=16)


def verify_password(stored_hash, candidate):
    if not stored_hash or candidate is None:
        return False

    candidate = str(candidate)
    if stored_hash == LEGACY_PASSWORD_HASH:
        return candidate == "password"

    try:
        return check_password_hash(stored_hash, candidate)
    except ValueError:
        return False


def hash(string):
    return hash_password(string)


def b_hash(string):
    return hash_password(string).encode("utf-8")


def clean_text(value):
    return str(value or "").strip()


def valid_email(value):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", clean_text(value)) is not None
    
def ago(date):
    """
        Calculate a '3 hours ago' type string from a python datetime.
    """
    now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

    return (timeago.format(date, now)) # will print x secs/hours/minutes ago
