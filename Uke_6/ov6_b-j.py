from cmath import sqrt
import matplotlib.pyplot as plt
import sys
import csv
import numpy as np

sys.path.append('../../')
sys.path.insert(0, '/home/alkas/syncthing/documents/Skule/DAT120/Øvinger/')
from Uke_6.ov6_a import euk_disk
from Uke_4.ov4_f_g import turbin_effekt, circ_area

tidspunkt = []
retning1 = []
retning2 = []
effect = []

# Read CSV data into lists
with open("Uke_6/tidevannsdata_csv.txt", 'r') as csv_file:
    reader = csv.reader(csv_file, dialect=csv.excel, delimiter = ';')
    next(csv_file)

    for row in reader:
        i = reader.line_num - 1
        tidspunkt.append(float(row[0]))
        retning1.append(float(row[1]))
        retning2.append(float(row[2]))

# Copy lists into np arrays to do quick math on
np_ret1 = np.array(retning1)
np_ret2 = np.array(retning2)
# Oppg: d
tot_strom = np.array(euk_disk(np_ret1,np_ret2)) # NOT WORKING???

# Oppg: e
plt.subplot(2,1,1)
plot_name = "Vannstrøm"
plt.plot(tidspunkt, tot_strom, label=plot_name)
plt.title(plot_name)
plt.legend()

# Oppg: f
for s in tot_strom:
    effect.append(turbin_effekt(s))

# Oppg: g
plt.subplot(2,1,2)
plot_name = "Effekt"
plt.plot(tidspunkt, effect, label=plot_name)
plt.title(plot_name)
plt.legend()
plt.show()

# Oppg: h
gj_strom = np.sum(tot_strom)/len(tidspunkt)
print(f"Gjennomsnittlig vannstrøm: {gj_strom:.4}")
# Oppg: i
print(f"Total energi: {round(gj_strom * (24*60*60), 2)}")
# Oppg: j
# Hvorfor bruke listen fra f når vi allerede har gjennomsnittet???
print(f"Gjennomsnittlig effekt: {turbin_effekt(gj_strom):.4}")
