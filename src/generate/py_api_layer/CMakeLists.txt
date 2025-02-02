find_file(LOADER_INTERFACES_H
    NAMES loader_interfaces.h
    HINTS
        "$ENV{USERPROFILE}/Documents/git//OpenXR-SDK-Source"
        "$ENV{HOME}/git/OpenXR-SDK-Source"
    PATH_SUFFIXES src/common
    DOC "Header file for C API layer development"
)
if(LOADER_INTERFACES_H)
    configure_file(
        "${LOADER_INTERFACES_H}"
        "${CMAKE_CURRENT_SOURCE_DIR}/"
        @ONLY
        NEWLINE_STYLE LF  # Even/especially on windows...
    )
endif()

add_library(XrApiLayer_python SHARED py_api_layer.cpp loader_interfaces.h)

if (WIN32)
    install(
        TARGETS XrApiLayer_python
        RUNTIME  # dll only?
        DESTINATION ${CMAKE_SOURCE_DIR}/../xr/api_layer/windows
    )
else()
    set_target_properties(XrApiLayer_python PROPERTIES LINK_FLAGS "-Wl,-Bsymbolic,--exclude-libs,ALL")
    install(
        TARGETS XrApiLayer_python
        DESTINATION ${CMAKE_SOURCE_DIR}/../xr/api_layer/linux
    )
endif()
