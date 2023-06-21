import numpy as np
import pandas as pd
import rdkit
from rdkit.Chem import Descriptors

def Rdescriptor():

    desc_list = Descriptors.descList
    xyz = pd.read_csv('rdkit/smiles.csv')
    asd=xyz.iloc[:,1]
    smiles=[]
    for i in range(len(asd)):
        B=xyz.iloc[i, 1]
        smiles.append(B)
    #smiles = ["CCO", "CCC", "CC", "CCCCC","CCCCCCCCO"]
    mols = []
    for i in smiles:
        mol = rdkit.Chem.MolFromSmiles(i)
        mols.append(mol)

    df = pd.DataFrame(mols)
    df.columns = ["ROMol"]
    rdkit_desc = pd.concat([df["ROMol"].map(j) for _, j in desc_list], axis=1)
    rdkit_desc.columns = [i for i, _ in desc_list]
    rdkit_desc.insert(0, "SMILES", pd.Series(smiles))
    rdkit_desc.to_csv('rdkit_to_user/rdkit_descriptor.csv')

    return rdkit_desc