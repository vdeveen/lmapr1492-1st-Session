#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymatgen.io.cif import CifParser
parser = CifParser("Ba2PCl_mp-27869_symmetrized.cif")
structure = parser.get_structures()[0]

# Read a POSCAR and write to a CIF.
structure = Structure.from_file("POSCAR")
structure.to(filename="CsCl.cif")


# In[ ]:




