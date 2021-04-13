import cars
import insurance
import profiles

# ss =                                                  # страховая сумма
# tbd = 'Audi A1'                                       # коэффициент для каждой модели авто в процентах
# kv = [1, 1.14, 1.25, 1.38, 1.52, 1.67, 1.78, 1.86]    # коэффициент возраста тс
kfr = 0.8                                               # коэффициент в зависимости о твеличины франшизы, всегда 2%
# kvs =                                                 # коэффициент возраста - стажа водителя
# parking_sum = car_price * (tbs * kv * kfr + tx)

def test_1():
    print(893230 * (0.0132 * 1.67 * 0.8 + 0.0055))




def test():
    profiles.profiles_prepare()
    profiles.profiles_accept_prepared()
    cars.car_change()

    print(insurance.test_get_poffers_parking())

