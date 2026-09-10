import os, sys, subprocess, argparse

def run_software_tests(project_dir, test_cmd=None):
    if not os.path.exists(project_dir):
        print(f'[ERROR] Project directory not found: {project_dir}')
        return False
    if not test_cmd:
        if os.path.exists(os.path.join(project_dir, 'package.json')):
            test_cmd = 'npm test'
        elif os.path.exists(os.path.join(project_dir, 'pyproject.toml')) or os.path.exists(os.path.join(project_dir, 'requirements.txt')):
            test_cmd = 'pytest'
        else:
            print('[SOFTWARE QA] No automated test runner specified or detected')
            return False
    print(f'[SOFTWARE QA] Executing: {test_cmd} in {project_dir}')
    res = subprocess.run(test_cmd, shell=True, cwd=project_dir)
    return (res.returncode == 0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True)
    parser.add_argument('--cmd', default=None)
    args = parser.parse_args()
    run_software_tests(args.dir, args.cmd)
