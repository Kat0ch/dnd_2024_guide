from django import forms

char_widget = forms.TextInput(attrs={'class': 'form-control'})
text_widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
int_widget = forms.NumberInput(attrs={'class': 'form-control'})
range_widget = forms.NumberInput(attrs={'class': 'form-range', 'type': 'range'})
image_widget = forms.ClearableFileInput(attrs={'class': 'form-control', 'type': 'file'})
MMCF_widget = forms.SelectMultiple(attrs={'class': 'form-select'})
MCF_widget = forms.Select(attrs={'class': 'form-select'})


class AddClassForm(forms.Form):

    def __init__(self,
                 chars,
                 dices,
                 skills,
                 weapons_categories,
                 armors_categories,
                 tools,
                 request=None,
                 ):
        super().__init__(request)

        self.fields['name'] = forms.CharField(label='Название', widget=char_widget)
        self.fields['image'] = forms.ImageField(label='Изображение', widget=image_widget, required=False)
        self.fields['description'] = forms.CharField(label='Описание', widget=text_widget, required=False)
        self.fields['main_chars'] = forms.ModelMultipleChoiceField(label='Основные характеристики', widget=MMCF_widget,
                                                                   queryset=chars)
        self.fields['hit_dice'] = forms.ModelChoiceField(label='Кость хитов', queryset=dices, widget=MCF_widget)
        self.fields['hits_on_first_level'] = forms.IntegerField(label='Хиты на первом уровне', widget=int_widget)
        self.fields['hits_on_next_levels'] = forms.IntegerField(label='Хиты на последующих уровнях', widget=int_widget)
        self.fields['saving_throws'] = forms.ModelMultipleChoiceField(label='Спасброски', widget=MMCF_widget,
                                                                      queryset=chars)
        self.fields['skills_quantity'] = forms.IntegerField(label='Кол-во доступных для изучения навыков',
                                                            widget=int_widget)
        self.fields['skills_list'] = forms.ModelMultipleChoiceField(label='Навыки', widget=MMCF_widget,
                                                                    queryset=skills, required=False)
        self.fields['weapons'] = forms.ModelMultipleChoiceField(label='Владение оружием', widget=MMCF_widget,
                                                                queryset=weapons_categories, required=False)
        self.fields['weapons_text'] = forms.CharField(label='Текст оружия', widget=text_widget, required=False)
        self.fields['armors'] = forms.ModelMultipleChoiceField(label='Владение доспехами', widget=MMCF_widget,
                                                               queryset=armors_categories, required=False)
        self.fields['armors_text'] = forms.CharField(label='Текст доспехов', widget=text_widget, required=False)
        self.fields['tools'] = forms.ModelMultipleChoiceField(label='Владение инструментами', widget=MMCF_widget,
                                                              queryset=tools, required=False)
        self.fields['tools_text'] = forms.CharField(label='Текст инструментов', widget=text_widget, required=False)
        self.fields['beginning_equipment'] = forms.CharField(label='Начальное снаряжение', widget=text_widget,
                                                             required=False)
        self.fields['spells_power'] = forms.IntegerField(label='Сила заклинателя (от 0 до 3)', widget=range_widget,
                                                         max_value=3, min_value=0)
