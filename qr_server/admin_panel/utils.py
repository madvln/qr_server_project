from django.utils.text import slugify

menu = [
    {"title": "Добавить", "url_name": "add_user"},
]


class DataMixin:
    title_page = None

    def get_mixin_context(self, context, **kwargs):
        context["menu"] = menu
        context["title"] = self.title_page or ""
        context.update(kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)


def generate_unique_slug(slug_base, model):
    slug = slug_base
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{slug_base}-{counter}"
        counter += 1
    return slug
