"""
posts viwes
"""

#django
from django.http import HttpResponse

#utilities
from datetime import datetime



posts = [
    {
        'name':'Gal Gadot',
        'user':'Wonder Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://www.eluniverso.com/resizer/lJMJvfyEXnPr91HVocPyjRoC2ts=/817x670/smart/filters:quality(70)/cloudfront-us-east-1.images.arcpublishing.com/eluniverso/4BWQMPEOCXAT4VVX3F3CBBU6UQ.jpg',
    }
    ,
    {
        'name':'Christian Bale',
        'user':'Batman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://aws.revistavanityfair.es/prod/designs/v1/assets/785x589/196248.jpg',
    }
    ,
    {
        'name':'Barry Allen',
        'user':'Flash',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'https://vader.news/__export/1601592596230/sites/gadgets/img/2020/10/01/barry-allen-the-flash.jpg_1277422037.jpg',
    }



]



def lists_posts(request):
    "lists Existing posts"
    contenido = []
    for post in posts:
        contenido.append("""

            <p><strong>{name}</strong></p>
            <p><small>{user}</strong></p>
            <figure><img src="{picture}"/></figure>

        """.format(**post))

    return HttpResponse('<br>'.join(contenido))
