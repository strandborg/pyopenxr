# This script creates an updated version of xr/platform/windows.py

import inspect

import xrg


def main():
    compiler_args = [
        "-DXR_USE_GRAPHICS_API_OPENGL",
        "-DXR_USE_GRAPHICS_API_VULKAN",
        "-DXR_USE_PLATFORM_WAYLAND",
        "-DXR_USE_PLATFORM_XCB",
        "-DXR_USE_PLATFORM_XLIB",
        "-DXR_USE_TIMESPEC",
    ]
    cg = xrg.CodeGenerator(
        header=xrg.Header.PLATFORM,
        compiler_args=compiler_args,
        header_preamble=inspect.cleandoc("""
            #include <Windows.h>
        """),
    )

    cg.print_header()
    print(inspect.cleandoc("""
        from ..enums import *
        from ..typedefs import *
        from ..version import *


        # Forward declaration of a Wayland structure
        class wl_display(Structure):
            pass
    """))
    print("\n")
    cg.print_items()
    cg.print_all_list()


if __name__ == "__main__":
    main()
