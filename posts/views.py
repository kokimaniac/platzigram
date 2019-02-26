"""Posts views."""

#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %d th, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
        <p><strong>{name}</strong><p/>
        <figure><img src="{picture}"/></figure>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        """.format(**post))

    return HttpResponse('<br>'.join(content))
