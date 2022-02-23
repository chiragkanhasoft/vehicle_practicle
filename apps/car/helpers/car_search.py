import json

import requests


class carExistance:
    def check_car_existance(self, make, model):
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
        }
        results = requests.request("GET", url=url, headers=headers)

        # CHECK RESPONSE STATUS #
        if results.ok:
            res = results.json()

            # GET RESULT FROM RESPONSE #
            car_list = res.get("Results")

            # FIND MODEL FROM RESPONSE USING MODEL NAME #
            model_check = list(
                filter(
                    lambda car_obj: (
                        car_obj.get("Model_Name").lower() == model.lower()
                    ),
                    car_list,
                )
            )

            # IF MODEL EXIST RETURN TRUE OTHERWISE RETURN FALSE #
            if model_check:
                return True
            else:
                return False
        else:
            # RETURN FALSE IF API SEND OTHER RESPONSE #
            return False
