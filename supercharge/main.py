"""
Tesla Supercharger Station example
"""

import itertools
import random

import simpy


RANDOM_SEED = 42
ACCUM_RECHARGE = 1.4                      # kWh/minute
ACCUM_SIZE = 85                           # Max accumulator capacity
ACCUM_LEVEL = [10, 35]                    # Min/max levels of incoming accumulator capacity
MAX_THROUGHPUT = 10                       # Max simultaneous charging
CAR_INTER = [1, 7]                        # Create a car every [min, max] minute
SIM_TIME = 400                            # Simulation time in minute

def car(name, env, recharger, counters):
    accum_level = random.randint(*ACCUM_LEVEL)
    if counters["car_on_charge"] > 10:
        queued_cars = counters["car_on_charge"] - 10
    else:
        queued_cars = 0
    print('%s arriving at recharge station at %.1f, car in queue = %.1i' % (name, env.now, queued_cars))
    with recharger.request() as req:
        start = env.now
        yield req
        kwh_required = ACCUM_SIZE - accum_level

        yield env.timeout(kwh_required / ACCUM_RECHARGE)
        counters["car_on_charge"] = counters["car_on_charge"] - 1

        print('%s finished recharging in %.1f minutes.' % (name, env.now - start))


def car_generator(env, recharger, counters):
    for i in itertools.count():
        yield env.timeout(random.randint(*CAR_INTER))
        counters["car_on_charge"] = counters["car_on_charge"] + 1
        env.process(car('Car %d' % i, env, recharger, counters))


print('Tesla accumulator charger')
random.seed(RANDOM_SEED)

counters = {
    "car_on_charge": 0
}

env = simpy.Environment()
recharger = simpy.Resource(env, 10)

env.process(car_generator(env, recharger, counters))

env.run(until=SIM_TIME)