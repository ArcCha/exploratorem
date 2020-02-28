import pandas as pd
from pathlib import Path
import re


data_path = Path('logkeys.log')
csv_path = Path('logkeys.csv')

with data_path.open() as f:
    data = f.readlines()
data = filter(lambda x: not re.match(r'^\s*$', x), data)
data = filter(lambda x: not re.match(r'^Logging.*', x), data)
data = ''.join(data)
data = 'timestamp > key\n' + data
with csv_path.open('w') as f:
    f.write(str(data))

df = pd.read_csv(csv_path, sep=' > ', engine='python')
print(df)

print(df['key'].value_counts().head(50))
