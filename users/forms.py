from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['name','email']

class UserUpdateForm(forms.ModelForm):
    # Наш список для отображения
    PET_LIST = [
        'альпака', 'бантенг', 'аксолотль', 'бегемот', 'варан', 
        'гепард', 'даман', 'енот', 'ёж', 'жираф', 'зебра', 
        'игуана', 'койот', 'лемур', 'манул', 'носорог', 
        'питон', 'росомаха', 'суррикат', 'тапир', 'утконос', 
        'фенек', 'хомяк', 'шиншилла', 'щенок', 'эму', 'юрок', 
        'ягуар', 'ящерица'
    ]

    # Распаковываем список в красивую строку через запятую для подсказки
    pets_string = ", ".join(PET_LIST)

    favourite_pet = forms.CharField(
        label="Любимый питомец",
        required=False,
        help_text=f"Доступные варианты: {pets_string}"
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'favourite_pet', 'bio']

    def clean_favourite_pet(self):
        data = self.cleaned_data.get('favourite_pet', '').lower().strip()
        if not data:
            return data
            
        if data not in self.PET_LIST: 
            raise ValidationError(f'Этого зверя нет в списке! Можно выбрать: {self.pets_string}')
            
        return data
            