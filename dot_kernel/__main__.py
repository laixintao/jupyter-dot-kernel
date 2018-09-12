from .kernel import DotKernel
from ipykernel.kernelapp import IPKernelApp

IPKernelApp.launch_instance(kernel_class=DotKernel)
