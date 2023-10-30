import random

# Список подозреваемых
suspects = ["Джон", "Мэри", "Майк", "Лиза", "Том"]
# Словарь мест преступления
crime_scenes = {
    "Кухня": "Кровь на полу",
    "Гостиная": "Разбитое окно",
    "Спальня": "Перевернутая мебель"
}
# Множество найденных улик
evidence = set()
# Флаги для проверки прогресса игры
found_suspect = False
found_scene = False

def welcome_message():
    print("Добро пожаловать в игру 'Детектив'!")
    print("Ваша задача - расследовать убийство")
    print("Удачи!")

def choose_suspect():
    print("Выберите подозреваемого:")
    for i, suspect in enumerate(suspects):
        print(f"{i+1}. {suspect}")
    choice = input("Введите номер подозреваемого: ")
    suspect_index = int(choice) - 1
    suspect = suspects[suspect_index]
    print(f"Вы выбрали подозреваемого: {suspect}")
    return suspect

def investigate_scene():
    print("Места преступления:")
    for scene, evidence in crime_scenes.items():
        print(f"{scene}: {evidence}")
    scene = input("Введите место преступления: ")
    print(f"Вы расследуете преступление на {scene}")
    return scene

def find_evidence():
    evidence_type = input("Введите тип улики: ")
    evidence.add(evidence_type)
    print(f"Вы нашли улику: {evidence_type}")

def check_progress():
    global found_suspect, found_scene
    if not found_suspect:
        print("Вы должны сначала выбрать подозреваемого!")
    elif not found_scene:
        print("Вы должны сначала расследовать место преступления!")
    else:
        print("Вы нашли все необходимые улики и задокументировали их!")

def game():
    welcome_message()

    suspect = choose_suspect()
    found_suspect = True

    print("Вы получили информацию от свидетеля")
    witness_statement = "Подозреваемый был на месте преступления вечером"
    print(f"Информация от свидетеля: {witness_statement}")

    scene = investigate_scene()
    found_scene = True

    print("Вы нашли орудие преступления")
    weapon = "Нож"
    print(f"Орудие преступления: {weapon}")

    print("Вы анализируете улики...")
    print("Найдены отпечатки пальцев на ноже")
    print("Обнаружены следы обуви на месте преступления")

    find_evidence()
    find_evidence()

    check_progress()

game()