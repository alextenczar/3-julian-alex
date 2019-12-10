from django.forms import ModelForm
from scoring.models import Judge_Assignment

class ScoringForm(ModelForm):
    class Meta:
        model = Judge_Assignment
        fields = ['project_id', 'judge_id', 'goal_score', 'plan_score', 'action_score', 'result_analysis_score', 'communication_score']

    def save(self, commit=True):
        ja = super(ScoringForm, self).save(commit=True)
        ja.goal_score = self.cleaned_data['goal_score']
        ja.plan_score = self.cleaned_data['plan_score']
        ja.action_score = self.cleaned_data['action_score']
        ja.result_analysis_score = self.cleaned_data['result_analysis_score']
        ja.communication_score = self.cleaned_data['communication_score']

        if commit:
            ja.save()

        return ja
