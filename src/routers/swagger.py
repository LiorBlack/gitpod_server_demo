from actions.html_generator import get_oauth2_redirect
from actions.html_generator import get_swagger_html
from fastapi.responses import RedirectResponse
from fastapi.routing import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/swagger/index.html", include_in_schema=False)
async def swagger_ui_html(req: Request) -> HTMLResponse:
    root_path = req.scope.get("root_path", "").rstrip("/")
    swagger_html = get_swagger_html(root_path)
    return HTMLResponse(swagger_html)


@router.get("/swagger/oauth2-redirect.html", include_in_schema=False)
async def swagger_oauth2_redirect() -> HTMLResponse:
    swagger_html = get_oauth2_redirect()
    return HTMLResponse(swagger_html)


@router.get("/", include_in_schema=False)
def redirect_to_swagger():
    response = RedirectResponse(url="/swagger/index.html")
    return response
