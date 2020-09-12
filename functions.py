import hashlib
from decorators import *


@param_log_decorator('files/log.txt')
def hash_generator(path: str = 'files/file.txt'):
    with open(path, encoding='utf-8') as f:
        for line in f:
            hash_line = hashlib.md5(bytes(line.rstrip(), encoding='utf-8'))
            yield hash_line.hexdigest()


if __name__ == '__main__':
    generator = hash_generator()
    for item in generator:
        print(item)
