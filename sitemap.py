import os.path
import re
import urllib.parse

url = 'https://wiki.leanschuler.ch'


def build_sitemap():
    pattern = re.compile(r'\[(.+)\]\(([^ ]+?)( "(.+)")?\)')
    data = open('docs/_sidebar.md').read()
    sitemap = ""
    pages = 0
    for match in pattern.finditer(data):
        path = match.group(2)
        file_path = "docs" + match.group(2)
        if path.endswith('/'):
            file_path += 'README.md'
        else:
            file_path += '.md'
        if os.path.exists(file_path):
            path = urllib.parse.urljoin(url, path)
            sitemap += f'{path}\n'
            pages += 1
        else:
            print(f'Warning: {file_path} not found')
    open('docs/sitemap.txt', 'w').write(sitemap)
    print(f'Created sitemap with {pages} pages.')


build_sitemap()
