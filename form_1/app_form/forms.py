from django import forms
from django.core import validators
import re

def validate_co_address(value):
    # when we pass value keyword, django automatically trace for Validation
    if (value[0:3].upper() != "C/O"):
        raise validators.ValidationError("Address must be started with c/o")

class FormName(forms.Form):

    Name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Verify your email")
    # Let us call a custom made validator which will validate if the text starts with the character c/o
    text = forms.CharField(widget = forms.Textarea, validators = [validate_co_address])
    #text = forms.CharField(widget = forms.Textarea)
## django has in built validators you can conveniently use to validate your forms
## this check for bots (automatically genearated scripts)
## we are going to add validation for blank fields and for checking for robots
## Let us add a hidden field to our forms.html. This field will remain hidden but is necessary to catch robots.
## required = False means the field will be hidden
    #botcatcher = forms.CharField(required = False, widget = forms.HiddenInput)
    ## Let us define a custom function to catch the bot or robots
    # def clean_botcatcher(this):
    #     botcatcher = this.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         # Yes We have robot in our system
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher

    ## let us validate bot free by using django built in validators
    ## The botcatcher variable length will not equal to 0 if there is a bot attack, so we nned to pass length = 0 for validators.MaxLengthValidator
    ## function.
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])
    ## you can check python documentation for validators functions

    ## Let us clean out entire your form after you verified your Email
    ## clean does not clear your text rather pass your validation
    def clean(this):
        all_clear = super().clean()
        email = all_clear['email']
        verify_email = all_clear['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Email should match")

    # clean_fieldname automatically tells django to go for a validation check
    def clean_Name(this):
        Name = this.cleaned_data['Name']
        # If Name contains space i.e. first name and last name
        if bool(re.search(r"\s", Name)):
            first_name, last_name = Name.split()
            if (first_name[0].isupper() and last_name[0].isupper()):
                pass
            else:
                raise forms.ValidationError("Define your name in a proper way")
        else:
            raise forms.ValidationError("Also provide last name")
        return Name
