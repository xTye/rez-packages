# rez-packages

My personal rez packages

---

# Bootstrap

Install Python 3.11.9 for all users and add to path.
https://www.python.org/downloads/release/python-3119/

Set environment variables:

```
REZ_CONFIG_FILE             (ex. rez-packages/config.py)
REZ_LOCAL_PACKAGES_PATH     (ex. ~/rez/build)
REZ_PACKAGES_PATH           (ex. ~/rez/build;~/rez/release)
REZ_RELEASE_PACKAGES_PATH   (ex. ~/rez/release)
```

Install to the release path

`rez-bind --quickstart -r`

Navigate to `rez-packages/python/3.11.9` and `rez build -ci`

This will fix issues rez-pip in the future (it removes the symlink dependency resolve).
