import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# import data
X = np.loadtxt('data_nAtoms.txt')
n = X[:,0]
t = X[:,1]

nAtoms = n * n * n * 4.0

# fit data
m, b = np.polyfit(np.log10(nAtoms),np.log10(t),1)
x = 10**np.arange(15)

# Plots
fig = plt.figure(figsize=(8.0, 4.25))
fig.suptitle("Computation of Lenard-Jones Force", fontsize=14)
gs = gridspec.GridSpec(1, 2)
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])

ax1.loglog(nAtoms, t, 'ko')
ax1.loglog(x, (10**b)*(x**m), 'r-', label="")
#ax1.set_xlim(1e3, 1e7)
ax1.set_xlabel("# of atoms")
ax1.set_ylabel("time (s)")

# ax2 is for changing "lattice length"

gs.tight_layout(fig, rect=[0, 0, 1, 0.95])
fig.savefig('plot_forceLJ.pdf', dpi=200)
