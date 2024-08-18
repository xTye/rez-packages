from typing import Literal, Union

import platform
import os
import requests
import shutil
import zipfile

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
  paths = RezPaths()
  
  print({paths.install_path})
  save_path = os.path.join(paths.install_path, "bin")
  print(f"{save_path=}")
  
  _prepare_install(path=save_path)
  
  url: str = f"https://github.com/coreybutler/nvm-windows/releases/download/1.1.12/nvm-noinstall.zip"
  
  # Send a GET request to the URL
  response = requests.get(url, stream=True)
  
  # Check if the request was successful
  response.raise_for_status()

  file_path: str = os.path.join(save_path, "nvm.zip")

  # Open the file in binary write mode
  with open(file_path, 'wb') as file:
    # Download the file in chunks
    for chunk in response.iter_content(chunk_size=8192):
      if chunk:
        file.write(chunk)

  print(f"File downloaded successfully and saved to: {save_path}")
  print(f"Unzipping zip")

  with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(save_path)

  print(f"Deleting file...")
  os.remove(file_path)

  settings_file_name: str = os.path.join(save_path, "settings.txt")
  print(f"Creating {settings_file_name=}")

  with open(settings_file_name, 'w') as file:
    file.write(f"root: {os.path.join(paths.install_path, 'bin')}\n")
    file.write(f"path: {os.path.join(paths.install_path, 'bin', 'node')}\n")
    file.write(f"proxy: none\n")
    file.write(f"arch: 64\n")

if __name__ == "__main__":
  _build(platform=platform.system())
