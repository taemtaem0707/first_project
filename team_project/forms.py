from django import forms
from django.utils.translation import gettext_lazy as _

no = forms.HiddenInput()
team1_option = (
                ('Liverpool', 'Liverpool'),
                ('Manchester City', 'Manchester City'),
                ('Manchester United', 'Manchester United'),
                ('Chelsea', 'Chelsea'),
                ('Leicester City', 'Leicester City'),
                ('Tottenham Hotspur', 'Tottenham Hotspur'),
                ('Wolverhampton Wanderers', 'Wolverhampton Wanderers'),
                ('Arsenal', 'Arsenal'),
                ('Sheffield United', 'Sheffield United'),
                ('Burnley', 'Burnley'),
                ('Southampton', 'Southampton'),
                ('Everton', 'Everton'),
                ('Newcastle United', 'Newcastle United'),
                ('Crystal Palace', 'Crystal Palace'),
                ('Brighton and Hove Albion', 'Brighton and Hove Albion'),
                ('West Ham United', 'West Ham United'),
                ('Aston Villa', 'Aston Villa'),
                ('AFC Bournemouth', 'AFC Bournemouth'),
                ('Watford', 'Watford'),
                ('Norwich City', 'Norwich City'),
                )


team2_option = (
    ('Liverpool', 'Liverpool'),
    ('Manchester City', 'Manchester City'),
    ('Manchester United', 'Manchester United'),
    ('Chelsea', 'Chelsea'),
    ('Leicester City', 'Leicester City'),
    ('Tottenham Hotspur', 'Tottenham Hotspur'),
    ('Wolverhampton Wanderers', 'Wolverhampton Wanderers'),
    ('Arsenal', 'Arsenal'),
    ('Sheffield United', 'Sheffield United'),
    ('Burnley', 'Burnley'),
    ('Southampton', 'Southampton'),
    ('Everton', 'Everton'),
    ('Newcastle United', 'Newcastle United'),
    ('Crystal Palace', 'Crystal Palace'),
    ('Brighton and Hove Albion', 'Brighton and Hove Albion'),
    ('West Ham United', 'West Ham United'),
    ('Aston Villa', 'Aston Villa'),
    ('AFC Bournemouth', 'AFC Bournemouth'),
    ('Watford', 'Watford'),
    ('Norwich City', 'Norwich City'),
)


class checkForm(forms.Form):
    team1 = forms.ChoiceField(required=True,
                              choices=team1_option,
                              label='',
                              )
    team1.widget.attrs.update({'class':'selectpicker show-tick',
                               'data-live-search':'true',
                               'data-style':'btn-primary',
                               'data-header':"자신의 팀을 고르세요.",
                               'data-size': "5",
                               'data-dropup-auto':"false"



                               })
    team2 = forms.ChoiceField(required=True,
                              choices=team2_option,
                              label='',
                              )
    team2.widget.attrs.update({'class':'selectpicker show-tick',
                               'data-live-search':'true',
                               'data-style':'btn-danger',
                               'data-header': "상대 팀을 고르세요.",
                               'data-size': "5",
                               'data-dropup-auto': "false"
                               })

    from django.forms import Select

