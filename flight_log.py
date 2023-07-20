from dronekit import connect, VehicleMode
import flight_location
import datetime
import csv

# 機体に接続
vehicle = connect('tcp:127.0.01:5762', wait_ready=True, timeout=60)

# フライト開始(arm)するまで待機
print("Wait for arming...")
while not vehicle.armed:
    pass

# フライト開始(arm)
if(vehicle.armed):
    # フライト日付
    flight_date = datetime.date.today()
    # フライト開始時刻
    flight_start_time = datetime.datetime.now()
    on_time = flight_start_time.strftime("%H:%M:%S")
    # 離陸場所の住所
    latitude = vehicle.location.global_frame.lat
    longitude = vehicle.location.global_frame.lon
    start_location = flight_location.get_address_from_coordinates(latitude, longitude)
    
    print("ARMED")
    print("FLIGHT DATE: " + str(flight_date))
    print("OFF TIME: " + str(on_time))
    print("FROM: " + str(start_location))

# フライト終了(disarm)するまで待機
print("\nIn flight...")
while vehicle.armed:
    pass

# フライト終了(disarm)
if(not vehicle.armed):
    # フライト終了時刻
    flight_end_time = datetime.datetime.now()
    off_time = flight_end_time.strftime("%H:%M:%S")
    # フライト時間
    elapsed_time = flight_end_time - flight_start_time
    flight_time = str(elapsed_time.seconds // 3600) + ":" + str((elapsed_time.seconds % 3600) // 60) + ":" + str(elapsed_time.seconds % 60)
    # 着陸場所の住所
    latitude = vehicle.location.global_frame.lat
    longitude = vehicle.location.global_frame.lon
    end_location = flight_location.get_address_from_coordinates(latitude, longitude)

    print("DISARMED")
    print("ON TIME: " + str(on_time))
    print("FLIGHT TIME: " + str(flight_time))
    print("TO: " + str(start_location))


# flight log
flight_log = [flight_date, start_location, end_location, on_time, off_time, flight_time]

# フライトログ出力
print("\nOutputting flight log...")
with open('flight_log.csv', mode='a') as f: # 任意のディレクトリにログ出力用のcsvファイルを作成
    writer = csv.writer(f)
    writer.writerow(flight_log)

print("\nCompleted")
