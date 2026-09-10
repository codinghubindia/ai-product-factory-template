import os, sys, shutil, argparse

def create_release_archive(source_dir, output_zip_path):
    if not os.path.exists(source_dir):
        print(f'[ERROR] Source dir does not exist: {source_dir}')
        return False
    base_name = os.path.splitext(output_zip_path)[0]
    result_path = shutil.make_archive(base_name, 'zip', source_dir)
    print(f'[ARCHIVE BUILDER] Created package archive: {result_path}')
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    create_release_archive(args.source, args.output)
