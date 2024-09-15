from django.db import models

# def translit_to_eng(s: str) -> str:
#     d = {
#         "а": "a",
#         "б": "b",
#         "в": "v",
#         "г": "g",
#         "д": "d",
#         "е": "e",
#         "ё": "yo",
#         "ж": "zh",
#         "з": "z",
#         "и": "i",
#         "й": "y",
#         "к": "k",
#         "л": "l",
#         "м": "m",
#         "н": "n",
#         "о": "o",
#         "п": "p",
#         "р": "r",
#         "с": "s",
#         "т": "t",
#         "у": "u",
#         "ф": "f",
#         "х": "h",
#         "ц": "c",
#         "ч": "ch",
#         "ш": "sh",
#         "щ": "shch",
#         "ъ": "",
#         "ы": "y",
#         "ь": "",
#         "э": "e",
#         "ю": "yu",
#         "я": "ya",
#     }
#     return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

# class ActiveManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_published=Users.Status.PUBLISHED)

class Users(models.Model): 

    name = models.CharField(max_length=255, verbose_name="ФИО")
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    qr_qode = models.ImageField(
        upload_to="qr_codes/%Y/%m/%d/",
        default=None,
        blank=True,
        null=True,
        verbose_name="QR код",
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_active = models.BooleanField(default=False, verbose_name="Активен")
    # objects = models.Manager()
    # active = ActiveManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_info", kwargs={"user_slug": self.slug})

    def save(self, *args, **kwargs):
        self.is_active = bool(self.qr_qode)
        super().save(*args, **kwargs)