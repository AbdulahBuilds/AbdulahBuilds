"""
Script to update dark.svg and light.svg banners for Muhammad Abdullah (AbdulahBuilds).
Run this script anytime you want to re-generate or re-sync the SVG banners.
"""

import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASCII_PATH = os.path.join(BASE_DIR, 'mine_ascii.txt')

# Read ascii lines
with open(ASCII_PATH, 'r', encoding='utf-8') as f:
    ascii_lines = [line.rstrip('\r\n') for line in f if line.strip()]

print(f"Read {len(ascii_lines)} ascii lines from {ASCII_PATH}")

# Prepare tspan block
tspan_elements = []
for i, line in enumerate(ascii_lines):
    dy = '0' if i == 0 else '6.2'
    tspan_elements.append(f'<tspan x="70" dy="{dy}">{line}</tspan>')
ascii_svg_block = '\n        '.join(tspan_elements)

def update_svg(filename, is_dark=True):
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update clipPhrases widths:
    # 1. Full-Stack Developer -> 216
    # 2. MERN Stack Developer -> 216
    # 3. Next.js Developer -> 184
    # 4. React & TypeScript Developer -> 292
    # 5. Backend API Developer -> 227
    # 6. Problem Solver -> 151
    clip_configs = [
        ('clipPhrase1', 'values="0; 216; 216; 0; 0" keyTimes="0; 0.0571; 0.1429; 0.1571; 1"'),
        ('clipPhrase2', 'values="0; 0; 216; 216; 0; 0" keyTimes="0; 0.1667; 0.2238; 0.3095; 0.3238; 1"'),
        ('clipPhrase3', 'values="0; 0; 184; 184; 0; 0" keyTimes="0; 0.3333; 0.3905; 0.4762; 0.4905; 1"'),
        ('clipPhrase4', 'values="0; 0; 292; 292; 0; 0" keyTimes="0; 0.5; 0.5571; 0.6429; 0.6571; 1"'),
        ('clipPhrase5', 'values="0; 0; 227; 227; 0; 0" keyTimes="0; 0.6667; 0.7238; 0.8095; 0.8238; 1"'),
        ('clipPhrase6', 'values="0; 0; 151; 151; 0; 0" keyTimes="0; 0.8333; 0.8905; 0.9762; 0.9905; 1"')
    ]
    for cid, val_str in clip_configs:
        content = re.sub(
            rf'<clipPath id="{cid}">[\s\S]*?</clipPath>',
            f'<clipPath id="{cid}">\n        <rect x="522" y="180" height="30" width="0">\n          <animate attributeName="width" {val_str} dur="21s" repeatCount="indefinite" />\n        </rect>\n      </clipPath>',
            content
        )

    # 2. Update usernames
    content = content.replace('mahyudeen@avatar:~', 'abdullah@avatar:~')
    content = content.replace('mahyudeen@avatar:~$', 'abdullah@avatar:~$')
    content = content.replace('mahyudeen@terminal:~', 'abdullah@terminal:~')
    content = content.replace('Mahyudeen Shahid', 'Muhammad Abdullah')

    # 3. Update ASCII art block
    ascii_pattern = r'(<text x="70" y="140"[^\>]*xml:space="preserve">)[\s\S]*?(</text>)'
    content = re.sub(ascii_pattern, f'\\1\n        {ascii_svg_block}\n      \\2', content)

    # 4. Update cursor animation translation
    new_cursor_vals = 'values="0,0; 216,0; 216,0; 0,0; 0,0; 216,0; 216,0; 0,0; 0,0; 184,0; 184,0; 0,0; 0,0; 292,0; 292,0; 0,0; 0,0; 227,0; 227,0; 0,0; 0,0; 151,0; 151,0; 0,0; 0,0"'
    content = re.sub(r'values="0,0;\s*259,0;[\s\S]*?0,0"', new_cursor_vals, content)

    # 5. Metadata details
    content = re.sub(r'(Location:\s*<tspan[^>]*>)[^<]*(</tspan>)', r'\g<1>Peshawar, Pakistan\g<2>', content)
    content = re.sub(r'(Education:\s*<tspan[^>]*>)[^<]*(</tspan>)', r'\g<1>BS Computer Science student at VU\g<2>', content)
    content = re.sub(r'(Focus:\s*<tspan[^>]*>)[^<]*(</tspan>)', r'\g<1>Full-Stack MERN, Next.js &amp; Orderworker\g<2>', content)
    content = re.sub(r'(Portfolio:\s*<tspan[^>]*>)[^<]*(</tspan>)', r'\g<1>github.com/AbdulahBuilds\g<2>', content)
    content = re.sub(r'(Email:\s*<tspan[^>]*>)[^<]*(</tspan>)', r'\g<1>abdullahak071@gmail.com\g<2>', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated: {filename}")

if __name__ == '__main__':
    update_svg('dark.svg', is_dark=True)
    update_svg('light.svg', is_dark=False)
