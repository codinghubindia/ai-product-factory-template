import os, sys, argparse

def generate_html_document(title, markdown_path, output_path):
    if not os.path.exists(markdown_path):
        print(f'[ERROR] File not found: {markdown_path}')
        return False
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    header = '<!DOCTYPE html><\nhtml lang="en"><\nhead><\nmeta charset="UTF-8"><\ntitle>' + title + '</title><\nstyle>body { font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; } pre { background: #edf2f7; padding: 16px; white-space: pre-wrap; hr { border: 0 solid #e2e8f0; } </style><\n/head><\nbody><\nh1>' + title + '</h1><\npre>'
    footer = '</pre><\n</body><\n</html>'
    html = header + md_text + footer

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'[DOCUMENT BUILDER] Successfully generated: {output_path}')
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    generate_html_document(args.title, args.input, args.output)
