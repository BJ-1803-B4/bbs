from django import forms


class PostEditForm(forms.Form):
    post_title = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '标题'}))
    post_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',  'placeholder': '正文'}))


    def clean(self):
        cleaned_data = self.cleaned_data
        title = self.cleaned_data['post_title']
        cont_str = self.cleaned_data['post_content']
        cont_html = cont_str
        return cleaned_data
