"""
Tesla Supercharger Station example
"""

import itertools
import random

import simpy


RANDOM_SEED = 42
ACCUM_RESERVE = 30                        # Count
ACCUM_REPLACE = 2                         # Accumulator replace time
ACCUM_RECHARGE = 1.4                      # kWh/minute
ACCUM_SIZE = 85                           # Max accumulator capacity
ACCUM_LEVEL = [10, 35]                    # Min/max levels of incoming accumulator capacity
MAX_THROUGHPUT = 10                       # Max simultaneous charging
CAR_INTER = [1, 7]                        # Create a car every [min, max] minute
SIM_TIME = 400                            # Simulation time in minute

def car(name, env, recharger, reserve, counters):
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

        try:
            yield reserve.get(1)
            yield env.timeout(ACCUM_REPLACE)
        except:
            yield env.timeout(kwh_required / ACCUM_RECHARGE)
        counters["car_on_charge"] = counters["car_on_charge"] - 1

        print('%s finished recharging in %.1f minutes.' % (name, env.now - start))


def accumulator_recharge_control(env, recharger, reserve, counters):
    while True:
        if reserve.level < ACCUM_RESERVE and counters["car_on_charge"] < 10:
            start = env.now
            accum_level = random.randint(*ACCUM_LEVEL)
            with recharger.request() as req:
                yield req
                kwh_required = ACCUM_SIZE - accum_level
                yield env.timeout(kwh_required / ACCUM_RECHARGE)
                yield reserve.put(1)
                print('Finished recharging accumulator %.1f minutes, accumulator count = %i' % (env.now - start, reserve.level + 1))

        yield env.timeout(1)  # Check every 1 minute


def car_generator(env, recharger, reserve, counters):
    for i in itertools.count():
        yield env.timeout(random.randint(*CAR_INTER))
        counters["car_on_charge"] = counters["car_on_charge"] + 1
        env.process(car('Car %d' % i, env, recharger, reserve, counters))

print('Tesla accumulator charger')
random.seed(RANDOM_SEED)

counters = {
    "car_on_charge": 0
}

env = simpy.Environment()
recharger = simpy.Resource(env, 10)
reserve = simpy.Container(env, ACCUM_RESERVE, init=ACCUM_RESERVE)

env.process(car_generator(env, recharger, reserve, counters))
env.process(accumulator_recharge_control(env, recharger, reserve, counters))

env.run(until=SIM_TIME)