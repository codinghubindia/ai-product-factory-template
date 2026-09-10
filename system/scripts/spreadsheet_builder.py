import os, sys, csv, argparse

def generate_csv_spreadsheet(rows_dict_list, output_path):
    if not rows_dict_list:
        print('[ERROR] Empty rows data')
        return False
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    fieldnames = list(rows_dict_list[0].keys())
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_dict_list)
    print(f'[SPREADSHEET BUILDER] Generated structured CSV: {output_path}')
    return True

if __name__ == '__main__':
    print('[SPREADSHEET BUILDER] Engine ready')
