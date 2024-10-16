import argparse
import re
from functools import wraps
import inspect
import secrets
from typing import Callable
from typing_extensions import Annotated
import typer

import pandas as pd

# from main import function_tool
from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools import function_tool


@function_tool(
    description="Prints pandas {name}!",
    requirements=["pandas==2.2.3"],
)
def test_123(
    name: str,
    boolean_val: bool,  # This will validate that the input is a boolean
    optional_str: Annotated[
        str, typer.Argument()
    ] = "sheeesh",  # This is how to add a default value
):
    import pandas as pd

    print(f"Hello {name}! {boolean_val} {optional_str}")
    df = pd.DataFrame(
        {"name": [name], "boolean_val": [boolean_val], "test": [optional_str]}
    )

    print(df)


@function_tool(
    description="Greats a person via llm {name}!",
    requirements=["litellm==1.49.4"],
    env=["LLM_BASE_URL"],
    secrets=["LLM_API_KEY"],
)
def litellm_hello_world(
    name: str,
):
    import os
    import litellm

    llm_key = os.environ["LLM_API_KEY"]
    llm_base_url = os.environ["LLM_BASE_URL"]

    try:
        response = litellm.completion(
            model="openai/gpt-4o",
            api_key=llm_key,
            base_url=llm_base_url,
            messages=[
                {
                    "content": f"Your task it to great people in a random movie star way, you must say which movie star you choose",
                    "role": "system",
                },
                {"content": f"My name is {name}, greet me!", "role": "user"},
            ],
        )
    except Exception as e:
        print(e)
        return

    print(response.choices[0].message.content)
