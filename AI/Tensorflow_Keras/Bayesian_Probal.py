import random


def give_P():
    P = {}

    P["D|N,W"] = 0.50
    P["~D|N,W"] = 0.50
    P["D|~N,W"] = 0.30
    P["D|N,~W"] = 0.10
    P["~D|N,~W"] = 0.90
    P["D|~N,~W"] = 0.05

    P["B|W"] = 0.50
    P["~B|W"] = 0.50
    P["B|~W"] = 0
    P["~B|~W"] = 1 - P["B|~W"]

    P["Z|D,B"] = 0.90
    P["Z|D,~B"] = 0.10
    P["Z|~D,B"] = 0.80
    P["Z|~D,~B"] = 0.02

    P["N"] = 0.3
    P["~N"] = 0.7
    P["W"] = 0.5
    P["~W"] = 0.5

    return P


def analytically():
    P = give_P()
    P["D"] = P["D|N,W"] * P["N"] * P["W"] + P["D|~N,W"] * P["~N"] * P["W"] + \
        P["D|N,~W"] * P["N"] * P["~W"] + P["D|~N,~W"] * P["~N"] * P["~W"]

    P["B"] = P["B|W"] * P["W"]
    P["~B"] = 1 - P["B"]

    P["B,D"] = P["B|W"] * P["D|N,W"] * P["N"] * P["W"] + P["B|~W"] * P["D|N,~W"] * P["N"] * P["~W"] + \
        P["B|W"] * P["D|~N,W"] * P["~N"] * P["W"] + \
        P["B|~W"] * P["D|~N,~W"] * P["~N"] * P["~W"]
    P["~B,D"] = P["~B|W"] * P["D|N,W"] * P["N"] * P["W"] + P["~B|~W"] * P["D|N,~W"] * P["N"] * \
        P["~W"] + P["~B|W"] * P["D|~N,W"] * P["~N"] * P["W"] + \
        P["~B|~W"] * P["D|~N,~W"] * P["~N"] * P["~W"]

    P["Z|D"] = (P["B,D"] * P["Z|D,B"] + P["~B,D"] * P["Z|D,~B"]) / P["D"]

    P["D,B|N"] = P["D|N,W"] * P["B|W"] * \
        P["W"] + P["D|N,~W"] * P["B|~W"] * P["~W"]
    P["D,~B|N"] = P["D|N,W"] * P["~B|W"] * \
        P["W"] + P["D|N,~W"] * P["~B|~W"] * P["~W"]
    P["~D,B|N"] = P["~D|N,W"] * P["B|W"] * \
        P["W"] + P["~D|N,~W"] * P["B|~W"] * P["~W"]
    P["~D,~B|N"] = P["~D|N,W"] * P["~B|W"] * \
        P["W"] + P["~D|N,~W"] * P["~B|~W"] * P["~W"]

    P["Z|N"] = P["Z|D,B"] * P["D,B|N"] + P["Z|D,~B"] * P["D,~B|N"] + \
        P["Z|~D,B"] * P["~D,B|N"] + P["Z|~D,~B"] * P["~D,~B|N"]

    return P["Z|D"], P["B,D"], P["Z|N"]


def monte_carlo():
    P = give_P()

    EventsZ_D = 0
    EventsB_D = 0
    EventsZ_N = 0
    d = 0
    n = 0

    for i in range(0, 1000000):
        eventW = random.random() < P["W"]
        if eventW:
            eventB = random.random() < P["B|W"]
        elif not eventW:
            eventB = random.random() < P["B|~W"]

        eventN = random.random() < P["N"]
        if eventN and eventW:
            eventD = random.random() < P["D|N,W"]
        elif eventN and not eventW:
            eventD = random.random() < P["D|N,~W"]
        elif not eventN and eventW:
            eventD = random.random() < P["D|~N,W"]
        elif not eventN and not eventW:
            eventD = random.random() < P["D|~N,~W"]

        if eventD and eventB:
            eventZ = random.random() < P["Z|D,B"]
        elif eventD and not eventB:
            eventZ = random.random() < P["Z|D,~B"]
        elif not eventD and eventB:
            eventZ = random.random() < P["Z|~D,B"]
        else:
            eventZ = random.random() < P["Z|~D,~B"]

        if eventD:
            d += 1
            if eventZ:
                EventsZ_D += 1

        if eventN:
            n += 1
            if eventZ:
                EventsZ_N += 1

        if eventB and eventD:
            EventsB_D += 1

    P["Z|D"] = EventsZ_D / d
    P["B,D"] = EventsB_D / i
    P["Z|N"] = EventsZ_N / n

    return P["Z|D"], P["B,D"], P["Z|N"]


print("Analytically: P(Z|D) = {}, P(B,D) = {}, P(Z|N) = {}".format(*analytically()))
print("Monte Carlo: P(Z|D) = {}, P(B,D) = {}, P(Z|N) = {}".format(*monte_carlo()))
