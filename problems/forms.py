from django import forms
from problems.models import CodeSubmission

LANGUAGE_CHOICES = [
    ("py", "Python"),
    ("c", "C"),
    ("cpp", "C++"),
]

class CodeSubmissionForm(forms.ModelForm):
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 bg-gray-800 border border-gray-600 rounded text-white'
        })
    )

    class Meta:
        model = CodeSubmission
        fields = ["language", "code", "input_data"]
        widgets = {
            'code': forms.Textarea(attrs={
                'rows': 10,
                'class': 'w-full p-2 bg-gray-800 border border-gray-600 rounded text-white font-mono',
                'placeholder': 'Write your code here...'
            }),
            'input_data': forms.Textarea(attrs={
                'rows': 5,
                'class': 'w-full p-2 bg-gray-800 border border-gray-600 rounded text-white font-mono',
                'placeholder': 'Enter input data (optional)...'
            }),
        }
