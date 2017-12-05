# Napisz swoją wersję printa o nazwie mojprint, która oprócz zwykłych argumentów
# pobierze jeszcze obowiązkowo ile razy dana rzecz ma być wyprintowana
# oraz opcjonalnie czy ma być jakiś sufix przed daną wartością.

def mojprint(ile=1, *args, prefix):
    for i in range(0, ile):
        for j in range(0, len(args)):
            print(prefix + ": " + args[j])


mojprint(2, "patelnia", prefix="prefix")