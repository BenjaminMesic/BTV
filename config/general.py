# ------- General options ----------
# campaign name, needed for list of samples definition, etc...
campaigns       = ['A', 'B']
# Choose True if you want to overwrite already existing files/results
force_all       = False
# If True all files are copied locally and used, else use files from original location
work_locally    = True

# -------- Merge options -----------
# Luminosity (this number doesn't mean anything since data/MC is "manually" scaled)
luminosity      = 1
# Name of the analyzer
analyzer_module = 'btagval'
# Groups for histogram merging
groups          = ['DATA', 'QCD']

# -------- Batch options -----------
# Choose if you want to use batch: False, condor, lxbatch
batch_type      = 'condor' # 'lxbatch' # 
# Number of jobs per sample: -1 = all, x = some arbitrary number
number_of_jobs  = 1
# Number of files per job
number_of_files = 1
# Send jobs switch
send_jobs       = True
# lxbatch options
queue_lxbatch   = '8nh' # LXBatch queue (choose among cmst3 8nm 1nh 8nh 1nd 1nw)
# batch templates
batch_templates = {
  'copy'      : ['copy.txt','copy.py', 'copy.sh'],
  'histogram' : ['histogram.txt','btagvalidation_cfg.py', 'histogram.sh'],
  'check'     : ['check.txt','check.py', 'check.sh'],
}

# -------- Browse/copy options -----------
remote_locations = {
  'storage_element' : {
    'eos' : '/eoscms.cern.ch/', # Used for gfal
    # 'eos' : '/srm-eoscms.cern.ch:8443/srm/v2/server?SFN=', # Used for lcg
  },
  'path'   : {
    'eos' : 'store/group/phys_btag/BoostedBTag/BTagNTuples/2017/9_2_X',   # Used for gfal
    # 'eos' : 'eos/cms/store/group/phys_btag/BoostedBTag/BTagNTuples/2017/9_2_X', # Used for lcg
  },
  'path_ex': {
    'eos' : '/eos/cms/store/group/phys_btag/BoostedBTag/BTagNTuples/2017/9_2_X',   
  },
  'protocol': {
    'eos'  : 'root:/', # Used for gfal
    # 'eos'  : 'srm:/', # Used for lcg
  },
}
# Keywords which are going to be searched (or not) for.
search_keywords = {
  'all' : ['.root'],
  'any' : [],
  'none': ['failed', 'log']
}