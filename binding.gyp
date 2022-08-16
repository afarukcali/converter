{
    "targets": [{
        "target_name": "hex-resolver",
        "cflags!": [ "-fno-exceptions" ],
        "cflags": [ "-std=c++11" ],
        "cflags_cc!": [ "-fno-exceptions" ],
        "sources": [
            "Bytestring.cpp",
            "Bytestring.hpp",
            "byteswap.h",
            "common.h",
            "cpuid.h",
            "endian.h",
            "hex-resolver.cpp",
            "sha256.cpp",
            "sha256.h"
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")",
        ],
        "libraries": [],
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")",
        ],
        'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }]
}