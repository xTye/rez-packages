name = "nvm_windows"

version = "1.1.12"

description = "NVM library for managing node packages on Windows"

tools = [
  "node",
  "nvm-windows",
]

build_requires = [
  "bazel"
]

build_command = "python {root}/build.py"

def commands():
  env.NVM_HOME = "{root}/bin"
  env.NVM_SYMLINK = "{root}/bin/node"

  env.PATH.append("{env.NVM_HOME}")
  env.PATH.append("{env.NVM_SYMLINK}")
