def get_appname() -> str:
    """for settings"""
    return "django_layui29"


def get_layui_from_local(request):
    """
    自定义上下文处理器，用于在模板中访问 LAYUI_FROM_LOCAL 设置。
    """
    from django.conf import settings

    return {"LAYUI_FROM_LOCAL": getattr(settings, "LAYUI_FROM_LOCAL", False)}
