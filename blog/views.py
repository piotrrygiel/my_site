from django.shortcuts import render
from datetime import date


all_posts = [
    {"slug": "hike-in-the-mountains",
     "image": "mountains.jpg",
     "author": "Piotr",
     "date": date(2023, 2, 26),
     "title": "Mountain Hiking",
     "excerpt": "Beautiful mountains. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus lacinia ipsum vitae pretium. Etiam mi velit, tincidunt in dapibus at, venenatis vitae neque. Mauris in nunc posuere, luctus mauris a, efficitur leo.",
     "content": """
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        """
     },
    {"slug": "programming-is-fun",
     "image": "coding.jpg",
     "author": "Piotr",
     "date": date(2023, 2, 22),
     "title": "Coding",
     "excerpt": "I love coding. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus lacinia ipsum vitae pretium. Etiam mi velit, tincidunt in dapibus at, venenatis vitae neque. Mauris in nunc posuere, luctus mauris a, efficitur leo.",
     "content": """
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        """
     },
    {"slug": "into-the-woods",
     "image": "woods.jpg",
     "author": "Piotr",
     "date": date(2023, 2, 13),
     "title": "Into the woods",
     "excerpt": "Trip to the beautiful forest. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed faucibus lacinia ipsum vitae pretium. Etiam mi velit, tincidunt in dapibus at, venenatis vitae neque. Mauris in nunc posuere, luctus mauris a, efficitur leo.",
     "content": """
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        Integer commodo tincidunt elit, quis sagittis erat pellentesque ut. Pellentesque consectetur nisi tortor, eu ornare elit imperdiet non. Ut consectetur ac nulla eu laoreet. Integer vitae tincidunt nisl. In ut tincidunt justo, eu lacinia magna.
        """
     }
]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    #for post in all_posts:
    #    if post["slug"] == slug:
    #        my_post = post
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })

