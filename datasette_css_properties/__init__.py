from datasette import hookimpl
from datasette.utils.asgi import Response
from datasette.utils import escape_css_string, to_css_class


def css_response(css):
    return Response(css, content_type="text/css; charset=utf-8")


def render_css(request, rows):
    try:
        row = rows[0]
    except IndexError:
        return css_response("")
    raw_keys = request.args.getlist("_raw")
    lines = [":root {"]
    for key, value in dict(row).items():
        if key not in raw_keys:
            value = "'{}'".format(
                escape_css_string(str(value) if value is not None else "")
            )
        lines.append("  --{}: {};".format(to_css_class(key), value))
    lines.append("}")
    return css_response("\n".join(lines))


@hookimpl
def register_output_renderer(datasette):
    return {
        "extension": "css",
        "render": render_css,
    }
