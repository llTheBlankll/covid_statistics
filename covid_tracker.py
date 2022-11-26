import json
import requests

class CovidTracker:
    """
    This is Philippines Data of Covid 19.
    """
    def __init__(self):
        self.user_agent: str = ""
        self.session: requests.Session = requests.Session()
        self.API: str = "https://covid19-api-philippines.herokuapp.com/api"
        
    def getSummary(self) -> str:
        data = self.session.get(self.API + "/summary")
        return data.text


def main():
    ct = CovidTracker()
    json_data: dict = json.loads(ct.getSummary())
    print("Current state of the Philippines from COVID-19")
    print("Total: %s" % json_data.get("data")["total"])
    print("Recoveries: %s" % json_data.get("data")["recoveries"])
    print("Deaths: %s" % json_data.get("data")["deaths"])
    print("Active Cases: %s" % json_data.get("data")["active_cases"])
    print("Fatality Rate: %s" % json_data.get("data")["fatality_rate"])
    print("Recovery Rate: %s" % json_data.get("data")["recovery_rate"])

if __name__ == "__main__":
    main()
    