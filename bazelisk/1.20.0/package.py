name = "bazelisk"

version = "1.20.0"

description = "Bazelisk bootstrap"

tools = [
  "bazel",
  "bazelisk"
]

build_requires = [
  "requests",
]

build_command = "python {root}/build.py"

def commands():
  env.PATH.append("{root}/bin")
