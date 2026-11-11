from datetime import datetime, timedelta

records = [
    {"начало": "10:10:2026 00:15", "конец": "10:10:2026 02:40", "спутник": "SAT-01", "качество": 87},  # 1
    {"начало": "10:10:2026 01:10", "конец": "10:10:2026 04:25", "спутник": "SAT-02", "качество": 76},  # 2
    {"начало": "10:10:2026 03:05", "конец": "10:10:2026 05:50", "спутник": "SAT-03", "качество": 94},  # 3
    {"начало": "10:10:2026 05:20", "конец": "10:10:2026 08:10", "спутник": "SAT-04", "качество": 68},  # 4
    {"начало": "10:10:2026 07:45", "конец": "10:10:2026 10:30", "спутник": "SAT-05", "качество": 91},  # 5
    {"начало": "10:10:2026 09:15", "конец": "10:10:2026 12:05", "спутник": "SAT-01", "качество": 83},  # 6
    {"начало": "10:10:2026 11:40", "конец": "10:10:2026 14:20", "спутник": "SAT-02", "качество": 72},  # 7
    {"начало": "10:10:2026 13:10", "конец": "10:10:2026 16:45", "спутник": "SAT-03", "качество": 98},  # 8
    {"начало": "10:10:2026 15:30", "конец": "10:10:2026 18:15", "спутник": "SAT-04", "качество": 64},  # 9
    {"начало": "10:10:2026 17:05", "конец": "10:10:2026 20:40", "спутник": "SAT-05", "качество": 89},  # 10
    {"начало": "10:10:2026 19:20", "конец": "10:10:2026 22:10", "спутник": "SAT-01", "качество": 79},  # 11
    {"начало": "10:10:2026 21:15", "конец": "11:10:2026 00:35", "спутник": "SAT-02", "качество": 96},  # 12
    {"начало": "10:10:2026 22:05", "конец": "11:10:2026 01:20", "спутник": "SAT-03", "качество": 85},  # 13
    {"начало": "10:10:2026 23:10", "конец": "11:10:2026 02:15", "спутник": "SAT-04", "качество": 73},  # 14
    {"начало": "10:10:2026 23:35", "конец": "11:10:2026 03:05", "спутник": "SAT-05", "качество": 92},  # 15

    {"начало": "11:10:2026 00:20", "конец": "11:10:2026 03:10", "спутник": "SAT-01", "качество": 81},  # 16
    {"начало": "11:10:2026 01:05", "конец": "11:10:2026 04:40", "спутник": "SAT-02", "качество": 95},  # 17
    {"начало": "11:10:2026 03:30", "конец": "11:10:2026 06:15", "спутник": "SAT-03", "качество": 69},  # 18
    {"начало": "11:10:2026 05:10", "конец": "11:10:2026 08:45", "спутник": "SAT-04", "качество": 88},  # 19
    {"начало": "11:10:2026 07:25", "конец": "11:10:2026 10:05", "спутник": "SAT-05", "качество": 74},  # 20
    {"начало": "11:10:2026 09:40", "конец": "11:10:2026 12:30", "спутник": "SAT-01", "качество": 99},  # 21
    {"начало": "11:10:2026 11:15", "конец": "11:10:2026 14:50", "спутник": "SAT-02", "качество": 67},  # 22
    {"начало": "11:10:2026 13:45", "конец": "11:10:2026 16:20", "спутник": "SAT-03", "качество": 90},  # 23
    {"начало": "11:10:2026 15:05", "конец": "11:10:2026 18:35", "спутник": "SAT-04", "качество": 78},  # 24
    {"начало": "11:10:2026 17:30", "конец": "11:10:2026 20:15", "спутник": "SAT-05", "качество": 93},  # 25
    {"начало": "11:10:2026 19:10", "конец": "11:10:2026 22:45", "спутник": "SAT-01", "качество": 71},  # 26
    {"начало": "11:10:2026 20:50", "конец": "11:10:2026 23:40", "спутник": "SAT-02", "качество": 86},  # 27
    {"начало": "11:10:2026 21:20", "конец": "12:10:2026 00:30", "спутник": "SAT-03", "качество": 97},  # 28
    {"начало": "11:10:2026 22:10", "конец": "12:10:2026 01:45", "спутник": "SAT-04", "качество": 82},  # 29
    {"начало": "11:10:2026 23:15", "конец": "12:10:2026 02:50", "спутник": "SAT-05", "качество": 75},  # 30

    {"начало": "12:10:2026 00:10", "конец": "12:10:2026 02:55", "спутник": "SAT-01", "качество": 92},  # 31
    {"начало": "12:10:2026 01:25", "конец": "12:10:2026 04:10", "спутник": "SAT-02", "качество": 77},  # 32
    {"начало": "12:10:2026 03:15", "конец": "12:10:2026 06:35", "спутник": "SAT-03", "качество": 89},  # 33
    {"начало": "12:10:2026 05:40", "конец": "12:10:2026 08:20", "спутник": "SAT-04", "качество": 65},  # 34
    {"начало": "12:10:2026 07:10", "конец": "12:10:2026 10:45", "спутник": "SAT-05", "качество": 96},  # 35
    {"начало": "12:10:2026 09:30", "конец": "12:10:2026 12:15", "спутник": "SAT-01", "качество": 84},  # 36
    {"начало": "12:10:2026 11:50", "конец": "12:10:2026 14:35", "спутник": "SAT-02", "качество": 73},  # 37
    {"начало": "12:10:2026 13:20", "конец": "12:10:2026 16:55", "спутник": "SAT-03", "качество": 100}, # 38
    {"начало": "12:10:2026 15:45", "конец": "12:10:2026 18:30", "спутник": "SAT-04", "качество": 80},  # 39
    {"начало": "12:10:2026 17:15", "конец": "12:10:2026 20:50", "спутник": "SAT-05", "качество": 87},  # 40
    {"начало": "12:10:2026 19:05", "конец": "12:10:2026 22:25", "спутник": "SAT-01", "качество": 70},  # 41
    {"начало": "12:10:2026 20:30", "конец": "12:10:2026 23:15", "спутник": "SAT-02", "качество": 94},  # 42
    {"начало": "12:10:2026 21:10", "конец": "13:10:2026 00:20", "спутник": "SAT-03", "качество": 83},  # 43
    {"начало": "12:10:2026 21:45", "конец": "13:10:2026 01:10", "спутник": "SAT-04", "качество": 98},  # 44
    {"начало": "12:10:2026 22:30", "конец": "13:10:2026 02:05", "спутник": "SAT-05", "качество": 76},  # 45
    {"начало": "12:10:2026 23:05", "конец": "13:10:2026 03:25", "спутник": "SAT-01", "качество": 91},  # 46
    {"начало": "12:10:2026 23:40", "конец": "13:10:2026 02:30", "спутник": "SAT-02", "качество": 68},  # 47
    {"начало": "12:10:2026 22:55", "конец": "13:10:2026 01:35", "спутник": "SAT-03", "качество": 85},  # 48
    {"начало": "12:10:2026 18:50", "конец": "12:10:2026 21:35", "спутник": "SAT-04", "качество": 79},  # 49
    {"начало": "12:10:2026 16:20", "конец": "12:10:2026 19:05", "спутник": "SAT-05", "качество": 88},  # 50
]


def set_indexes(records):  # Присвоение индексов записям в списке
    for i, record in enumerate(records, start=1):
        record["index"] = i

    return records

def find_duration(record): # Поиск продолжительности в минутах
    duration = ( datetime.strptime(record["конец"], "%d:%m:%Y %H:%M") - datetime.strptime(record["начало"], "%d:%m:%Y %H:%M") ).total_seconds() / 60
    return duration

def validate_records(records):
    """Проверка корректности исходных данных."""
    pass

def crosses_midnight(record, fmt): # Отмечает, переходит ли запись через 00
    start = datetime.strptime(record["начало"], fmt)
    end = datetime.strptime(record["конец"], fmt)

    record["crosses_midnight"] = start.date() != end.date()

    return record

def sort_daily_records(daily_records):  # Сортировка записей по датам
    sorted_items = sorted(
        daily_records.items(),
        key=lambda item: datetime.strptime(item[0], "%d:%m:%Y")
    )

    return dict(sorted_items)

def split_records_by_date(records): # Разделяет записи по дням, использует crosses_midnight, чтобы отметить записи, переходящие через 00
    fmt = "%d:%m:%Y %H:%M"
    daily_records = {}

    for record in records:

        record = crosses_midnight(record, fmt)

        start = datetime.strptime(record["начало"], fmt)
        end = datetime.strptime(record["конец"], fmt)

        current_start = start

        while current_start.date() < end.date():

            midnight = datetime.combine(
                current_start.date() + timedelta(days=1),
                datetime.min.time()
            )

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
        start_a = datetime.strptime(a["начало"], "%d:%m:%Y %H:%M")
        end_a = datetime.strptime(a["конец"], "%d:%m:%Y %H:%M")
        start_b = datetime.strptime(b["начало"], "%d:%m:%Y %H:%M")
        end_b = datetime.strptime(b["конец"], "%d:%m:%Y %H:%M")

        return start_a < end_b and start_b < end_a

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

def calculate_scores(variants, records): # формула оценки комбинации
    alpha = 0.5
    beta = 0.5

    records_by_index = {
        record["index"]: record
        for record in records
    }

    # максимальная продолжительность записи в комбинации (используется для нормировки при рассчете оценки)
    total_times = [
        sum(find_duration(records_by_index[i]) for i in variant)
        for variant in variants if variant
    ]

    t_max = max(total_times, default=0) 

    if t_max == 0:
        return {}

    # среднее качество (используется для нормировки при рассчете оценки)
    average_quality = ( 
        sum(record["качество"] for record in records) / len(records)
        if records else 0
    )

    scores = {}

    for variant in variants:
        if not variant:
            continue

        selected_records = [
            records_by_index[i] for i in variant
        ]

        total_time = sum( # Продолжительность записи      
            find_duration(record) for record in selected_records
        )

        min_quality = min( # минимальное качество записи в комбинации 
            record["качество"] for record in selected_records
        )

        t_norm = total_time / t_max                                             # нормировка
        q_norm = min_quality / average_quality if average_quality > 0 else 0

        scores[tuple(variant)] = alpha * t_norm + beta * q_norm # формула оценки, первое слагаемое отвечает за продолжительность, второе за качество

    return scores

def select_best_combination(variants, records): # выбирает лучшие комбинации за сутки

    scores = calculate_scores(variants, records)

    best_combinations = {}
    best_scores = {}

    for variant in variants:
        if not variant:
            continue

        score = scores[tuple(variant)]

        crossing_ids = {
            record["index"]
            for record in records
            if record["index"] in variant and record["crosses_midnight"]
        }

        category = tuple(crossing_ids)

        if category not in best_scores or score > best_scores[category]:
            best_scores[category] = score
            best_combinations[category] = variant

    return best_combinations

def select_overall_best(best_combinations_by_day, records): # объеденяет и вычисляет лучшую комбинацию из select_best_combinations

    dates = list(best_combinations_by_day.keys())

    if not dates:
        return []

    # Собираем все индексы переходящих записей
    possible_indexes = {}

    for date in dates:
        possible_indexes[date] = {
            index
            for key in best_combinations_by_day[date]
            for index in key
        }

    # Определяем индексы, общие для каждой пары соседних дней
    shared_indexes = {}

    for i in range(1, len(dates)):
        previous_date = dates[i - 1]
        current_date = dates[i]

        shared_indexes[current_date] = (
            possible_indexes[previous_date]
            & possible_indexes[current_date]
        )

    global_variants = set()

    # Рекурсивно перебираем совместимые дневные комбинации
    def backtrack(day_number, selected_indexes, previous_key):

        if day_number == len(dates):
            global_variants.add(tuple(sorted(selected_indexes)))
            return

        date = dates[day_number]

        for key, variant in best_combinations_by_day[date].items():

            current_key = set(key)

            if day_number > 0:

                shared = shared_indexes[date]

                previous_selected = set(previous_key) & shared
                current_selected = current_key & shared

                if previous_selected != current_selected:
                    continue

            backtrack(
                day_number + 1,
                selected_indexes | set(variant),
                key
            )

    backtrack(0, set(), ())

    variants = [
        list(variant)
        for variant in global_variants
    ]

    scores = calculate_scores(variants, records)

    if not scores:
        return []

    best_combination = max(scores, key=scores.get)

    return list(best_combination)

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

    # вывод объектов
    objects = {}
    for record in selected_records:
        satellite = record['спутник']
        index = record['index']
        quality = record['качество']

        if satellite not in objects or quality > int( records[int( objects[satellite] ) - 1]['качество'] ): # Добавляем объект и индекс записи если она ещё не встречалась, 
            objects[satellite] = index                                                                      # или обновляем индекс, если она имеет лучшее качество

    # Количество записей
    length = len(selected_records)

    # Среднее качество
    average_quality = sum(
        record["качество"]
        for record in selected_records
    ) / length

    # Худшее качество
    min_quality = min(
        record["качество"] for record in selected_records
    )

    # Общая продолжительность в минутах
    total_minutes = 0

    for record in selected_records:
        total_minutes += find_duration(record)

    # Переводим в часы и минуты
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)

    print(f"Лучшая комбинация непересекающихся записей: {best_variant}")
    print(f"Лучшая запись для каждого объекта: {objects}") # Лучшая запись для каждого объекта из best_variant
    print(f"Количество записей: {length}")
    print(f"Среднее качество записи: {average_quality:.2f}")
    print(f"Худшее качество записи: {min_quality:.2f}")
    print(f"Общая продолжительность: {hours} ч {minutes} мин")


def main():

    daily_records = split_records_by_date(set_indexes(records)) # Разделяем records по дням, расставляем индексы

    best_daily_records = {}

    for date, sublist in daily_records.items():  # Находим лучшие комбинации для каждого дня
        variants = find_combinations(sublist)

        best_combination = select_best_combination(
            variants,
            sublist,
        )

        best_daily_records[date] = best_combination

    best_variant = select_overall_best( # Находим итоговую комбинацию лучших записей
        best_daily_records,
        records
    )

    stats(best_variant, records) # Данные о записи
    pass


main()
