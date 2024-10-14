import argparse
import pandas as pd


def pandas(name: str):
    df = pd.DataFrame({"name": [name]})

    print(df)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pandas {name}!")
    parser.add_argument("name", help="Name to say hello to")

    # Parse command-line arguments
    args = parser.parse_args()

    # Get coordinates for the given city
    name = args.name

    pandas(name)
