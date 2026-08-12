from django import template

register = template.Library()

@register.filter
def split(value, sep=','):
    """Split a string by `sep` and return a list with whitespace stripped."""
    if not value:
        return []
    try:
        return [part.strip() for part in value.split(sep)]
    except Exception:
        return []

@register.filter
def tech_icon(value):
    """
    Map technology name to Devicon class.
    Returns 'devicon-{name}-plain' by default if not mapped.
    """
    if not value: 
        return ""
    
    value = value.strip()
    lower_val = value.lower()
    
    # Map common names to specific devicon classes
    # See https://devicon.dev/
    mapping = {
        'python': 'python-plain',
        'django': 'django-plain',
        'html': 'html5-plain',
        'css': 'css3-plain',
        'javascript': 'javascript-plain',
        'js': 'javascript-plain',
        'react': 'react-original',
        'vue': 'vuejs-plain',
        'bootstrap': 'bootstrap-plain',
        'tailwind': 'tailwindcss-original',
        'c++': 'cplusplus-plain',
        'cpp': 'cplusplus-plain',
        'c#': 'csharp-plain',
        'c': 'c-plain',
        'java': 'java-plain',
        'postgres': 'postgresql-plain',
        'postgresql': 'postgresql-plain',
        'mysql': 'mysql-plain',
        'git': 'git-plain',
        'github': 'github-original',
        'docker': 'docker-plain',
        'aws': 'amazonwebservices-original-wordmark',
        'linux': 'linux-plain',
        'blender': 'blender-original',
        'unity': 'unity-original',
        'three.js': 'threejs-original',
        'threejs': 'threejs-original',
    }
    
    if lower_val in mapping:
        return f"devicon-{mapping[lower_val]}"
        
    # Fallback: try to use the name directly
    # e.g. "pandas" -> "devicon-pandas-plain"
    return f"devicon-{lower_val}-plain"
