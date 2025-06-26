import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Inout data for the exercise
your_data = [
    2.68, 3.73, 3.62, 3.43, 3.24, 3.34, 3.21, 3.15, 3.04, 2.98,
    3.16, 3.18, 3.21, 3.15, 3.15, 3.08, 3.08, 3.02, 3.02, 3.02,
    3.03, 3.07, 3.03, 3.02, 3.04, 3.04, 3.04, 3.04, 3.08, 3.08,
    3.18, 3.00, 3.01, 3.04, 3.04, 3.09, 3.09, 3.11, 3.11, 3.11,
    3.32, 2.69, 2.80, 3.05, 3.17, 3.17, 3.03, 3.08, 3.03, 3.05,
    3.00, 3.10, 3.13, 3.08, 3.08, 3.54, 3.54, 3.21, 3.21, 3.05,
    3.05, 2.89, 2.89, 2.86, 2.86, 3.01, 3.01, 3.01, 3.01, 3.01,
    3.01, 3.01, 3.01, 3.01, 3.04, 3.04, 3.10, 3.10, 3.10, 3.07,
    3.13, 3.17, 3.17, 3.17, 3.17, 3.12, 3.12, 3.04, 3.04, 3.04,
    3.04, 3.17, 3.17, 3.17, 3.17, 3.14, 3.14, 3.13, 3.13, 3.23,
    3.20, 3.20, 3.21, 3.21, 3.21, 3.21, 3.16, 3.16, 3.10, 3.08,
    3.08, 3.04, 3.04, 3.03, 2.97, 3.10, 3.14, 3.14, 3.16, 3.16,
    3.16, 3.02, 3.02, 3.03, 3.03, 3.05, 3.05, 3.17, 3.17, 2.98, 2.98
]

def analyze_series(series, max_lag=60): #where I defined the maximum lag
    series = pd.Series(series).dropna()
    n = len(series)
    mean = series.mean()
    variance = series.var(ddof=1)

    print(f"Mean: {mean:.4f}")
    print(f"Variance: {variance:.4f}")

    covariances = []
    autocorrelations = []
    correlation_times = []

    threshold = np.exp(-1)  # ≈0.3679 - In Order to change the target e, changes this value here
    tau_drop_lag = None

    # compute covariances, autocorrelations, and τ_k
    for k in range(max_lag + 1):
        if k == 0:
            cov = variance
            autocorr = 1.0
        else:
            x1 = series[:-k]
            x2 = series[k:]
            cov = np.sum((x1 - mean) * (x2 - mean)) / (n - k)
            autocorr = cov / variance #calculation of aut

        covariances.append(cov)
        autocorrelations.append(autocorr)

        if k > 0 and autocorr > 0:
            tau_k = -k / np.log(autocorr)
            correlation_times.append((k, tau_k))

        if tau_drop_lag is None and autocorr <= threshold:
            tau_drop_lag = k

    # print results
    print("\nAutocorrelation values:")
    for k, a in enumerate(autocorrelations):
        print(f"  Lag {k}: a(k) = {a:.4f}")

    print("\nEstimated correlation time τ for selected lags:")
    for k, tau_k in correlation_times:
        print(f"  Lag {k}: τ ≈ {tau_k:.2f} hours")

    if tau_drop_lag is not None:
        print(f"\n▶ Correlation drops below e⁻¹ ≈ 0.37 at lag {tau_drop_lag} h")
    else:
        print(f"\n⚠ Autocorr never drops below e⁻¹ within {max_lag} lags.")

    # --- Plot: Full Autocorrelation vs Lag ---
    plt.figure(figsize=(10, 5))
    lags = list(range(max_lag + 1))
    plt.stem(lags, autocorrelations,
             basefmt=" ", linefmt='orange', markerfmt='o')
    plt.title("Autocorrelation vs. Lag")
    plt.xlabel("Lag (hours)")
    plt.ylabel("Autocorrelation")
    plt.axhline(y=threshold,
                color='red', linestyle='--',
                label='a(k) = e⁻¹ ≈ 0.37')
    if tau_drop_lag is not None:
        plt.axvline(x=tau_drop_lag,
                    color='blue', linestyle='--',
                    label=f'Corr time ≈ {tau_drop_lag} h')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return {
        "mean": mean,
        "variance": variance,
        "covariances": covariances,
        "autocorrelations": autocorrelations,
        "correlation_times": correlation_times,
        "tau_drop_lag": tau_drop_lag
    }

# Run the analysis
results = analyze_series(your_data, max_lag=60) #Inputs are the size of the lag and avai
