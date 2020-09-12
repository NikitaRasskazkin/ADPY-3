from functions import hash_generator


if __name__ == '__main__':
    generator = hash_generator('files/text.txt')
    for item in generator:
        print(item)

