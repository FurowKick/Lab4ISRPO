def decay(n0, k, dt, steps):
    values = [n0]
    for _ in range(steps):
        values.append(values[-1] - k * values[-1] * dt)
    return values

if __name__ == "__main__":
    result = decay(100.0, 0.3, 0.1, 10)
    print(f"Итоговое значение: {result[-1]:.2f}")

print(f"Шагов: {len(result) - 1}")

print("Моделирование распада")