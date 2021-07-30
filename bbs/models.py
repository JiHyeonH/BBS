from django.db import models

# Create your models here.


class Board(models.Model):

    b_title = models.CharField('글 제목', max_length=30)
    b_author = models.CharField('작성자', max_length=20)
    b_content = models.CharField('내용', max_length=1000)
    b_date = models.DateTimeField(auto_now=True)    # 자동으로 현재 시간으로 설정해줌. (등록, 수정 어떤 경우에도)
    b_comment_count = models.IntegerField(default=0)
    b_like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.b_title


class Comment(models.Model):

    c_author = models.CharField(max_length=20)
    c_content = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_content
