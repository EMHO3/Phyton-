items=[
  {
    "producto":"polo",
    "precio":100

  },
  {
    "producto":"short",
    "precio":120
  },
{
  "producto":"sabana",
  "precio":500
}
]

prices=list(map(lambda item:item["precio"],items))
print(prices)

def add_taxes(item):
  new_item=item.copy()
  new_item["taxes"]=item["precio"]*.19
  return item

new_items=list(map(add_taxes,items))
print("new items")
print(new_items)
print("old items")
print(items)