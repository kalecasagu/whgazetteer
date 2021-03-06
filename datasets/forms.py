# datasets.forms

from django import forms
from django.db import models
from django.forms import ClearableFileInput
from datasets.models import Dataset, Hit, DatasetFile
from main.choices import FORMATS, DATATYPES, STATUS

MATCHTYPES = [
  ('closeMatch','closeMatch'),
  #('exactMatch','exactMatch'),
  #('related','related'),
  ('none','no match'),]

class HitModelForm(forms.ModelForm):
  match = forms.CharField(
    initial='none',
    widget=forms.RadioSelect(choices=MATCHTYPES))
  #flag = forms.BooleanField(initial=False, required=False)
  
  class Meta:
    model = Hit
    fields = ['id','authority','authrecord_id','query_pass','score','json' ]
    hidden_fields = ['id','authority','authrecord_id','query_pass','score','json' ]
    widgets = {
      'id': forms.HiddenInput(),
      'authority': forms.HiddenInput(),
      'authrecord_id': forms.HiddenInput(),
      'json': forms.HiddenInput()
    }
    
  def __init__(self, *args, **kwargs):
    super(HitModelForm, self).__init__(*args, **kwargs)

    for key in self.fields:
      self.fields[key].required = False     


#class DatasetFileModelForm(forms.ModelForm):
  #class Meta:
    #model = DatasetFile
    #fields = ['file','rev','uri_base','format','dataset_id','delimiter',
              #'status','accepted_date','header','numrows']
    #widgets = { 'file': ClearableFileInput() }    
  

class DatasetFileModelForm(forms.ModelForm):
  class Meta:
    model = DatasetFile
    fields = ('dataset_id','file','rev','format','delimiter',
              'df_status','datatype','header','numrows')
    
  #file = forms.FileField()
  #uri_base = forms.URLField(widget=forms.URLInput(attrs={'placeholder':'Leave blank unless changed'}))
  #format = forms.ChoiceField(choices=FORMATS)
    
  def __init__(self, *args, **kwargs):
    super(DatasetFileModelForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.error_messages = {'required':'The field {fieldname} is required'.format(
                  fieldname=field.label)}    

class DatasetDetailModelForm(forms.ModelForm):
  class Meta:
    model = Dataset
    # file fields = ('file','rev','uri_base','format','dataset_id','delimiter',
    #   'status','accepted_date','header','numrows')
    fields = ('owner','id','label','title','uri_base','description',
              'datatype','numlinked','public','webpage')
    widgets = {
      'description': forms.Textarea(attrs={
        'rows':2,'cols': 40,'class':'textarea','placeholder':'brief description'}),
      'webpage': forms.TextInput(attrs={'size': 30})
    }
  
  file = forms.FileField(required=False)
  uri_base = forms.URLField(
    widget=forms.URLInput(
      attrs={'placeholder':'Leave blank unless changed','size': 40}
    ),
    required=False
  )
  format = forms.ChoiceField(choices=FORMATS,initial="delimited")
    
  def __init__(self, *args, **kwargs):
    super(DatasetDetailModelForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.error_messages = {'required':'The field fubar {fieldname} is required'.format(
                  fieldname=field.label)}    

class DatasetCreateModelForm(forms.ModelForm):
  class Meta:
    model = Dataset
    # file fields = ('file','rev','uri_base','format','dataset_id','delimiter',
    #   'status','accepted_date','header','numrows')
    fields = ('owner','id','title','label','datatype','description','uri_base','public','creator','webpage')
    widgets = {
      'description': forms.Textarea(attrs={
        'rows':2,'cols': 39,'class':'textarea','placeholder':'brief description'})
      ,'uri_base': forms.URLInput(attrs={
        'placeholder':'Leave blank unless record IDs are URIs','size':40})
      ,'title': forms.TextInput(attrs={'size': 40})
      ,'creator': forms.TextInput(attrs={'size': 40})
      ,'webpage': forms.URLInput(attrs={'size': 40,'placeholder':'Blank if none'})
    }
  
  # fields used to create new DatasetFile record from form
  #uri_base = forms.URLField(widget=forms.URLInput(
    #attrs={'placeholder':'Leave blank unless record IDs are URIs','size':35}))
  file = forms.FileField()
  rev = forms.IntegerField()
  format = forms.ChoiceField(choices=FORMATS)
  delimiter = forms.CharField()
  header = forms.CharField()
  df_status = forms.ChoiceField(choices=STATUS)
  numrows = forms.IntegerField()
  upload_date = forms.DateTimeField()

  def __init__(self, *args, **kwargs):
    super(DatasetCreateModelForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.error_messages = {'required':'The field {fieldname} is required'.format(
                  fieldname=field.label)}    
