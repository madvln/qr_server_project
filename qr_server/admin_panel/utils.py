menu = [
    {"title": "Добавить", "url_name": "add_user"},
]

class DataMixin:
    def get_mixin_context(self, context, **kwargs):
        context["menu"] = menu
        context.update(kwargs)
        return context