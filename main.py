import pandas as pd
from pathlib import Path
import re


SEPARATOR = ' > '


def log_to_csv(path):
    with path.open() as f:
        data = f.readlines()
    data = filter(lambda x: not re.match(r'^\s*$', x), data)
    data = filter(lambda x: not re.match(r'^Logging.*', x), data)
    return ''.join(data)


def prepend_header(data):
    return 'timestamp' + SEPARATOR + 'key\n' + data


def save(path, item):
    with path.open('w') as f:
        f.write(item)


def main():
    csv = log_to_csv(Path('logkeys.log'))
    csv = prepend_header(csv)
    save(Path('logkeys.csv'), csv)

    df = pd.read_csv(Path('logkeys.csv'), sep=SEPARATOR, engine='python')
    print(df)
    print(df['key'].value_counts().head(50))


if __name__ == '__main__':
    main()
