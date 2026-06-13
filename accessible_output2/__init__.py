from __future__ import absolute_import
import ctypes
import types
from pathlib import Path

lib = Path(__file__).parent / "lib"


def load_library(libname, cdll=False):

    lib_path = lib / libname
    libfile = str(lib_path)
    if cdll:
        return ctypes.cdll[libfile]
    return ctypes.windll[libfile]


def get_output_classes():
    from . import outputs

    module_type = types.ModuleType
    classes = [
        m.output_class
        for m in outputs.__dict__.values()
        if isinstance(m, module_type) and hasattr(m, "output_class")
    ]
    return sorted(classes, key=lambda c: c.priority)
