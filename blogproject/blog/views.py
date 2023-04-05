from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import date
from .models import Post,Author,Tag

# Create your views here.
# post_lists = [
#        {
#        "slug":"wano-mountains",
#        "image":"mountain.jpg",
#        "author":"mark",
#        "date":date(2022,1,22),
#        "title":"Wano",
#        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus",
#        "content":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus"
#        },
#        {
#        "slug":"impel-down",
#        "image":"impel-down.jpg",
#        "author":"oda",
#        "date":date(2022,2,12),
#        "title":"IMPEL DOWN",
#        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus",
#        "content":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus"
#        },
#        {
#        "slug":"enies-lobby",
#        "image":"enieslobby.jpg",
#        "author":"tony",
#        "date":date(2022,3,21),
#        "title":"Enies lobby",
#        "excerpt": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus",
#        "content":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error in iste eius! Esse quidem amet sunt illum provident dolores eligendi dignissimos. Molestiae necessitatibus ex corrupti, est tempore eum nostrum doloribus"
#        }
# ]

# def get_key(post):
#        return post["date"]


def index(req):
    latest_post = Post.objects.all().order_by("-date")[:3]
#     sort_list = sorted(post_lists,key=get_key)
#     sort_list = sorted(latest_post)
#     final_list = sort_list[-3:]
    return render(req,"blog/index.html",{"posts":latest_post})

# def posts(req):
#         return render(req,"blog/all-post.html",{"post_lists":post_lists})

def posts(req):
        post = Post.objects.all()
        return render(req,"blog/all-post.html",{"post_lists":post})


def post_detail(req,slug):
        # identified_post = ""
        # for post in post_lists:
        #         if post["slug"]==slug:
        #                 identified_post = post
       #  //
       #  identified_post = next(post for post in post_lists if post["slug"]==slug)
       #  return render(req,"blog/post-detail.html",{"post":identified_post})
    #    post_lists = Post.objects.get(slug=slug)
       post_lists =get_object_or_404(Post,slug=slug)
      
       # identified_post = next(post for post in post_lists if post["slug"]==slug)
       return render(req,"blog/post-detail.html",{"post":post_lists,"post_tag":post_lists.tag.all()})
