from __future__ import annotations


def _read_positive_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Ошибка: введите число (например: 70 или 70.5).")
            continue

        if value <= 0:
            print("Ошибка: значение должно быть больше 0.")
            continue

        return value


def _bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "недовес"
    if bmi < 25:
        return "нормальный"
    if bmi < 30:
        return "избыточный"
    return "ожирение"


def main() -> None:
    weight_kg = _read_positive_float("Введите вес (кг): ")
    height_m = _read_positive_float("Введите рост (м): ")

    bmi = weight_kg / (height_m**2)
    category = _bmi_category(bmi)

    print(f"BMI: {bmi:.2f}")
    print(f"Категория: {category}")


if __name__ == "__main__":
    main()

