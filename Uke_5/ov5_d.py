def gjennomsnitt(ant, tot):
    return(float(tot/ant))
with open("Uke_5/max_vind_sola_enkelttall_med_feil.txt", "r") as måling_fil:
    total_temp = float(0)
    målinger = int(0)
    max_temp = float(0)
    ugyl_målinger = int(0)
    for m in måling_fil:
        try:
            float(m)
            total_temp += float(m)
            målinger += 1
            if float(m) > max_temp:
                max_temp = float(m)
        except ValueError:
            ugyl_målinger += 1

    print(f"Gjennomsnittet er: {gjennomsnitt(målinger, total_temp):.1f}")
    print(f"Makstemp er: {max_temp}")
    print(f"Antall gyldige målinger: {målinger}")