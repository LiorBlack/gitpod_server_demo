from functools import lru_cache
from pathlib import Path

from common.environment import APP_TITLE
from common.environment import HTML_TEMPLATE_DIR
from common.environment import OAUTH_CLIENT_ID
from common.jinja2_utils import get_jinja_env
from common.jinja2_utils import get_root_template_dir
from jinja2.environment import Template


@lru_cache(maxsize=None)
def get_swagger_html(root_path: str) -> str:
    openapi_url = root_path + "/openapi.json"
    oauth2_redirect_url = root_path + "/swagger/oauth2-redirect.html"
    template: Template = get_jinja_env(
        get_root_template_dir(HTML_TEMPLATE_DIR)
    ).get_template("swagger.html")
    return template.render(
        {
            "title": APP_TITLE,
            "openapi_url": openapi_url,
            "oauth2_redirect_url": oauth2_redirect_url,
            "oauth_client_id": OAUTH_CLIENT_ID,
            "swagger_js_url": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui-bundle.js",
            "swagger_css_url": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui.css",
            "swagger_favicon_url": "https://liorplayground.mooo.com/favicon.ico",
        }
    )


@lru_cache(maxsize=None)
def get_oauth2_redirect() -> str:
    template: Template = get_jinja_env(
        get_root_template_dir(HTML_TEMPLATE_DIR)
    ).get_template("oauth2-redirect.html")
    return template.render()
