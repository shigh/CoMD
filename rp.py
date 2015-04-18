import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from glob import glob

p_all_ranks_res = \
r"""  Timer: (?P<function>.+)
    MinRank: (?P<minrank>\d+)
    MinTime:  (?P<mintime>.+)
    MaxRank: (?P<maxrank>\d+)
    MaxTime:  (?P<maxtime>.+)
    AvgTime:  (?P<avgtime>.+)
    StdevTime:   (?P<stddevtime>.+)
"""

p_r0_res = \
r"""Timer: (?P<function>.+)
    CallCount:  (?P<callcount>\d+)
    AvgPerCall: (?P<avgpercall>.+)
    Total:      (?P<total>.+)
    PercentLoop:(?P<percentloop>.+)
"""

p_cmd = \
r"""Command Line Parameters:
  doeam: (?P<doeam>\d)
  potDir: pots
  potName: Cu_u6.eam
  potType: funcfl
  nx: (?P<nx>\d+)
  ny: (?P<ny>\d+)
  nz: (?P<nz>\d+)
  xproc: (?P<xproc>\d+)
  yproc: (?P<yproc>\d+)
  zproc: (?P<zproc>\d+)
  Lattice constant: -1 Angstroms
  nSteps: (?P<nsteps>\d+)
  printRate: (?P<printRate>\d+)
  Time step: (?P<timestep>\d+) fs
  Initial Temperature: 600 K
  Initial Delta: 0 Angstroms
"""

p_sim_data = \
r"""Simulation data: 
  Total atoms        : (?P<totalatoms>\d+)
"""

p_decomp_data = \
r"""Decomposition data:.*
  Processors         :\s*(?P<px>\d+),\s*(?P<py>\d+),\s*(?P<pz>\d+).*
  Local boxes        :\s*(?P<lbx>\d+),\s*(?P<lby>\d+),\s*(?P<lbz>\d+).*
"""

p_mem_data = \
r"""Memory data:.*
  Intrinsic atom footprint = \s*(?P<intrinsatomfp>\d+)\s*B/atom\s*
  Total atom footprint     =(?P<totatomfp>.+) MB \((?P<totatomfpn>.+)MB/node\)
  Link cell atom footprint =(?P<linkcellatomfp>.+) MB/node\s*
  Link cell atom footprint =(?P<linkcellatomfphalo>.+) MB/node.*
"""

p_perf_res = \
r"""Performance Results:
  TotalRanks: (?P<totalranks>\d+)
"""

def clean_dict(d):
    for k,v in d.iteritems():
        d[k] = v.strip()
    return d

class ResultsParser(object):
    
    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as f:
            self.res = f.read()
        self.parse_cmd()
        self.parse_sim_data()
        self.parse_r0()
        self.parse_all_ranks()
        
    def parse_cmd(self):
        r = re.search(p_cmd, self.res)
        self.res_cmd = clean_dict(r.groupdict())
        
    def parse_sim_data(self):
        res_sim_data = {}
        for p in [p_cmd,
                  p_sim_data,
                  p_decomp_data,
                  p_mem_data,
                  p_perf_res]:
            
            r = re.search(p, self.res)
            if r==None:
                raise ValueError("Failed to parse %s\n%s\n"%\
                                 (self.file_name, p))
            res_sim_data.update(clean_dict(r.groupdict()))
        
        self.sim_data = res_sim_data
        
    def parse_r0(self):
        r = re.finditer(p_r0_res, self.res)
        if r==None:
           raise ValueError("Failed to parse %s\n%s\n"%\
                            (self.file_name, p_r0_res))
        
        r0_res = []
        for i in r:
            r0_res.append(clean_dict(i.groupdict()))
        self.r0_res = r0_res
        
    def parse_all_ranks(self):
        r = re.finditer(p_all_ranks_res, self.res)
        if r==None:
            raise ValueError("Failed to parse %s\n%s\n"%\
                             (self.file_name, p_all_ranks_res))
            
        all_ranks_res = []
        for i in r:
            all_ranks_res.append(clean_dict(i.groupdict()))
        self.all_ranks_res = all_ranks_res

    def results_r0(self):
        
        res = []
        for r in self.r0_res:
            i = {}
            i["file_name"] = self.file_name
            i.update(self.sim_data)
            i.update(r)
            res.append(i)
        
        return res
    
    def results_all_ranks(self):
        
        res = []
        for r in self.all_ranks_res:
            i = {}
            i["file_name"] = self.file_name
            i.update(self.sim_data)
            i.update(r)
            res.append(i)
        
        return res
            