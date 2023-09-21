import random


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}

    weathers = {"солнечная": True, "дождливая": False}

    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella(weathers)
    return step2_no_umbrella(weathers)


def step2_umbrella(weathers):
    print("\nУтка-маляр 🦆 решил на всякий случай взять с собой зонтик, "
          "ведь он не посмотрел прогноз погоды.")

    weathers = {"солнечная": True, "дождливая": False}
    weather = input("Какая сегодня погода ({}/{})?: ".format(*weathers))

    drinks = {"cold": ["пиво", "коктейль", "напиток", "кумыс"],
              "warm": ["чай с лимоном", "кофе", "горячий шоколад"]}
    drink = ""

    if weathers[weather]:
        print("С погодой повезло, "
              "а вот с решением взять зонт нет. ")

        print("\nРаз уж погода хорошая, можно выпить что-то холодное.\n"
              "В меню сегодня из холодного "
              "{}, {}, {}, {}".format(*drinks["cold"]))

        angry_counter = 3
        while drink not in drinks["cold"]:
            if angry_counter == 0:
                print("\nУтка-маляр 🦆 сегодня был не в себе и "
                      "заказывал того, чего нет в меню. Разозленный "
                      "бармен позвал охранника и он выпнул утку.")
                print("Утка-маляр 🦆 пришел домой без нас настроения. "
                      "Его разочарование неизмеримо, его день испорчен.")
                return

            drink = input("Чего желает Утка-маляр 🦆: ")

            if drink in drinks["warm"]:
                print("\nУтка-маляр 🦆 решил выпить горячее "
                      "в жаркую погоду. Ну, это его выбор)")
                return
            elif drink not in drinks["cold"]:
                angry_counter -= 1
                if angry_counter > 0:
                    print("Бармен: у нас в меню нет такого выбора. "
                          "Попробуйте что-то другое.")

        if drink == "кумыс":
            print("\nСчастливый Утка-маляр 🦆 пришел домой забыв "
                  "взять свой зонтик ☂️ из-за выпитового кумыса")
            return
        else:
            print(f"\nУтка-маляр 🦆 выпил несколько бокалов {drink} "
                  "и разговорился с другими утками 🦆🦆🦆")
            print("Так они и просидели до ночи.")
            return
    else:
        print("\nВзять зонт был отличным решением.")
        print("Хоть и Утка-маляр 🦆 не промок, но нужно согреться")

        while drink not in drinks["warm"]:
            print("\nИз горячих напитков в меню "
                  "{}, {}, {}".format(*drinks["warm"]))
            drink = input("Что же выбрать: ")

            if drink in drinks["cold"]:
                print("\nВ такую холодную погоду Утка-маляр 🦆 "
                      f"решил выпить {drink}")
                print("Главное теперь не заболеть")
                return
            elif drink not in drinks["warm"]:
                print("\nВыберите что-то из меню")

        print("\nСогревшись и разговорившись с барменом "
              "Утка-маляр 🦆 чуть не пропустил свой автобус")
        return


def step2_no_umbrella(weathers):
    weather = random.choice(list(weathers.keys()))

    if weathers[weather]:
        print("\nПрогноз погоды на сегодня - "
              "день солнечный")
        print("Повезло, повезло! "
              "Можно спокойно отдохнуть в баре")
    else:
        print("\nПрогноз погоды на сегодня - "
              "ливень")
        print("Оставшись под сильным ливнем, "
              "Утка-маляр 🦆 не смог дойти до бара "
              "и сев в автобус пошел домой")

    print("")


if __name__ == '__main__':
    step1()
