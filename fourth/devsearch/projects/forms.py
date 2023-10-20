from django.forms import ModelForm
from .models import Projects, Review
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'featured_image',
                  'description', 'demo_link',
                  'source_link', 'tags']

        widgets = {'tags': forms.CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
