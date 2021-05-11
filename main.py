from carmd import CarMD
import ast

# Use Car MD api

def Pull_carMD_car_data_using_api(vin_number):
    api_auth_and_token = {'authorization': 'Put yours',
                           'token':'Put yours'}

    filename = ['output_Maintlist.txt', 'output_recall.txt', 'output_warranty.txt']

    car = CarMD(api_auth_and_token['authorization'],
                api_auth_and_token['token'])

    my_vehicle = car.vin(vin_number)

    mantinenance_list_dic = my_vehicle.maintenance_list()
    recalls = my_vehicle.recalls()
    warrenty = my_vehicle.warranty()


    with open(filename[0], 'w') as text_file:
        text_file.write(str(mantinenance_list_dic))

    with open(filename[1], 'w') as text_file:
        text_file.write(str(recalls))

    with open(filename[2], 'w') as text_file:
        text_file.write(str(warrenty))


Pull_carMD_car_data_using_api('enter your vin here')

with open('output_warranty.txt') as f:
   data = f.read()

d = ast.literal_eval(data)

print(d.keys())
print(d['message']['code'])
print(d['message']['message'])
print(d['message']['credentials'])
print(d['message']['endpoint'])
print(d['message']['counter'])
print('-----------------------------------------------------')

for i in range(len(d['data'])):
    print(d['data'][i])
    print('-----------------------------------------------------')




