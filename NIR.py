from datetime import datetime, timedelta

records = [
    {"начало": "10:10:2026 00:25", "конец": "10:10:2026 02:18", "спутник": "SAT-03", "качество": 82},
    {"начало": "10:10:2026 01:10", "конец": "10:10:2026 04:42", "спутник": "SAT-17", "качество": 96},
    {"начало": "10:10:2026 02:35", "конец": "10:10:2026 05:05", "спутник": "SAT-06", "качество": 67},
    {"начало": "10:10:2026 04:50", "конец": "10:10:2026 07:36", "спутник": "SAT-25", "качество": 91},
    {"начало": "10:10:2026 07:20", "конец": "10:10:2026 10:11", "спутник": "SAT-28", "качество": 88},
    {"начало": "10:10:2026 08:40", "конец": "10:10:2026 12:25", "спутник": "SAT-11", "качество": 59},
    {"начало": "10:10:2026 09:55", "конец": "10:10:2026 13:17", "спутник": "SAT-19", "качество": 100},
    {"начало": "10:10:2026 11:30", "конец": "10:10:2026 14:09", "спутник": "SAT-04", "качество": 76},
    {"начало": "10:10:2026 12:50", "конец": "10:10:2026 16:44", "спутник": "SAT-26", "качество": 93},
    {"начало": "10:10:2026 14:35", "конец": "10:10:2026 17:20", "спутник": "SAT-08", "качество": 65},
    {"начало": "10:10:2026 17:05", "конец": "10:10:2026 20:38", "спутник": "SAT-13", "качество": 71},
    {"начало": "10:10:2026 18:25", "конец": "10:10:2026 21:06", "спутник": "SAT-30", "качество": 98},
    {"начало": "10:10:2026 20:15", "конец": "10:10:2026 23:50", "спутник": "SAT-05", "качество": 84},
    {"начало": "11:10:2026 00:20", "конец": "11:10:2026 03:47", "спутник": "SAT-22", "качество": 90},
    {"начало": "11:10:2026 01:40", "конец": "11:10:2026 04:16", "спутник": "SAT-14", "качество": 63},
    {"начало": "11:10:2026 03:05", "конец": "11:10:2026 06:55", "спутник": "SAT-27", "качество": 95},
    {"начало": "11:10:2026 04:30", "конец": "11:10:2026 07:14", "спутник": "SAT-09", "качество": 78},
    {"начало": "11:10:2026 06:10", "конец": "11:10:2026 09:52", "спутник": "SAT-16", "качество": 86},
    {"начало": "11:10:2026 09:45", "конец": "11:10:2026 13:30", "спутник": "SAT-24", "качество": 97},
    {"начало": "11:10:2026 12:15", "конец": "11:10:2026 15:06", "спутник": "SAT-07", "качество": 56},
    {"начало": "11:10:2026 15:20", "конец": "11:10:2026 19:05", "спутник": "SAT-18", "качество": 92},
    {"начало": "11:10:2026 19:30", "конец": "11:10:2026 23:15", "спутник": "SAT-12", "качество": 80},
]

def set_indexes(daily_records): # Присвоение индексов записям в списке и подсписках
    index = 1

    for records in daily_records.values():
        for i, record in enumerate(records):
            records[i] = {"index": index, **record}
            index += 1

    return daily_records

def find_duration(record): # Поиск продолжительности в минутах
    duration = ( datetime.strptime(record["конец"], "%d:%m:%Y %H:%M") - datetime.strptime(record["начало"], "%d:%m:%Y %H:%M") ).total_seconds() / 60
    return duration

def validate_records(records):
    """Проверка корректности исходных данных."""
    pass

def split_records_by_date(records): # разделение одного списка на несколько по дням (позволяеть сильно оптимизировать поиск лучшей комбинации)
    fmt = "%d:%m:%Y %H:%M"
    daily_records = {}

    for record in records:
        start = datetime.strptime(record["начало"], fmt)
        end = datetime.strptime(record["конец"], fmt)

        current_start = start

        while current_start.date() < end.date():
            # Полночь, когда заканчивается текущий день
            midnight = datetime.combine(
                current_start.date() + timedelta(days=1),
                datetime.min.time()
            )

            # Копируем исходную запись для текущего дня
            part = record.copy()
            part["начало"] = current_start.strftime(fmt)
            part["конец"] = midnight.strftime(fmt)

            date_key = current_start.strftime("%d:%m:%Y")
            daily_records.setdefault(date_key, []).append(part)

            current_start = midnight

        # Добавляем оставшуюся часть записи
        if current_start < end:
            part = record.copy()
            part["начало"] = current_start.strftime(fmt)
            part["конец"] = end.strftime(fmt)

            date_key = current_start.strftime("%d:%m:%Y")
            daily_records.setdefault(date_key, []).append(part)

    return daily_records

def find_combinations(records): # Поиск возможных комбинаций
    variants = []

    def overlaps(a, b):
        return a["начало"] < b["конец"] and b["начало"] < a["конец"]

    def backtrack(index, selected):
        # Рассмотрели все записи — сохраняем полученный набор
        if index == len(records):
            variants.append([record["index"] for record in selected])
            return

        # Вариант 1: пропускаем текущую запись
        backtrack(index + 1, selected)

        # Вариант 2: пытаемся добавить текущую запись
        current = records[index]

        # Проверяем, нет ли пересечений с уже выбранными
        can_add = True

        for record in selected:
            if overlaps(current, record):
                can_add = False
                break

        if can_add:
            selected.append(current)
            backtrack(index + 1, selected)

            # Возвращаем список в прежнее состояние
            selected.pop()

    backtrack(0, [])
    return variants


def select_best_combination(   # Поиск лучшей комбинации
    variants,
    records,
    alpha=0.5,  # Коэффициент альфа, влияет на вес длительности комбинации при оценке
    beta=0.5    # Коэффициент бета, влияет на вес среднего качества комбинации при оценке
):

    records_by_index = {
        record["index"]: record
        for record in records
    }

    # Суммарная продолжительность каждой комбинации
    total_times = [
        sum(find_duration(records_by_index[i]) for i in variant)
        for variant in variants
    ]

    t_max = max(total_times, default=0)

    if t_max == 0:
        return []

    # Максимальное среднее качество среди комбинаций
    average_qualities = [
        sum(records_by_index[i]["качество"] for i in variant)
        / len(variant)
        for variant in variants
        if variant
    ]

    q_avg = sum(record["качество"] for record in records) / len(records) # Среднее качество записи в records

    best_variant = []
    best_score = float("-inf")

    for variant in variants:
        if not variant:
            continue

        selected_records = [
            records_by_index[i] for i in variant
        ]

        # Суммарное время наблюдения
        total_time = sum(
            find_duration(record) for record in selected_records
        )

        # Среднее качество
        average_quality_day = sum(
            record["качество"] for record in selected_records
        ) / len(selected_records)

        # Нормирование на среднее значение качества
        t_norm = total_time / t_max
        q_norm = average_quality_day / q_avg if q_avg > 0 else 0

        # Итоговая оценка
        score = alpha * t_norm + beta * q_norm

        if score > best_score:
            best_score = score
            best_variant = variant

    return best_variant

def merge_lists(daily_records):  # Объединяет несколько подсписков в один список
    merged_records = []

    for records in daily_records.values():
        merged_records.extend(records)

    return merged_records

def stats(best_variant, records):  # выводит данные комбинации

    records_by_index = {
        record["index"]: record
        for record in records
    }

    selected_records = [
        records_by_index[i]
        for i in best_variant
    ]

    if not selected_records:
        print("Лучшая комбинация пуста.")
        return

    # Количество записей
    length = len(selected_records)

    # Среднее качество
    average_quality = sum(
        record["качество"]
        for record in selected_records
    ) / length

    # Общая продолжительность в минутах
    total_minutes = 0

    for record in selected_records:
        start = datetime.strptime(record["начало"], "%d:%m:%Y %H:%M")
        end = datetime.strptime(record["конец"], "%d:%m:%Y %H:%M")

        duration = (end - start).total_seconds() / 60
        total_minutes += duration

    # Переводим в часы и минуты
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    print(f"Количество записей: {length}")
    print(f"Среднее качество: {average_quality:.2f}")
    print(f"Общая продолжительность: {hours} ч {minutes} мин")

def main():

    daily_records = set_indexes(split_records_by_date(records)) # Разделяем записи на несколько подсписков по дням, расставляем индексы

    best_daily_records = {}

    for date, sublist in daily_records.items(): # Поиск лучших комбинаций для каждого подсписка  
        variants = find_combinations(sublist)

        best_combination = select_best_combination(     # В теле функции select_best_combination можно изменить коэффициенты альфа и бета, влияющие на критерии оценки комбинации
            variants,
            sublist,
        )

        best_daily_records[date] = best_combination

    print("Лучшая комбинация: ", best_daily_records) # Лучшая комбинация

    stats( merge_lists(best_daily_records), merge_lists(daily_records) ) # Вывод данных лучшей комбинации         merge_lists объеденяет список с несколькими пожсписками в один
    pass


main()
