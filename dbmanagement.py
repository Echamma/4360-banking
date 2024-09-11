import json

class dbManagement:
    def __init__(self):
        self.data = None

    def read_file(self):
        try:
            with open("data.json", "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return None

    def update_customer(self, customer_id, new_data):
        data = self.read_file()
        for customer in data:
            if customer["accountNumber"] == customer_id:
                customer.update(new_data)
                self.write_file(data)
                return data
        print(f"Customer with ID {customer_id} not found")
        return data

    def write_file(self, data):
        with open("data.json", "w") as f:
            json.dump(data, f)