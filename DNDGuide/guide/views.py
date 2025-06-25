from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import View
from django.db.models.query import QuerySet


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'guide/home.html', {})


class AddClass(View):
    armors = ArmorCategory.objects.all()
    weapons = WeaponsCategories.objects.all()
    chars = Chars.objects.all()
    dices = Dices.objects.all()
    skills = Skills.objects.all()
    tools = Tools.objects.all()

    def get(self, request, *args, **kwargs):
        create_form = AddClassForm(self.chars, self.dices, self.skills, self.weapons, self.armors, self.tools)

        return render(request, 'guide/add_class.html', {'form': create_form})

    def post(self, request, *args, **kwargs):
        create_form = AddClassForm(self.chars, self.dices, self.skills, self.weapons, self.armors, self.tools,
                                   request.POST)
        if create_form.is_valid():
            form_data: dict = dict()
            form_data_queryset: dict = dict()
            for field in create_form.cleaned_data:
                if type(create_form.cleaned_data[field]) == QuerySet:
                    form_data_queryset[field] = create_form.cleaned_data[field]
                else:
                    form_data[field] = create_form.cleaned_data[field]

            new_class = Classes(
                **form_data
            )

            new_class.save()

            for data in form_data_queryset:
                getattr(new_class, data).set(form_data_queryset[data])

            pk = new_class.pk
            new_class.save()

            return render(request, 'guide/home.html')
        else:
            return render(request, 'guide/add_class.html', {'form': create_form})
