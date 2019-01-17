from django import forms
from.models import ListeningQuestion


class UploadListenQuestionForm(forms.Form):
    audio_file = forms.FileField(label='題目檔案')
    answer1 = forms.CharField(label='選項1', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer2 = forms.CharField(label='選項2', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer3 = forms.CharField(label='選項3', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer4 = forms.CharField(label='選項4', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    combo = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
    )

    correct = forms.ChoiceField(label='正確答案', choices=combo)
    # correct2 = forms.MultipleChoiceField(label='正確答案2', choices=combo[])


class ModifyListenQuestionForm(forms.ModelForm):
    audio_name = forms.CharField(label='題目名稱')
    audio_file = forms.FileField(label='題目檔案')
    answer1 = forms.CharField(label='選項1', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer2 = forms.CharField(label='選項2', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer3 = forms.CharField(label='選項3', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    answer4 = forms.CharField(label='選項4', max_length=255, required=True,
                              error_messages={'required': '此項目必填！'})
    combo = [
        ('answer1', '選項1'),
        ('answer2', '選項2'),
        ('answer3', '選項3'),
        ('answer4', '選項4'),
    ]
    correct = forms.ChoiceField(label='正確答案', choices=combo)

    class Meta:
        model = ListeningQuestion
        fields = '__all__'


class LoginForm(forms.Form):
    account = forms.CharField(label='學號', max_length=10)
    password = forms.CharField(label='密碼', max_length=15, widget=forms.PasswordInput)
