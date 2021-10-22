import os
import pandas as pd

path_to_files = '../../counts/'

df_dict = {
    'participant': [],
    'file_name': [],
    'source': [],
    'count': [],
    'type': []
}


with open(os.path.join(path_to_files, 'fitbit_csv_counts.txt'), 'r') as f:
    for line in f.readlines():
        _, count, fp_raw = line.split(' ')
        pt, src, fname = fp_raw.strip().split('/')

        df_dict['participant'].append(pt)
        df_dict['file_name'].append(fname)
        df_dict['source'].append(src)
        df_dict['count'].append(int(count))
        df_dict['type'].append('.csv')

with open(os.path.join(path_to_files, 'pmsys_csv_counts.txt'), 'r') as f:
    for line in f.readlines():
        _, count, fp_raw = line.split(' ')
        pt, src, fname = fp_raw.strip().split('/')

        df_dict['participant'].append(pt)
        df_dict['file_name'].append(fname)
        df_dict['source'].append(src)
        df_dict['count'].append(int(count))
        df_dict['type'].append('.csv')


with open(os.path.join(path_to_files, 'json_counts_fitbit.txt'), 'r') as f:
    for line in f.readlines():
        fp_raw, count = line.strip().split(': ')
        pt, src, fname = fp_raw.split('/')

        df_dict['participant'].append(pt)
        df_dict['file_name'].append(fname)
        df_dict['source'].append(src)
        df_dict['count'].append(int(count))
        df_dict['type'].append('.csv')


df = pd.DataFrame(df_dict)
df.to_excel('counts_formatted.xlsx', index=False, header=True)
