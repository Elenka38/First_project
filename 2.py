import random
times = ["Утром", "Днём", "Вечером", "Ночью"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей", "встреч", "неожиданного праздника"]
i = 0
while i < 3:
        index_t = random.randrange(0, len(times))
        index_a = random.randrange(0, len(advices))
        index_p = random.randrange(0, len(promises))
        print(times[index_t] + " " + advices[index_a] + " " +
promises[index_p])
        i = i + 1