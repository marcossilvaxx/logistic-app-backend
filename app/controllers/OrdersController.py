from app.models.Order import Order, orders_schema
from app.models.Customer import Customer
from app.models.Company import Company

class OrdersController:
  def list(request):
    all_orders = orders_schema.dump(Order.query.all())
    
    return { "data": all_orders }, 200