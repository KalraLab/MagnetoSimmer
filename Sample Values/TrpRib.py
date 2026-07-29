#  USER INPUTS  —  edit ONLY this cell, then run the notebook


# Naming the radical pair (this label is reused in every output filename)
radicalPairName = "TrpRib"


# Isotropic electron g-values
g1 = 2.00277     # Donor radical    (electron 1)
g2 = 2.00367     # Acceptor radical (electron 2)


# Hyperfine couplings, entered as (I, a_iso in MHz)
# Using I = 0.5 for H-1 / P-31, and I = 1 for N-14.
# Commenting out a line removes that nucleus from the simulation.

nucleiRadical1 = [
    (0.5, 37.72790),
    (0.5, -16.00730),
]

nucleiRadical2 = [
    (1, 20.41894),
    (0.5, 17.71863),
    (0.5, 16.80610)
]


# Spin-relaxation rate (s^-1)
k_relax = 1.0e6


# Grid-search settings (finding the rate constants that maximise the MFE)
B_grid    = 50.0e-6     # Fixed field used during the grid search (Tesla)
grid_size = 15          # Number of points per axis (total points = grid_size^2)
log_kS_min, log_kS_max = 5, 7   # Scanning kS over 10^5 ... 10^8 s^-1
log_kC_min, log_kC_max = 5, 7   # Scanning kC over 10^5 ... 10^8 s^-1


# MARY-curve settings (final field sweep at the optimal rates)
B_max_mT   = 30e-3      # Field end-point in mT (sweeping from 0 up to this value)
n_low = 200         # Number of data points in low-field region  (0-1 mT)
n_mid = 100         # Number of data points in mid-field region  (1-10 mT)
n_high = 50         # Number of data points in high-field region (10 mT-B_max)

# Building the output file names from the radical-pair label
csv_grid  = f"{radicalPairName}_MFE_Grid.csv"
png_grid  = f"{radicalPairName}_MFE_Grid.png"
csv_mary  = f"{radicalPairName}_MARY.csv"
png_mary  = f"{radicalPairName}_MARY.png"

print(f"Radical pair      : {radicalPairName}")


# Computing the Hilbert-space dimensions of the full spin system
# (2 electrons, each spin-1/2, plus every coupled nucleus with dimension 2I+1)
N = 2*2            # Starting from the two electrons
dims = [2, 2] + [int(2*I+1) for I,_ in nucleiRadical1] \
              + [int(2*I+1) for I,_ in nucleiRadical2]
N = int(np.prod(dims))   # Total Hilbert-space dimension
print(f"Hilbert Space        : {N}x{N}")
print(f"Liouville Space      : {N*N}x{N*N}")
