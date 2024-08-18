from typing import Literal, Union

import platform
import os
import requests
import shutil

class RezPaths():
  install_path: str
  build_path: str

  def __init__(self):
    self.install_path = os.environ["REZ_BUILD_INSTALL_PATH"]
    self.build_path = os.environ["REZ_BUILD_PATH"]

def _prepare_install(path: str) -> None:
  """
  Prepare install.
  """

  print(f"{path=}")

  if os.path.exists(path):
    shutil.rmtree(path)

  os.makedirs(path)

def _build(platform: Union[str, Literal["Linux", "Darwin", "Windows"]]) -> None:
  """
  Build command for Bazelisk.
  """
  file_name: str = ""
  paths = RezPaths()
  
  print({paths.install_path})
  save_path = os.path.join(paths.install_path, "bin")
  print(f"{save_path=}")
  
  _prepare_install(path=save_path)

  print(f"Checking for platform: {platform}")
  if platform == "Linux":
    file_name = "bazelisk-darwin-amd64"
  elif platform == "Darwin":
    file_name = "bazelisk-linux-amd64"
  elif platform == "Windows":
    file_name = "bazelisk-windows-amd64.exe"
  else:
    raise Exception("Platform not supported")
  print(f"Using filename: {file_name}")
  
  url: str = f"https://github.com/bazelbuild/bazelisk/releases/download/v1.20.0/{file_name}"
  
  # Send a GET request to the URL
  response = requests.get(url, stream=True)
  
  # Check if the request was successful
  response.raise_for_status()

  file_path: str = os.path.join(save_path, "bazelisk")

  if platform == "Windows":
    file_path: str = os.path.join(save_path, "bazelisk.exe")
  
  # Open the file in binary write mode
  with open(file_path, 'wb') as file:
    # Download the file in chunks
    for chunk in response.iter_content(chunk_size=8192):
      if chunk:
        file.write(chunk)

  print(f"File downloaded successfully and saved to: {save_path}")

if __name__ == "__main__":
  _build(platform=platform.system())
