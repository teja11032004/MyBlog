from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from blog.models import post, Comment,Reply
from django.contrib.auth.decorators import login_required

# Existing view - unchanged
def blog_home(request):
    allposts = post.objects.all()
    content = {'posts': allposts}
    return render(request, 'blog/blog_page.html', content)

# UPDATED view - now includes comments
def blog_post(request, slug):
    post_item = get_object_or_404(post, slug=slug)
    comments = post_item.comments.order_by('-timestamp')

    context = {
        'post': post_item,
        'comments': comments
    }
    return render(request, 'blog/blog_post.html', context)


# NEW VIEW to add comments
@login_required
def add_comment(request, slug):
    post_item = get_object_or_404(post, slug=slug)

    if request.method == "POST":
        comment_text = request.POST.get("comment")

        if comment_text.strip():
            Comment.objects.create(
                post=post_item,
                user=request.user,
                comment=comment_text
            )

    return redirect('blog_post', slug=slug)

def post_reply(request, comment_id):
    if request.method == "POST":
        reply_text = request.POST.get("reply_text")
        
        Reply.objects.create(
            comment_id=comment_id,
            user=request.user,
            reply=reply_text
        )
        return redirect(request.META.get("HTTP_REFERER", "/"))

