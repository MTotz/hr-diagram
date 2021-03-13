import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_raw = pd.read_csv('../database/hygdata_v3.csv', usecols=['absmag', 'spect', 'lum', 'ci'])


df_raw = df_raw.sort_values('ci')
print(df_raw.head())

# fig1 = df_raw.plot(kind='scatter', x='ci', y='absmag', s=1)
# plt.gca().invert_yaxis() # invert axis so bottom to top is positive to negative values, since the most negative the absolute magnitude value the brighter the star
# plt.grid()
# plt.title('absolute magnitude vs. color index')
# fig1.set_xlim(-0.5, 2)

fig2 = df_raw.plot(kind='scatter', x='ci', y='lum', s=1, logy=True)
plt.grid()
plt.title('lum vs. color index')
fig2.set_xlim(-0.5, 2)
#fig2.set_ylim(0, 1)



plt.show()