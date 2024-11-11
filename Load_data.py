#Created on Thu Oct 31 19:48:25 2024
#@author: MaartenvZw

# Python code to load up test data Master thesis Maarten van der Zwaan

import numpy as np #Code built on numpy version 1.26.4

# Choose dataset number
dataset_number = "1"

# Load the .npz file
data = np.load("dataset" + dataset_number + ".npz", allow_pickle=True)  # Replace with the actual filename

# Access the arrays
N = int(data['N'])
D = int(data['D'])
O = int(data['O'])
O_d = data['O_d']
S = int(data['S'])
V = int(data['V'])
C = int(data['C'])
K = int(data['K'])
WINTER_n = data['WINTER_n']
SIX_ROW_n = data['SIX_ROW_n']
STDG = data['DG']
VB_vn = data['VB_vn']
OQ_od = data['OQ_od']
KG_n = data['KG_n']
U_nod = data['U_nod']
CH_nc = data['CH_nc']
SV_ns = data['SV_ns']
VAR_AMOUNT_MAX_od = data['VAR_AMOUNT_MAX_od']
VAR_AMOUNT_MIN_od = data['VAR_AMOUNT_MIN_od']
WINTER_MAX_od = data['WINTER_MAX_od']
WINTER_MIN_od = data['WINTER_MIN_od']
SIX_ROW_MAX_od = data['SIX_ROW_MAX_od']
SIX_ROW_MIN_od = data['SIX_ROW_MIN_od']
SPRING_MAX_od = data['SPRING_MAX_od']
SPRING_MIN_od = data['SPRING_MIN_od']
TWO_ROW_MAX_od = data['TWO_ROW_MAX_od']
TWO_ROW_MIN_od = data['TWO_ROW_MIN_od']
VAR_MAX_vod = data['VAR_MAX_vod']
VAR_MIN_vod = data['VAR_MIN_vod']
CUSTMAX_sod = data['CUSTMAX_sod']
CUSTMIN_sod = data['CUSTMIN_sod']
HMMAX_sod = data['HMMAX_sod']
HMMIN_sod = data['HMMIN_sod']
NE_n = data['NE_n']
F_n = data['F_n']
BS_nm = data['BS_nm']
SAS = data['SAS']
IG_ng = data['IG_ng']
normalization_s = data['normalization_s']
OBJ_SCORE = data['OBJ_SCORE']
TO_EMPTY_d = [2 * (d+1) for d in range(D)] # Added after data collection, so default values are assumed