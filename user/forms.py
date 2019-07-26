from django import forms
from django.forms import ValidationError

from user.models import Profile


class ProfileModelForm(forms.ModelForm):
    # 将模型字段转化为验证字段
    class Meta:
        model = Profile
        # 表示全部使用
        fields = "__all__"
        # 部分使用
        # fields = ['location', 'dating_sex', 'min_dating_age']
        # 排除使用
        # exclude = ['location']

    # django自带的校验工具
    def clean_max_distance(self):
        cleaned_data = self.clean()
        min_distance = cleaned_data.get('min_distance')
        max_distance = cleaned_data.get('max_distance')
        if min_distance > max_distance:
            raise ValidationError('min_distance > max_distance')
        return max_distance

    def clean_max_dating_age(self):
        cleaned_data = self.clean()
        min_dating_age = cleaned_data.get('min_distance')
        max_dating_age = cleaned_data.get('max_distance')
        if min_dating_age > max_dating_age:
            raise ValidationError('min_dating_age > max_dating_age')
        return max_dating_age
