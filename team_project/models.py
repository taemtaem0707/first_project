from django.db import models

# Create your models here.



class Check(models.Model):
    id = models.AutoField(primary_key=True) # 자동증가, pk등록
    team1 = models.CharField(max_length=30)
    team2 = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)  # 저장된 레코드 수정 시 수정 시각

    # num_stars = models.IntegerField()  # 숫자 필드는 이렇게 선언한다.
