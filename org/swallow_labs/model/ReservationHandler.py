import json


class ReservationHandler:
    def __init__(self):
        pass
    
    def book_segment(self,res_dict):
        with open("../conf/Configuration_Display.json", "r") as json_config:
            config = json.load(json_config)
            json_config.close()
        res_day_path = config["reservation_root_directory"] + "/" + res_dict["segment_id"][:-5].replace("-", "/") + "Planning.json"
        hour_id, segment_id = res_dict["segment_id"][-5:].split("-")
        print(res_day_path)
        with open(res_day_path, "r") as json_data:
            data = json.load(json_data)
            json_data.close()
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // config["segment_duration_min"]]["holder"] = res_dict["holder"]
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // config["segment_duration_min"]]["video"]["id"] = res_dict["video"]
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // config["segment_duration_min"]]["photo"]["id"] = res_dict["photo"]
        with open(res_day_path, "w") as json_data:
            json.dump(data, json_data)
            json_data.close()
            print("done")
            print(int(segment_id))
            print(int(segment_id) % config["segment_duration_min"])

    
    def book_multiple_segment(self,res_dict):
        for i in res_dict:
            self.book_segment(i)

    
    def generate_res_dict(self,reservation_msg_queue):
        json_data = []
        for i in reservation_msg_queue:
            json_data.append(i.get_payload())
        return json_data



