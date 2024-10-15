import argparse
import re
from functools import wraps
import inspect
from typing import Callable
import pandas as pd

# from main import function_tool
from kubiya_sdk.tools.models import Arg, Tool, FileSpec
from kubiya_sdk.tools import function_tool


@function_tool(
    description="Prints pandas {name}!",
    requirements="""
pandas==2.2.3
""",
)
def test_123(name: str, bla: bool, test: str = "sheeesh"):
    import pandas as pd

    print(f"Hello {name}! {bla} {test}")
    df = pd.DataFrame({"name": [name]})

    print(df)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Pandas {name}!")
#     parser.add_argument("name", help="Name to say hello to")

#     # Parse command-line arguments
#     args = parser.parse_args()

#     # Get coordinates for the given city
#     name = args.name

#     pandas(name)
