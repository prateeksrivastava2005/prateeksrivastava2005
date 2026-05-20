# Parkinson's Disease Detection via Vocal Biomarkers

Developed by **Prateek Srivastava** *(Python, Scikit-learn, Audio Signal Processing)*

## Overview
A non-invasive diagnostic machine learning system trained on acoustic voice parameters to detect early-stage Parkinson's disease.

## Key Features & Methodology
- **Acoustic Feature Extraction**:
  - Fundamental frequency variation (MDVP:Fo, MDVP:Fhi, MDVP:Flo)
  - Jitter measurements (MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP)
  - Shimmer measurements (MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA)
  - 13-band Mel-Frequency Cepstral Coefficients (MFCCs)
  - Harmonics-to-Noise Ratio (NHR, HNR)
- **Model Comparison**:
  - K-Nearest Neighbors (KNN)
  - Random Forest Classifier (Grid-searched trees & max depth)
  - Decision Trees with cost-complexity pruning
- **Optimized Ensemble**:
  - Soft-voting ensemble combining RF, KNN, and Gradient Boosting yielding superior sensitivity and specificity.
