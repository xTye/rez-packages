name = "python"

version = "3.11.9"

description = "Standard python package with no build for 3.11.9"

tools = [
  "python"
]

build_command = ""

def commands():
  python_path = "E:/Python/Python311"

  env.PATH.prepend('{python_path}')
  env.PYTHONPATH.prepend('{python_path}/Scripts')
