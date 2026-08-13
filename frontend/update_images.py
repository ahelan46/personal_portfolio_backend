import os

files = [
    'src/content/stack.ts',
    'src/content/projects.ts',
    'src/content/gallery.ts',
    'src/components/sections/Hero/Hero.tsx',
    'src/components/sections/Connect/Connect.tsx'
]

for f in files:
    path = os.path.join('d:/Desktop/Desktop/portfolio3/portfolio/frontend', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('"/images/', '"/static/dist/images/')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done!')
