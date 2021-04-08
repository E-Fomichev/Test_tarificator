import cars
import insurance
import profiles

# ss =                                                  # страховая сумма
# tbd = 'Audi A1'                                       # коэффициент для каждой модели авто в процентах
# kv = [1, 1.14, 1.25, 1.38, 1.52, 1.67, 1.78, 1.86]    # коэффициент возраста тс
# kfr = [0.8, 0.75, 0.65, 0.55, 0.5]                    # коэффициент в зависимости о твеличины франшизы
# kvs =                                                 # коэффициент возраста - стажа водителя

def test():
    profiles.profiles_prepare()
    profiles.profiles_accept_prepared()
    cars.car_change()

    print(insurance.test_get_poffers_parking())