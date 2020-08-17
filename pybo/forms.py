from django import forms
from pybo.models import Question, Answer
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'subject',
            'content'
        ]
        # 위젯을 통해 폼 입력 항목란에 부트스트랩 클래스가 추가 가능

        # 라벨 지정
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'content'
        ]
        labels = {
            'content':'답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }