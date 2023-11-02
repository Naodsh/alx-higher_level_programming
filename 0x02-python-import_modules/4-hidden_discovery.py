if __name__ == "__main__":
    import py_compile
    import sys

try:
    module = py_compile.load_compiled("hidden_4", "hidden_4.pyc")
except FileNotFoundError:
    sys.exit(1)

module_attributes = dir(module)

filtered_names = [name for name in module_attributes if not name.startswith("__")]
filtered_names.sort()

for name in filtered_names:
    print(name)
