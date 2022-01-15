from college_portal_app.models import Calendar, CustomUser
from django import forms
from django.forms import ModelForm, DateInput

# class TimeField(forms.TimeField):
#   input_type='time'

class EventForm(ModelForm):

  # start_time = TimeField()

  class Meta:
    model = Calendar
    # datetime-local is a HTML5 input type, format to make date time show on fields
    # fields=('title','description','start_time','end_time')
    
    widgets = {
      # 'start_time': forms.TimeField(attrs={'type':'time','min','00:00','max',}),
      # 'email' : forms.TextInput(attrs={'type':'hidden','value':'request.GET.email'}),
      'description' : forms.Textarea(attrs={'placeholder':'No Events','class':'form-group'}),
     'start_time': forms.TextInput(attrs={'type':'time','class':'form-group','value':'00:00'}),
      'end_time' : forms.TextInput(attrs={'type':'time','class':'form-group','value':'23:59'}),  
    }
    # exclude = ['email']
    exclude = ['customuser','created_date']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
  # #   # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%H:%M',)
    self.fields['end_time'].input_formats = ('%H:%M',)