from  django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if any(char.isdigit() for char  in name):
            raise  forms.ValidationError("Ismida raqamlar bo'lmasligi kerak.")
        return  name