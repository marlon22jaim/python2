items = [
    {
        "product": "camisa",
        "price": 100,
    },
    {
        "product": "pantalones",
        "price": 300,
    },
    {
        "product": "pantalones 2",
        "price": 200,
    }
]

# prices = [100, 300, 200]
prices = list(map(lambda item: item["price"], items))


def add_taxes(item):
    ## se usa la funcion copy para copiar los datos de item sin copiar la referencia y asi no modificar el item original
    item_v2 = item.copy()
    item_v2["taxes"] = item_v2["price"]*.19
    return item_v2


new_items = list(map(add_taxes, items))
print("nueva lista", new_items)
print("antigua lista", items)
