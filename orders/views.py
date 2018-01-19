from django.http import JsonResponse
from .models import ProductInBasket


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    numb = data.get("nmb")
    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                 defaults={"number": numb})
    if not created:
        new_product.number += int(numb)
        new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_numb = products_in_basket.count()
    return_dict["product_total_numb"] = products_total_numb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["numb"] = item.number
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)
