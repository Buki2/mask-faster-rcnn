import os
import torch
# from torch.utils.ffi import create_extension
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

sources = ['src/roi_pooling.cpp']
headers = ['src/roi_pooling.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/roi_pooling_cuda.cpp']
    headers += ['src/roi_pooling_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = ['src/cuda/roi_pooling_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

# ffi = create_extension(
#     '_ext.roi_pooling',
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
        name='_ext.roi_pooling',
        ext_modules=[
            CppExtension('_ext.roi_pooling', sources=sources),
        ],
        cmdclass={
            'build_ext': BuildExtension
        }
    )
