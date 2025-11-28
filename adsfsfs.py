number_day = int(input())
weghit = float(input())
plan = weghit - number_day * 0.2
if weghit <= plan:
    print("Все идет по плану")
    print(
        "#{0}  ДЕНЬ: ТЕКУЩИЙ ВЕС = {1} кг, ЦЕЛЬ по ВЕСУ = {2} кг".format(
            number_day, weghit, plan
        )
    )
else:
    print("Что-то пошло не так")
    print(
        "#{0}  ДЕНЬ: ТЕКУЩИЙ ВЕС = {1} кг, ЦЕЛЬ по ВЕСУ = {2} кг".format(
            number_day, weghit, plan
        )
    )
