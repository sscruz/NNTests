import ROOT as r 
import pandas as pd
from root_numpy import tree2array

tf = r.TFile.Open("higgs_reco.root")
arr = tree2array( tf.Get("Friends") ) 

df = pd.DataFrame( arr ) 
df.to_hdf("higgs_reco.hdf",'df',mode='w')
