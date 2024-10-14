from . import main

import inspect


from kubiya_sdk.tools.models import Tool, Arg, FileSpec
from kubiya_sdk.tools.registry import tool_registry

pandas = Tool(
    name="pandas",
    type="docker",
    image="python:3.12",
    description="does pandas things {name}!",
    args=[Arg(name="name", description="name for pandas", required=True)],
    content="""
python /tmp/main.py "{{ .name }}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
    ],
)

tool_registry.register("pandas", pandas)
