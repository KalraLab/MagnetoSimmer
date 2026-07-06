# MagnetoSimmer: MFE on Radical-Pair Reaction Yields
This repository contains the code used for our publication from The Kalra Lab. The Jupyter Notebook `MagnetoSimmer.ipynb` simulates how the product yield of a singlet-born radical pair changes when an external magnetic field is applied. The primary output is a Magnetically Altered Reaction Yield (MARY) curve.

## Features
* **Rate-Constant Grid Search:** The script sweeps $k_S$ and $k_C$ over logarithmic ranges to find the exact rate constants that maximize the magnetic field effect at a given baseline field.
* **MARY Curve Sweep:** Once optimal rates are identified, the script sweeps the external magnetic field from 0 up to a user-defined maximum (e.g., 30 mT). The field grid is deliberately non-uniform (densely sampled at low fields and more sparsely sampled at high fields) to accurately capture rapid yield changes.
* **Crash-Resistance:** Output data streams directly to CSV files row-by-row. If the notebook crashes or is interrupted, rerunning it will automatically load the existing data and skip already computed points.

## Requirements
To run this notebook, you will need a standard Python scientific stack. The dependencies include:
* `pandas`
* `numpy`
* `scipy`
* `matplotlib`

## Usage
1. Open the Jupyter Notebook `MagnetoSimmer.ipynb`.
2. **You only need to edit Cell 2**.
3. Under the `# USER INPUTS` section, define your specific system parameters:
   * `radicalPairName` (used for output file naming).
   * Isotropic electron $g$-values (`g1`, `g2`).
   * Hyperfine couplings for both radicals (entered as spin quantum number and $a_{\text{iso}}$ in MHz).
   * Spin-relaxation rate (`k_relax`).
   * Grid-search and MARY-curve sweep settings (field limits and resolutions).
4. Run all cells from top to bottom.

## Outputs
The notebook automatically saves the following files to the working directory:
* `[radicalPairName]_MFE_Grid.csv`: Raw data from the $k_S$ vs $k_C$ grid search.
* `[radicalPairName]_MFE_Grid.png`: A 2D contour plot visualizing the maximum magnetic field effect across the rate-constant plane.
* `[radicalPairName]_MARY.csv`: Raw data from the magnetic field sweep.
* `[radicalPairName]_MARY.png`: The final plotted MARY curve showing the diagnostic points (0 field, maximum yield, and Earth's field). 

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
