import sys, shutil, subprocess

def inspect_environment():
    tools = {
        'python': shutil.which('python'),
        'node': shutil.which('node'),
        'npm': shutil.which('npm'),
        'git': shutil.which('git'),
        'pandoc': shutil.which('pandoc'),
        'curl': shutil.which('curl'),
        'tar': shutil.which('tar'),
        'powershell': shutil.which('powershell')
    }
    print('[TOOLING AUDIT] Detected Environment:')
    for t, path in tools.items():
        status = f'FOUND: {path}' if path else 'NOT FOUND'
        print(f'  - {t:12}: {status}')
    return tools

if __name__ == '__main__':
    inspect_environment()
