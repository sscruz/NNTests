import ROOT as r 
from root_numpy import tree2array
from root_pandas import read_root
import pandas as pd



def load_big_data(file, vars):
    datos=pd.DataFrame()
    for i in read_root(file, 'MiniTree', columns=vars, chunksize=100000, where='TChannel==1 & TNJets >= 2 & TNBtags >= 1 & TPassTrigger & TPassMETFilters & TNSelLeps == 2 & TLep0Pt >= 25 & TJet1Phi!=0'):
        datos=pd.concat([datos,i],axis=0)
    return datos

def load_data(file, vars):
    
    try: tfile = r.TFile.Open(file)
    except: raise 

    try: ttree = tfile.Get('MiniTree')
    except: raise

    arr = tree2array(ttree)
    return pandas.DataFrame(arr, columns=vars)

