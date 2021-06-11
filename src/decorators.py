import functools


def login_required():
    @functools.wraps()
    def wrapped_view(**kwargs):
        pass
    return wrapped_view
