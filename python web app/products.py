import datetime
from sql_connection import get_sql_connection
def get_all_results(connection):
  

  cursor=connection.cursor()
  query="SELECT * FROM sql_inventory.products;"
  cursor.execute(query)
  response=[]
  for (product_id,name,quantity_in_stock,unit_price) in cursor:
      response.append(
        {
          "product_id":product_id,
          "name":name,
          "quantity_in_stock":quantity_in_stock,
          "unit_price":unit_price
        }
      )
  return response

def add_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO sql_inventory.products "
             "(name, quantity_in_stock, unit_price)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['quantity_in_stock'], product['unit_price'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid
  
def del_product(connection,product_id):
  cursor=connection.cursor()
  query=("delete from sql_inventory.products where product_id = " + str(product_id))
  cursor.execute(query)
  connection.commit()

if __name__ =="__main__":
  Connection= get_sql_connection()
  print(get_all_results(Connection))
  # print(add_product(Connection,{
    
  #   "product_name":"microsoft",
  #   "quantity_in_stock":"546",
  #   "unit_price":"6.15"
  # }))
  # print(del_product(Connection,18))