import json

from org.swallow_labs.log.LoggerAdapter import LoggerAdapter
from org.swallow_labs.model.Parser import Parser

class ReservationHandler:
    """
                DESCRIPTION
                ===========
                This method set plannig.json files with new  informations video and photo 

    
        """
        
    global my_logger
    my_logger = LoggerAdapter(Parser().get_device_log_param())
    
    
    def __init__(self):
        pass
    
    def book_segment(self,res_dict):
        """
                DESCRIPTION
                ===========
                This method set plannig.json file with new  informations video and photo 

    
        """
        
        print("res_dict",res_dict)
        with open("../conf/Configuration_Display.json", "r") as json_config:
            config = json.load(json_config)
            json_config.close()
        res_day_path = config["reservation_root_directory"] + "/" + res_dict["segment_id"][:-5].replace("-", "/") + "Planning.json"
        hour_id, segment_id = res_dict["segment_id"][-5:].split("-")
        print(res_day_path)
        with open(res_day_path, "r") as json_data:
            data = json.load(json_data)
            json_data.close()
        segment_duration = int(data["planning"]["segment_duration_min"])
        print("segment_duration",int(segment_id) // segment_duration)
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // segment_duration]["holder"] = res_dict["holder"]
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // segment_duration]["video"]["id"] = res_dict["video"]
        data["planning"]["heure"][int(hour_id)]["creneau"][int(segment_id) // segment_duration]["photo"]["id"] = res_dict["photo"]
                   
        with open(res_day_path, "w") as json_data:
            json.dump(data, json_data)
            json_data.close()
            print("done")
            print("segment",int(segment_id))
            print("segment_duration",segment_duration)
            print("index",int(segment_id) // segment_duration)

        my_logger.log_Reservation_info(res_day_path)
    
    def book_multiple_segment(self,res_dict):
        for i in res_dict:
            self.book_segment(i)

    
    def generate_res_dict(self,reservation_msg_queue):
        """
                DESCRIPTION
                ===========
                This method set json_data list from capsule informations

    
        """
        json_data = []
        for i in reservation_msg_queue:
            json_data.append(i.get_payload())
        return json_data



