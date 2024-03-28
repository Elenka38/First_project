import random

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]

generated_prophecies = []
i = 0
while i < 5:
    j = 0
    forescast = []
    while j < 3:
        ti = random.randrange(0, len(times))
        ai = random.randrange(0, len(advices))
        pi = random.randrange(0, len(promises))

        t = times[ti]
        a = advices[ai]
        p = promises[pi]
        full_sentens = t.title() + " " + a + " " + p + "."

    forescast.append(full_sentens)

    j = j + 1
generated_prophecies.append(forescast[0] + " " + forescast[1] + " " + forecast[2]) 
i = i + 1   


