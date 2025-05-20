import time
from dummy_sensor import DummySensor

class MissionComputer:
    def __init__(self):
        
        self.ds = DummySensor()
        
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
      def get_mission_computer_info(self):
        try:
            os_name = platform.system(),
            os_version = platform.version(),
            cpu_type = platform.processor(),
            cpu_cores = os.cpu_count()
            mem_bytes = psutil.virtual_memory().total
            mem_gb = round(mem_bytes / (1024 ** 3), 2)
        
            print('{')
            print(f'  "OS": "[os_name]",')
            print(f'  "OS Version": "[os_version]",')
            print(f'  "CPU Type": "[cpu_type]",')
            print(f'  "CPU Cores": "[cpu_cores]",')
            print(f'  "Memory Size": "[mem_gb]",')
            print('}')
       
          except Exception as e:
            print(f'시스템 정보를 가져오는 중 오류가 발생했습니다:, {e}')

    def get_mission_computer_load(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1),
            mem_usage = psutil.virtual_memory().percent
            
            print('{')
            print(f'  "CPU Usage (%)": "[cpu_usage]",')
            print(f'  "Memory Usage (%)": "[mem_usage]')
            print('}')
          
        except Exception as e:
            print(f'시스템 정보를 가져오는 중 오류가 발생했습니다:, {e}')

runComputer = MissionComputer()
runComputer.get_mission_computer_info()
runComputer.get_mission_computer_load()
