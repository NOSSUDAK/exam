from django import forms
from django.forms import SelectDateWidget

from tasker.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {"deadline": SelectDateWidget(empty_label=("Year", "Month", "Day"))}
