import sys
import string
from multiprocessing import Pool


def file_read(path: str) -> str:
    f = open(path, "r", encoding="utf-8")
    text = f.read()
    f.close()
    return text


def text_fix(text: str) -> list:
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    return text


def search(key: str, path: str) -> None:
    text = file_read(path)
    text = text_fix(text)
    if key in text:
        print(f'"{key}" найден в {path}')
    else:
        print(f'"{key}" не найден в {path}')
    return None


def main() -> None:
    data = sys.argv[1:]
    key = data[0].lower()
    paths = data[1:]
    key = [key] * len(paths)
    with Pool(4) as p:
        p.starmap(search, zip(key, paths))    
    
    return None


if __name__ == "__main__":

    main()