from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form_control',
            'placeholder' : 'Leave a comment!'
        }
    ))