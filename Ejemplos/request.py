import requests
import json


class Request:
    dic_response = {}

    def request_user(self):
        page = 0
        pages = 2
        while page < pages:
            page = page + 1
            try:
                response = requests.get('https://reqres.in/api/users?page=%i' % page)
                json_data = response.json()['data']
                for data in json_data:
                    self.dic_response[data['email']] = self.dic_response.get(data['email'], data)
            except ValueError:
                print("Error, the request could not be made.")
                break
        if len(self.dic_response) != 0:
            print(json.dumps(self.dic_response, indent=4))


my_request = Request()
my_request.request_user()
