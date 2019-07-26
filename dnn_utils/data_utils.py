import ROOT as r 
from root_numpy import tree2array
import pandas

def load_data(file, vars):
    try: tfile = r.TFile.Open(file)
    except: raise 
    
    try: ttree = tfile.Get('Friends')
    except: raise

    arr = tree2array(ttree)
    return pandas.DataFrame(arr, columns=vars)
