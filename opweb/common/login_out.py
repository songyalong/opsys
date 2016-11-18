# coding:utf-8
import functools


def is_login(request):
    def decro_is_login(func):
        @functools.wraps(func)
        def wraps(*args, **keyvalues):
            print "session"
            return func(*args, **keyvalues)

        return wraps

    return decro_is_login
