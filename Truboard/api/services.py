import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def fetch_posts_from_external_api():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()
    return data

def paginate_posts(posts_data, page_number, items_per_page):
    paginator = Paginator(posts_data, items_per_page)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts
