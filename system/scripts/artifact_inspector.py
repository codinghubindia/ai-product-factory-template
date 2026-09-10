import os, sys, json, argparse

def inspect_artifact(file_path):
    if not os.path.exists(file_path):
        return {'file': file_path, 'exists': False, "size_bytes": 0}
    size = os.path.getsize(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    return {
        'file': file_path,
        'exists': True,
        'size_bytes': size,
        'extension': ext,
        'is_empty': (size == 0)
    }

if __name__ == '__main__':
    if len(sys.argv) > 1:
        res = inspect_artifact(sys.argv[1])
        print(json.dumps(res, indent=2))
