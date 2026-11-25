import math

def analytic(n0, k, t):
    return n0 * math.exp(-k * t)

def compare(n0, k, dt, steps):
    euler = decay(n0, k, dt, steps)
    for i, value in enumerate(euler):
        exact = analytic(n0, k, i * dt)
        print(f"t={i * dt:.1f}  Эйлер={value:.2f}  точно={exact:.2f}")

def decay(n0, k, dt, steps):
    values = [n0]
    for _ in range(steps):
        values.append(values[-1] - k * values[-1] * dt)
    return values

if __name__ == "__main__":
    result = decay(100.0, 0.3, 0.1, 10)
    print(f"Итоговое значение: {result[-1]:.2f}")
    compare(100.0, 0.3, 0.1, 5)

print(f"Шагов: {len(result) - 1}")

print("Моделирование распада")