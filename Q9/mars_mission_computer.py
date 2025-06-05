import time
import threading
import multiprocessing


class MissionComputer:
    def get_mission_computer_info(self):
        while True:
            print('[INFO] Mission Computer Info: System nominal.')
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            print('[LOAD] Mission Computer Load: CPU 45%, Memory 62%.')
            time.sleep(20)

    def get_sensor_data(self):
        for i in range(5):
            print('[SENSOR] Sensor Data Received:', i)
            time.sleep(5)


def run_threads(computer):
    info_thread = threading.Thread(target=computer.get_mission_computer_info)
    load_thread = threading.Thread(target=computer.get_mission_computer_load)
    sensor_thread = threading.Thread(target=computer.get_sensor_data)

    info_thread.daemon = True
    load_thread.daemon = True
    sensor_thread.daemon = True

    info_thread.start()
    load_thread.start()
    sensor_thread.start()

    # 메인 쓰레드가 종료되지 않도록 유지
    sensor_thread.join()


def run_process(computer):
    p1 = multiprocessing.Process(target=computer.get_mission_computer_info)
    p2 = multiprocessing.Process(target=computer.get_mission_computer_load)
    p3 = multiprocessing.Process(target=computer.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    # 멀티 쓰레드 실행
    print('[STEP 1] Running with single instance and multithreading...')
    runComputer = MissionComputer()
    thread_controller = threading.Thread(target=run_threads, args=(runComputer,))
    thread_controller.start()
    thread_controller.join(timeout=30)

    # 멀티 프로세스 실행
    print('[STEP 2] Running with multiple instances and multiprocessing...')
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    p1 = multiprocessing.Process(target=run_process, args=(runComputer1,))
    p2 = multiprocessing.Process(target=run_process, args=(runComputer2,))
    p3 = multiprocessing.Process(target=run_process, args=(runComputer3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
