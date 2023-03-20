import re
import urllib.parse

url = 'https://wiki.leanschuler.ch'


def build_sitemap():
    pattern = re.compile(r'\[(.+)\]\(([^ ]+?)( "(.+)")?\)')
    data = open('docs/_sidebar.md').read()
    sitemap = ""
    for match in pattern.finditer(data):
        path = match.group(2)
        path = urllib.parse.urljoin(url, path)
        sitemap += f'{path}\n'
    open('docs/sitemap.txt', 'w').write(sitemap)


build_sitemap()
