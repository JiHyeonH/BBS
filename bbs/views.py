from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Comment
from .forms import BoardForm
# Create your views here.


def b_list(request):

    posts = Board.objects.all().order_by('-id')
    return render(request, 'bbs/list.html', {
        'posts': posts
    })
    # 여기서 render하면 templates 폴더 중에서 html파일을 찾게 되는데 bbs폴더를 만든 이유가 여기서 보인다. (찾기 위한 경로)


def b_create(request):

    if request.method == 'POST':
        # POST 방식은 새글 작성화면에서 새글 저장 버튼을 눌렀을 때 실행된 경우 = POST
        board_form = BoardForm(request.POST)    # 입력 양식 각각에 한 번에 입력해주는 방법이다.

        if board_form.is_valid():   # 정상이면
            # board_form.save()   # 입력된 값 데이터 베이스 저장하는 방법을 아래와 같이 진행한다.
            new_post = board_form.save(commit=False)
            # new_post.b_like_count=100 # 이와 같이 form에는 없는 다른 속성에 대한 값도 지정해서 저장이 가능하기 때문.
            new_post.save()
            return redirect('bbs:b_list')

    else:
        # 리스트 화면에서 새글 작성 버튼을 눌렀을 때 실행된 경우 = GET
        board_form = BoardForm()    # 사용자 입력을 받을 수 있는 양식을 Form을 통해 만든다.
        return render(request, 'bbs/create.html', {
            'board_form': board_form
        })


def b_detail(request, post_id):

    board_objects = get_object_or_404(Board, pk=post_id)
    comment_objects = Comment.objects.select_related('Board__id')
    return render(request, 'bbs/detail.html', {
        'board_objects': board_objects
    })


def b_fix(request, post_id):

    board_objects = get_object_or_404(Board, pk=post_id)
    if request.method == 'POST':
        board_form = BoardForm(request.POST, instance=board_objects)
        # board_form.b_author = board_objects.b_author  # 글 수정에서 작성자 정보는 변동되지 않게 만들어서, 폼에 입력되야 할 작성자 변수가 누락된건가..?
        if board_form.is_valid():  # 정상이면
            board_objects = board_form.save(commit=False)
            board_objects.save()
            return redirect('bbs:b_detail', post_id=board_objects.id)
    else:
        board_form = BoardForm(instance=board_objects)
        return render(request, 'bbs/fix.html', {'board_form': board_form, 'board_objects':board_objects})


def b_delete(request, post_id):

    board_objects = get_object_or_404(Board, pk=post_id)
    board_objects.delete()
    return redirect('bbs:b_list')


def c_delete(request, comment_id):

    comment_objects = get_object_or_404(Board, pk=comment_id)
    comment_objects.delete()
    return redirect('bbs:b_detail')
