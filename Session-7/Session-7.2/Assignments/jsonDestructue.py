import json

with open("ecommerce_data.json", "r") as file:
  data = json.load(file)
  store_name = data["store"]["name"]
  country = data["store"]["location"]["country"]
  customers = data["customers"]
  laptop = data["products"][0]
  processor = laptop["specifications"]["processor"]
  ram = laptop["specifications"]["ram_gb"]
  
  payment_method = data["orders"][0]["payment"]["method"]
  
  print("Store Name : ",store_name)
  print("Country : ",country)
  for customer in customers:
    print("Name of Customer : ",customer["name"])
  print("Processor : ",processor)
  print("RAM : ",ram)
  print("First Customer Name : ", customers[0]["name"], "\nMembership : ", customers[0]["membership"]["level"])

  for product in products:
    print("Name of Product : ", product["name"])
    print("Selling Price : ", product["price"]["selling_price"])

  print("Payment Method of First Order : ", payment_method)
