#!/usr/bin/env python
# coding: utf-8

# In[1]:


Import pycuda.gpuarray as gpuarray
Import pycuda.driver as drv
Import numpy
from pycuda.scan import InclusiveScanKernel
import pycuda.autoinit
Algoritmos paralelos com PyCUDA10
n=10
start=drv.Event()
end=drv.Event()
start.record()
kernel=InclusiveScanKernel(numpy.uint32,"a+b")
h _ a = numpy.random.randint(1,10,n).astype(numpy.int32)
d _ a=gpuarray.to _ gpu(h _ a)
kernel(d _ a)
end.record()
end.synchronize()
secs = start.time _ till(end)*1e-3
assert(d _ a.get() == numpy.cumsum(h _ a,axis=0)).all()
print("Dado de entrada:")
print(h _ a)
print("Computação cumulative usando SCAN:")
print(d _ a.get())
print(" Soma cumulative na GPU")
print("%fs" % (secs))


# In[ ]:




