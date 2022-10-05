def gjennomsnitt(ant, tot):
    return(float(tot/ant))
måling_fil = open("Uke_5/max_vind_sola_enkelttall.txt", "r")
total_temp = float(0)
målinger = int(0)
max_temp = float(0)
for m in måling_fil:
    total_temp += float(m)
    målinger += 1
    if float(m) > max_temp:
        max_temp = float(m)

print(f"Gjennomsnittet er: {gjennomsnitt(målinger, total_temp):.1f}")
print(f"Makstemp er: {max_temp}")