import pytest
from django.test import override_settings
from django.urls import reverse


# 将测试标记为使用 Django 数据库
@pytest.mark.django_db
def test_layui_loaded_from_local(client):
    """
    测试当 LAYUI_FROM_LOCAL=True 时，layui.js 是否从本地加载。
    """
    # 覆盖 Django 设置
    with override_settings(LAYUI_FROM_LOCAL=True):
        # 访问 /normal/ 页面
        url = reverse("normal")
        response = client.get(url)

        # 检查 HTTP 状态码
        assert response.status_code == 200

        # 将响应内容解码为字符串
        content = response.content.decode("utf-8")

        # 断言 layui.js 的路径是本地路径
        assert 'src="/static/layui29/layui.js"' in content
        # 断言 layui.css 的路径是本地路径
        assert 'href="/static/layui29/css/layui.css"' in content
        # 确认不包含 CDN 路径
        assert "//unpkg.com/layui" not in content


@pytest.mark.django_db
def test_layui_loaded_from_cdn(client):
    """
    测试当 LAYUI_FROM_LOCAL=False 时，layui.js 是否从 CDN 加载。
    """
    with override_settings(LAYUI_FROM_LOCAL=False):
        url = reverse("normal")
        response = client.get(url)

        assert response.status_code == 200
        content = response.content.decode("utf-8")

        # 断言 layui.js 的路径是 CDN 路径
        assert 'src="//unpkg.com/layui' in content
        # 断言 layui.css 的路径是 CDN 路径
        assert 'href="//unpkg.com/layui' in content
        # 确认不包含本地静态路径
        assert "/static/layui29/layui.js" not in content
