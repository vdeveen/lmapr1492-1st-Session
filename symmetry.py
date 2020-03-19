#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pymatgen import Structure
from pymatgen import symmetry
from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifWriter
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.operations import SymmOp
from IPython.display import Image
with MPRester("izD7mJmnjhUOKyWGtZ") as m:

    # Structure for material id
    structure = m.get_structure_by_material_id("mp-27869")
    w = CifWriter(structure)
    w.write_file('mp-27869.cif')
    sGP= SpacegroupAnalyzer(structure)
    print("2ème élément de symétrie (Ci:0 0 0):")
    Op1=SymmOp.from_xyz_string("-x, -y, -z") 
    print("Effet sur P1 #2:")
    Eff1=Op1.operate((0,0,1/2))
    print(Eff1)
    display(Image(filename='sym1.jpg'))
    print("4ème élément de symétrie (3-bar axis:y,-x+y,-z):")
    Op2=SymmOp.from_xyz_string("y,-x+y,-z") 
    print("Effet sur BaO1 #4:")
    Eff2=Op2.operate((0,0,0.24))
    print(Eff2)
    display(Image(filename='sym2.jpg'))
    print("5ème élément de symétrie (3-bar axis:-x+y,-x,z):")
    Op3=SymmOp.from_xyz_string("-x+y,-x,z") 
    print("Effet sur BaO6 #5:")
    Eff3=Op3.operate((0.67,0.33,0.57))
    print(Eff3)
    display(Image(filename='sym3.jpg'))
    #print(sGP.get_symmetry_operations())
    
    ###Operation 2 :Rot:
    #[[-1.  0.  0.]
     #[ 0. -1.  0.]
     #[ 0.  0. -1.]] and tau [0. 0. 0.]
   ### Operation 4 Rot:
    #[[ 0.  0. -1.]
    #[-1.  0.  0.]
    #[ 0. -1.  0.]]
    #tau
    #[0. 0. 0.]
### Operation 5 Rot:
    #[[0. 1. 0.]
    # [0. 0. 1.]
    # [1. 0. 0.]]
    #tau
    #[0. 0. 0.]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




