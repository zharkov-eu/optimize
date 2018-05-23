"""
Tesla Supercharger Station example
"""

import itertools
import random

import simpy


RANDOM_SEED = 42
ACCUM_RESERVE = 15                        # Count
ACCUM_REPLACE = 2                         # Accumulator replace time
ACCUM_RECHARGE = 1.4                      # kWh/minute
ACCUM_SIZE = 85                           # Max accumulator capacity
ACCUM_LEVEL = [10, 35]                    # Min/max levels of incoming accumulator capacity
MAX_THROUGHPUT = 10                       # Max simultaneous charging
CAR_INTER = [1, 7]                        # Create a car every [min, max] minute
SIM_TIME = 500                            # Simulation time in minute

def car(name, env, recharger, reserve, counters):
    accum_level = random.randint(*ACCUM_LEVEL)
    if counters["charge_req"] > MAX_THROUGHPUT:
        queued_req = counters["charge_req"] - MAX_THROUGHPUT
    else:
        queued_req = 0
    print('%s arriving at recharge station at %.1f, car in queue = %.1i' % (name, env.now, queued_req))
    with recharger.request() as req:
        start = env.now
        yield req
        kwh_required = ACCUM_SIZE - accum_level

        if (reserve.level > 0):
            yield reserve.get(1)
            yield env.timeout(ACCUM_REPLACE)
        else:
            yield env.timeout(kwh_required / ACCUM_RECHARGE)

        counters["cars_charged_count"] = counters["cars_charged_count"] + 1
        counters["processing_time"] = counters["processing_time"] + (env.now - start)
        counters["charge_req"] = counters["charge_req"] - 1

        print('%s finished recharging in %.1f minutes.' % (name, env.now - start))


def accumulator_recharge_control(env, recharger, reserve, counters):
    while True:
        if reserve.level < ACCUM_RESERVE and counters["charge_req"] < MAX_THROUGHPUT:
            env.process(recharge_accumulator(env, recharger, reserve, counters))

        yield env.timeout(1)  # Check every 1 minute

def accumulator_recharge_control_adaptive(env, recharger, reserve, counters):
    while True:
        if (reserve.level < ACCUM_RESERVE and counters["charge_accum"] < (MAX_THROUGHPUT / 5)):
            env.process(recharge_accumulator(env, recharger, reserve, counters))

        yield env.timeout(1)  # Check every 1 minute

def recharge_accumulator(env, recharger, reserve, counters):
    start = env.now
    accum_level = random.randint(*ACCUM_LEVEL)
    with recharger.request() as req:
        yield req
        counters["charge_req"] = counters["charge_req"] + 1
        counters["charge_accum"] = counters["charge_accum"] + 1
        kwh_required = ACCUM_SIZE - accum_level
        yield env.timeout(kwh_required / ACCUM_RECHARGE)
        yield reserve.put(1)
        counters["charge_req"] = counters["charge_req"] - 1
        counters["charge_accum"] = counters["charge_accum"] - 1
        print('Finished recharging accumulator %.1f minutes, accumulator count = %i' % (env.now - start, reserve.level))

def car_generator(env, recharger, reserve, counters):
    for i in itertools.count():
        yield env.timeout(random.randint(*CAR_INTER))
        counters["charge_req"] = counters["charge_req"] + 1
        counters["cars_count"] = counters["cars_count"] + 1
        env.process(car('Car %d' % i, env, recharger, reserve, counters))

print('Tesla accumulator charger')
random.seed(RANDOM_SEED)

counters = {
    "charge_req": 0,
    "processing_time": 0,
    "charge_accum": 0,
    "cars_charged_count": 0,
    "cars_count": 0
}

env = simpy.Environment()
recharger = simpy.Resource(env, 10)
reserve = simpy.Container(env, ACCUM_RESERVE, init=ACCUM_RESERVE)

env.process(car_generator(env, recharger, reserve, counters))
env.process(accumulator_recharge_control(env, recharger, reserve, counters))
# env.process(accumulator_recharge_control_adaptive(env, recharger, reserve, counters))

env.run(until=SIM_TIME)

print("Cars charged: %i of %i" % (counters["cars_charged_count"], counters["cars_count"]))
print("Average processing time: %.1f" % (counters["processing_time"] / counters["cars_charged_count"]))