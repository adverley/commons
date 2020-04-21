import numpy as np
import matplotlib.pyplot as plt

n_random_samples_to_draw = 10000

min_sample = 0.00001
max_sample = 1
bins = [0.0001, 0.001, 0.01, 0.1, 1]
bins = np.logspace(np.log10(min_sample), np.log10(max_sample), 10)

a = np.log10(min_sample)
b = np.log10(max_sample)

log_r = np.random.random(size=n_random_samples_to_draw)  # between [0, 1)
log_r = (b - a) * log_r + a

print(f'min sampled logr = {min(log_r)} compared to min allowed: {a}')
print(f'max sampled logr = {max(log_r)} compared to max allowed: {b}')

r = np.power(10, log_r)

print(f'min sampled r = {min(r)} compared to min allowed: {min_sample}')
print(f'max sampled r = {max(r)} compared to max allowed: {max_sample}')

plt.hist(r, bins=bins)
plt.xscale('log')
plt.show()

# COMPARE TO LINEAR SAMPLINN

plt.hist((max_sample - min_sample) * np.random.random(size=n_random_samples_to_draw) + min_sample, bins=bins)
plt.xscale('log')
plt.show()
