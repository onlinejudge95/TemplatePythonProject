from pytest import mark

from src import template_python_project


@mark.asyncio
async def test_hello_returns():
    response = await template_python_project.hello()
    assert "hello" in response.lower()
