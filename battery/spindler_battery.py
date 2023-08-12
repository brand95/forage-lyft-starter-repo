from datetime import datetime
from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        current_date = datetime.today().date()
        return (current_date - self.last_service_date).days >= 730  # 2 years
