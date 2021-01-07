from datasette.app import Datasette
import pytest
import urllib


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "query,raw,expected_css",
    [
        (
            "select 'hello' as foo, 2 as bar, null as baz",
            [],
            ":root {\n  --foo: 'hello';\n  --bar: '2';\n  --baz: '';\n}",
        ),
        (
            """select 'hello '' this has quotes '' ' as foo""",
            [],
            ":root {\n  --foo: 'hello \\000027 this has quotes \\000027 ';\n}",
        ),
        ("select 'hello' as foo", ["foo"], ":root {\n  --foo: hello;\n}"),
    ],
)
async def test_css_output(query, raw, expected_css):
    datasette = Datasette([], memory=True)
    response = await datasette.client.get(
        "/:memory:.css?"
        + urllib.parse.urlencode(
            {
                "sql": query,
                "_raw": raw,
            },
            doseq=True,
        )
    )
    assert response.status_code == 200
    assert response.text == expected_css
    assert response.headers["x-content-type-options"] == "nosniff"
