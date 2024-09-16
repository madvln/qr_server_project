from django.db import models
from django.utils.text import slugify

from .utils import generate_unique_slug


def translit_to_eng(s: str) -> str:
    d = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "yo",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class UsersManager(models.Manager):
    def filter_users(self, request):
        queryset = self.get_queryset()
        search_query = request.GET.get("search")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        status_filter = request.GET.get("status")
        if status_filter == "active":
            queryset = queryset.filter(is_active=True)
        elif status_filter == "inactive":
            queryset = queryset.filter(is_active=False)

        return queryset


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
    objects = UsersManager()
    # active = ActiveManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user_info", kwargs={"user_slug": self.slug})

    def save(self, *args, **kwargs):
        # Автоматическая генерация slug
        if not self.slug:
            transliterated_name = translit_to_eng(self.name)
            new_slug = slugify(transliterated_name)
            self.slug = generate_unique_slug(new_slug, Users)
        # Проверка статуса по наличию QR-кода
        self.is_active = bool(self.qr_qode)
        super().save(*args, **kwargs)
