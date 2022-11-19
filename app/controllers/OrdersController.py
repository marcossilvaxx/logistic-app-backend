from app.models.Order import Order, orders_schema
from app.models.OrderItem import OrderItem
from sqlalchemy import or_

class OrdersController:
  def list(request):
    search = request.args.get('search')
    date = request.args.get('date')
    limit = request.args.get('limit')
    page = request.args.get('page')
    
    orders_result = Order.query
    
    if search:      
      search_string = f"%{search}%"
      
      orders_result = orders_result.join(OrderItem).filter(or_(Order.name.like(search_string), OrderItem.product.like(search_string)))
    
    if date:
      dateRange = date.split(",")
      
      orders_result = orders_result.filter(Order.created_at.between(dateRange[0], dateRange[1]))
    
    total = len(orders_result.all())
    
    orders_result = orders_result.paginate(page=int(page) if page else 1, per_page=int(limit) if limit else None, count=False)
    
    all_orders = orders_schema.dump(orders_result.items)
    
    return { "data": all_orders, "total": total }, 200