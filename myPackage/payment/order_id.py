from myPackage.payment import client

# Create  new order
class OrderId:
    def __init__(self, json_data):
        self.item_with_order_id = client.order.create(data=json_data) 
        
    def get_with_id(self):
        return self.item_with_order_id