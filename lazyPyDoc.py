"""lazyPyDoc by sm0lt4nkCraft

Print each docstring with markdown formatting.

Usage in console, save output: 
    lazyPyDoc.py module_name >> README.md
"""
import argparse
import inspect


def print_docs(module_name: str) -> None:
    """Get docstring form each class and function.
    Add markdown formatting.

    :params module_name: Module name without .py extension.
    :type module_name: str
    """
    for name, obj in inspect.getmembers(__import__(args.module_name)):
        if inspect.isclass(obj):
            docstring = inspect.getdoc(obj)
            if docstring:
                print(f"## CLASS: {name}\n", "```\n", docstring, "\n```", "\n\n")

            for name, func in inspect.getmembers(obj):
                if inspect.isfunction(func):
                    print(f"\n#### FUNC: {name}\n", "```\n", inspect.getdoc(func), "\n```", "\n")

        if inspect.isfunction(obj):
            docstring = inspect.getdoc(obj)
            if docstring:
               print(f"\n#### FUNC: {name}\n", "```\n", docstring, "\n```", "\n") 


if __name__ == "__main__":
    # CLI args.
    parser = argparse.ArgumentParser(prog="lazyPyDoc", description="Print each docstring with markdown formatting.")
    parser.add_argument("module_name", help="Module name without .py extension.")
    args = parser.parse_args()
    
    print_docs(args.module_name)
