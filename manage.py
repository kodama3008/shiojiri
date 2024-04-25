# import carla
# import random

# # Connect to the client and retrieve the world object
# client = carla.Client('localhost', 2000)
# world = client.get_world()

# # Set up the simulator in synchronous mode
# settings = world.get_settings()
# settings.synchronous_mode = True # Enables synchronous mode
# settings.fixed_delta_seconds = 0.05
# world.apply_settings(settings)

# # Set up the TM in synchronous mode
# traffic_manager = client.get_trafficmanager()
# traffic_manager.set_synchronous_mode(True)

# # Set a seed so behaviour can be repeated if necessary
# traffic_manager.set_random_device_seed(0)
# random.seed(0)

# # We will aslo set up the spectator so we can see what we do
# spectator = world.get_spectator()


import carla
import time
import random

client = carla.Client('localhost', 2000)
client.set_timeout(10.0)  # タイムアウトを10秒に設定

try:
    world = client.get_world()

    settings = world.get_settings()
    settings.synchronous_mode = True
    settings.fixed_delta_seconds = 0.05
    world.apply_settings(settings)

    traffic_manager = client.get_trafficmanager()
    traffic_manager.set_synchronous_mode(True)

    traffic_manager.set_random_device_seed(0)
    random.seed(0)
    spectator = world.get_spectator()
    # # シミュレーションの実行
    # while True:
    #     world.tick()  # 次のフレームに進む
    #     time.sleep(0.05)  # フレームレートの制御

except carla.TimeoutException:
    print("CARLAサーバーへの接続がタイムアウトしました。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")
finally:
    # シミュレーションの終了処理
    settings.synchronous_mode = False
    world.apply_settings(settings)
    print("シミュレーションを終了しました。")
