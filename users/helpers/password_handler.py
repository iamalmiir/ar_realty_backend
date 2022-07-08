from passlib.hash import bcrypt


def make_password(password):
    hasher = bcrypt.using(
        rounds=16,
    )
    return hasher.hash(password)


def check_password(password, hashed_password):
    hasher = bcrypt.using(
        rounds=16,
        salt=bcrypt.gensalt(),
    )
    return hasher.verify(password, hashed_password)
