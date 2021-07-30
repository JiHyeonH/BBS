# 모델폼 사용하기 : 사용자 입력 변수값 처리를 용이하게 해준다. 권장되는 방법. 파일명도 forms로 정해져있다.
from django import forms
from .models import Board


class BoardForm(forms.ModelForm):   # Form을 구성하는 방법은 정해져 있으므로 외우는 수 밖에(object, Meta, model, fields)?
    class Meta:
        model = Board   # BoardForm을 통해 사용할 모델
        fields = ['b_title', 'b_author', 'b_content']     # 그 모델 안의 변수 중에서 사용자 입력으로 보여줄 것.
        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '글제목'
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '작성자'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '내용'
                }
            )
        }

