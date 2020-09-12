from datetime import datetime


def log_decorator(function):
    path = 'files/log_file.txt'

    def decorator(*args, **kwargs):
        response = function(*args, **kwargs)
        now = datetime.now()
        log_string = f'{str(now)} {function.__name__} {args} {kwargs}\n'
        with open(path, 'a', encoding='utf-8') as f:
            f.write(log_string)
        return response
    return decorator


def param_log_decorator(path: str):
    def _log_decorator(function):
        def decorator(*args, **kwargs):
            response = function(*args, **kwargs)
            now = datetime.now()
            log_string = f'{str(now)} {function.__name__} {args} {kwargs}\n'
            with open(path, 'a', encoding='utf-8') as f:
                f.write(log_string)
            return response
        return decorator
    return _log_decorator
