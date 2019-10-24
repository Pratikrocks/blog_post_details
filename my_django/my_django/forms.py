from django import forms
from blog.models import BlogPost


class ContactForm(forms.Form):
    content = forms.CharField()
    title = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The size must be more than 5")


class BlogPostForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = BlogPost
        fields = ['content', 'title']

    def clean(self):
        print(dir(self))
        print("I am at BlogPostForm")
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        try:
            if len(title) < 2:
                raise forms.ValidationError("The size must be more than 5")
        except:
            pass
