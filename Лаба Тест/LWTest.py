def decay(n0, k, dt, steps):
    values = [n0]
    for _ in range(steps):
        values.append(values[-1] - k * values[-1] * dt)
    return values


print("Моделирование распада")