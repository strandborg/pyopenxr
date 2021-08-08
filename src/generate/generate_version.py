# This script creates an updated version of xr/version.py

import re
import inspect
import xrg

# These variables are filled in by cmake's configure_file process
try:
    pyopenxr_patch = int("@PYOPENXR_VERSION_PATCH_INCREMENTAL@")
except ValueError:
    pyopenxr_patch = 1

file_string = xrg.get_header_as_string()

# We expect a line in openxr.h like
#   "#define XR_CURRENT_API_VERSION XR_MAKE_VERSION(1, 0, 17)"
version_match = re.search(
    r"define XR_CURRENT_API_VERSION XR_MAKE_VERSION\((\d+), (\d+), (\d+)\)",
    file_string
)

major = int(version_match.group(1))
minor = int(version_match.group(2))
patch = int(version_match.group(3))
# funny way to merge two different patch numbers
patch2 = 100 * patch + pyopenxr_patch

print("# Warning: this file is automatically generated. Do not edit.\n")
print(inspect.cleandoc(
    f"""
    # pyopenxr version is based on openxr version...
    # except the patch number is:
    #   100 * openxr patch number + pyopenxr patch number

    XR_VERSION_MAJOR = {major}
    XR_VERSION_MINOR = {minor}
    XR_VERSION_PATCH = {patch}
    XR_CURRENT_API_VERSION = "{major}.{minor}.{patch}"

    PYOPENXR_VERSION_MAJOR = {major}
    PYOPENXR_VERSION_MINOR = {minor}
    PYOPENXR_VERSION_PATCH = {patch2}
    PYOPENXR_VERSION_PATCH_INCREMENTAL = {pyopenxr_patch}
    PYOPENXR_VERSION = "{major}.{minor}.{patch2}"

    __version__ = PYOPENXR_VERSION

    __all__ = [
        "XR_VERSION_MAJOR",
        "XR_VERSION_MINOR",
        "XR_VERSION_PATCH",
        "XR_CURRENT_API_VERSION",
        "PYOPENXR_VERSION_MAJOR",
        "PYOPENXR_VERSION_MINOR",
        "PYOPENXR_VERSION_PATCH",
        "PYOPENXR_VERSION_PATCH_INCREMENTAL",
        "PYOPENXR_VERSION",
    ]
    """))

