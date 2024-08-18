name = "bazel"

version = "7.3.0"

description = "Bazel for building rez packages"

tools = [
  "bazel",
  "build",
]

requires = [
  "bazelisk"
]

build_command = ""

def commands():
  env.USE_BAZEL_VERSION = "{version}"

  alias("bazel", "bazelisk")
