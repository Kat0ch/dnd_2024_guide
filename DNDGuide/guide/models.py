from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Components(models.Model):
    name = models.CharField(verbose_name='Названине')
    description = models.CharField(verbose_name='Описание')
    abbreviation = models.CharField(verbose_name='Сокращение', max_length=1)

    def __str__(self):
        return f'{self.name}({self.abbreviation})'

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'


class Dices(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name='Значение', )

    def __str__(self):
        return f'd{self.value}'

    class Meta:
        verbose_name = 'Кость'
        verbose_name_plural = 'Кости'


class MagicSchools(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа магии'
        verbose_name_plural = 'Школы магии'


class DamageTypes(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип урона'
        verbose_name_plural = 'Типы урона'


class Damages(models.Model):
    quantity = models.IntegerField(verbose_name='Количесво костей', validators=[MinValueValidator(1)])
    damage = models.ForeignKey(Dices, on_delete=models.CASCADE, verbose_name='Кость урона', related_name='damage_dice')
    damage_type = models.ForeignKey(Dices, on_delete=models.CASCADE, verbose_name='Тип урона',
                                    related_name='damage_type')

    def __str__(self):
        return f'{self.quantity}d{self.damage} - {self.damage_type}'

    class Meta:
        verbose_name = 'Урон'
        verbose_name_plural = 'Уроны'


class Spells(models.Model):
    name = models.CharField(verbose_name='Название')
    level = models.IntegerField(verbose_name='Уровень')
    school = models.ForeignKey(MagicSchools, on_delete=models.CASCADE, verbose_name='Школа')
    using_time = models.CharField(verbose_name='Время накладывания')
    distant = models.CharField(verbose_name='Дистанция')
    components = models.ManyToManyField(Components, verbose_name='Компоненты')
    material_components = models.CharField(verbose_name='Материальные компоненты', blank=True)
    concentration = models.BooleanField(verbose_name='Концентрация')
    spell_update = models.TextField(verbose_name='Улучшение заклинания')

    def __str__(self):
        return f'{self.level} уровень - {self.name}'

    class Meta:
        verbose_name = 'Заклинание'
        verbose_name_plural = 'Заклинания'


class DamageSpells(Spells):
    damage = models.ManyToManyField(Damages, verbose_name='Урон', related_name='spell_damages')
    damage_on_level = models.ManyToManyField(Damages, verbose_name='Урон за уровень',
                                             related_name='spell_damage_on_level')

    class Meta:
        verbose_name = 'Боевое заклинание'
        verbose_name_plural = 'Боевые заклинания'


class Chars(models.Model):
    name = models.CharField(verbose_name='Название')
    abbreviated = models.CharField(verbose_name='Сокращение', max_length=3)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.abbreviated


class Items(models.Model):
    name = models.CharField(verbose_name='Название')
    weight = models.FloatField(verbose_name='Вес', validators=[MinValueValidator(0.0)], blank=True)
    price = models.IntegerField(verbose_name='Цена', validators=[MinValueValidator(0.0)])
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Skills(models.Model):
    name = models.CharField(verbose_name='Название')
    char = models.ForeignKey(Chars, on_delete=models.CASCADE, verbose_name='Характеристика')
    description = models.TextField(verbose_name='Пример использования')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class WeaponsCategories(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Категория оружия'
        verbose_name_plural = 'Категории оружия'

    def __str__(self):
        return self.name


class WeaponsClasses(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Класс оружия'
        verbose_name_plural = 'Классы оружия'

    def __str__(self):
        return self.name


class WeaponsFeatures(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание', )

    class Meta:
        verbose_name = 'Свойство оружия'
        verbose_name_plural = 'Свойства оружия'

    def __str__(self):
        return self.name


class WeaponsTechniques(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Оружейные прием'
        verbose_name_plural = 'Оружейные приемы'

    def __str__(self):
        return self.name


class ArmorCategory(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Категория доспеха'
        verbose_name_plural = 'Категории доспехов'

    def __str__(self):
        return self.name


class Armors(Items):
    category = models.ForeignKey(ArmorCategory, models.CASCADE, 'armor_category', verbose_name='Категория доспеха')
    ac = models.IntegerField(verbose_name='Класс защиты', validators=[MinValueValidator(10)])
    ac_dex = models.IntegerField(verbose_name='Бонус ловкости', default=0)
    min_power = models.IntegerField(verbose_name='Минимум силы', blank=True)
    hide = models.BooleanField(verbose_name='Помеха скрытности', )

    class Meta:
        verbose_name = 'Доспех'
        verbose_name_plural = 'Доспехи'


class Weapons(Items):
    damage = models.ForeignKey(Damages, models.CASCADE, 'weapon_damage', verbose_name='Урон')
    category = models.ForeignKey(WeaponsCategories, models.CASCADE, 'weapon_type',
                                 verbose_name='Категория оружия')
    clas = models.ForeignKey(WeaponsClasses, models.CASCADE, 'weapon_class', verbose_name='Класс оружия')
    features = models.ManyToManyField(WeaponsFeatures, 'weapons_features', verbose_name='Свойства оружия')
    techniques = models.ForeignKey(WeaponsTechniques, models.CASCADE, 'weapon_technique',
                                   verbose_name='Оружейный прием')

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружия'


class Tools(Items):
    char = models.ForeignKey(Chars, models.CASCADE, verbose_name='Характеристика', related_name='tool_char')
    usage = models.CharField(verbose_name='Использование')
    creating = models.CharField(verbose_name='Создание', blank=True)
    creating_items = models.ManyToManyField(Items, verbose_name='Создвание предметов', related_name='items_tools',
                                            blank=True)

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class Classes(models.Model):
    name = models.CharField(verbose_name='Название')
    image = models.ImageField(upload_to='images/classes/%m/%Y/%d/', blank=True)
    description = models.TextField(verbose_name='Описание класса')
    main_chars = models.ManyToManyField(Chars, verbose_name='Основные хар-ки', related_name='class_main_chars')
    hit_dice = models.ForeignKey(Dices, models.CASCADE, verbose_name='Кость хитов', related_name='class_hit_dice')
    hits_on_first_level = models.IntegerField(verbose_name='Хиты на первом уровне')
    hits_on_next_levels = models.IntegerField(verbose_name='Хиты на следующих уровнях')
    saving_throws = models.ManyToManyField(Chars, verbose_name='Спасброски', related_name='class_saving_throws')
    skills_quantity = models.IntegerField(verbose_name='Количество навыков')
    skills_list = models.ManyToManyField(Skills, verbose_name='Навыки', related_name='class_skills', blank=True)
    weapons = models.ManyToManyField(WeaponsCategories, verbose_name='Владение оружием', related_name='class_weapons',
                                     blank=True)
    weapons_text = models.CharField(verbose_name='Владение оружием(текст)', blank=True)
    tools = models.ManyToManyField(Tools, verbose_name='Владение инструментами', related_name='class_tools', blank=True)
    tools_text = models.CharField(verbose_name='Владение инструменатми(текст)', blank=True)
    armors = models.ManyToManyField(ArmorCategory, verbose_name='Владение инструментами', related_name='class_armors',
                                    blank=True)
    armors_text = models.CharField(verbose_name='Владение доспехами(текст)', blank=True)
    beginning_equipment = models.TextField(verbose_name='Старовое снаряжение', blank=True)
    spells_power = models.IntegerField(verbose_name='Сила заклинаний',
                                       validators=[MinValueValidator(0), MaxValueValidator(3)])

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name


class ClassesSkillsTableColumns(models.Model):
    name = models.CharField(verbose_name='Название')
    clas = models.ForeignKey(Classes, models.CASCADE, 'class_skill_table', verbose_name='Класс')

    class Meta:
        verbose_name = 'Столбец таблицы умений класса'
        verbose_name_plural = 'Столбцы таблицы умений класса'

    def __str__(self):
        return self.name


class ClassesSkillsTableValues(models.Model):
    value = models.CharField(verbose_name='Значение')
    column = models.ForeignKey(ClassesSkillsTableColumns, models.CASCADE, 'column_value', verbose_name='Значение')

    class Meta:
        verbose_name = 'Значение таблицы умений класса'
        verbose_name_plural = 'Значения таблицы умений класса'

    def __str__(self):
        return self.value


class MagicFocuses(Items):
    classes = models.ManyToManyField(Classes, verbose_name='Класс', related_name='classes_focuses')

    class Meta:
        verbose_name = 'Фокусировка'
        verbose_name_plural = 'Фокусировки'


class SubClasses(models.Model):
    name = models.CharField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    clas = models.ForeignKey(Classes, models.CASCADE, verbose_name='Класс', related_name='class_level', blank=True)

    class Meta:
        verbose_name = 'Подкласс'
        verbose_name_plural = 'Подклассы'

    def __str__(self):
        return self.name


class Levels(models.Model):
    number = models.IntegerField(verbose_name='Номер уровня', validators=[MinValueValidator(1), MaxValueValidator(20)])
    name = models.CharField(verbose_name='Название уровня')
    description = models.TextField(verbose_name='Описание')
    clas = models.ForeignKey(Classes, models.CASCADE, verbose_name='Класс', related_name='class_levels', blank=True)
    subclass = models.ForeignKey(SubClasses, models.CASCADE, verbose_name='Подкласс', related_name='subclasses_level',
                                 blank=True)

    class Meta:
        verbose_name = 'Уровень'
        verbose_name_plural = 'Уровни'

    def __str__(self):
        return f'{self.number} уровень {self.clas.name}{self.subclass.name} - {self.name}'
