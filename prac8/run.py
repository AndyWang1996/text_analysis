import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

axe = plt.subplot(1, 1, 1, facecolor='white')
x = [0.2, 0.5, 0.6, 0.8, 0.88, 0.9, 0.95, 0.96, 0.97, 0.98]
y = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
x = [1-a for a in x]
# y = [np.log10(a) for a in y]
axe.set_xscale('log')
axe.set_yscale('log')
axe.set_xticks([0.01, 0.02, 0.04, 0.1, 0.2, 0.5, 0.8, 1])
axe.set_yticks([0.01, 0.02, 0.04, 0.1, 0.2, 0.5, 0.8, 1])
axe.get_xaxis().set_major_formatter(ticker.ScalarFormatter())
axe.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
axe.plot(y, x)
# plt.semilogy(axe)
# plt.semilogx(axe)

plt.show()
