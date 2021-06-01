import os
import torch
# from torch.utils.ffi import create_extension

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

sources = ['src/nms.cpp']
headers = ['src/nms.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/nms_cuda.cpp']
    headers += ['src/nms_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = ['src/cuda/nms_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

# ffi = create_extension(
#     '_ext.nms',
#     headers=headers,
#     sources=sources,
#     define_macros=defines,
#     relative_to=__file__,
#     with_cuda=with_cuda,
#     extra_objects=extra_objects
# )

if __name__ == '__main__':
    # ffi.build()
    setup(
        name='_ext.nms',
        ext_modules=[
            CppExtension('_ext.nms', sources=sources),
        ],
        cmdclass={
            'build_ext': BuildExtension
        }
    )
