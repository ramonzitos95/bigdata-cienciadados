#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pycuda.driver as drv
import pycude.autoinit

from pycuda.compiler import SourceModule

mod = SourceModule("""
    #include <stdio.h>
    _ _ global _ _ void primeiro _ kernel()
    {
        printf("Bloco numero: %d \\n", blockIdx.x);
    }
""")

function=mod.get_funcion("primeiro kernel")
function(grid=(4,1), block=(1,1,1))


# In[ ]:





# In[ ]:




