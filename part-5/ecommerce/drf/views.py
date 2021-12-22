from django.shortcuts import get_object_or_404
from ecommerce.drf.serializer import ProductInventorySerializer
from ecommerce.inventory.models import Product, ProductInventory
from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response


class ProductByCategory(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
):
    """
    API endpoint that returns products by category
    """

    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None):
        queryset = ProductInventory.objects.filter(
            product__category__slug=slug,
        ).filter(is_default=True)[:10]
        serializer = ProductInventorySerializer(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


# class AllProductViewSet(
#     viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
# ):
#     """
#     API endpoint that returns all products
#     """

#     queryset = Product.objects.all()
#     serializer_class = AllProductSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     lookup_field = "slug"

#     def retrieve(self, request, slug=None):
#         queryset = Product.objects.filter(category__slug=slug)[:10]
#         serializer = AllProductSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # category = self.request.query_params.get("category__slug")
#     # lookup_field = "category__slug"
#     # http_method_names = ["get", "head"]


# # class SingleProductViewSet(
# #     viewsets.GenericViewSet,
# #     mixins.RetrieveModelMixin,
# # ):
# #     """
# #     API endpoint that returns single Item
# #     """

# #     queryset = ProductInventory.objects.all()
# #     serializer_class = SingleProductSerializer
# #     lookup_field = "product__web_id"

# #     def retrieve(self, request, sku=None):
# #         queryset = ProductInventory.objects.filter(sku=sku)
# #         serializer = SingleProductSerializer(queryset, many=True)
# #         print(serializer)
# #         return Response(serializer.data)


# class SingleProductViewSet(viewsets.ViewSet):
#     """
#     https://www.django-rest-framework.org/api-guide/viewsets/
#     """

#     # queryset = ProductInventory.objects.all()
#     # serializer_class = SingleProductSerializer
#     # lookup_field = "product__web_id"

#     def list(self, request, id=None):

#         filter_arguments = []
#         q = ProductInventory.objects.all()

#         if request.GET:
#             for value in request.GET.values():
#                 filter_arguments.append(value)
#             queryset = get_object_or_404(q, product__web_id=id)

#         else:
#             queryset = get_object_or_404(q, product__web_id=id, is_default=True)

#         serializer = SingleProductSerializer(queryset)
#         return Response(serializer.data)

#     #     """
#     #     A list of foo objects.
#     #     """
#     #     context = {"request": self.request}
#     #     queryset = Foo.objects.all()
#     #     serializer = FooSerializer(queryset, many=True, context=context)
#     #     return Response(serializer.data)

#     # def retrieve(self, request):
#     #     queryset = ProductInventory.objects.filter(sku=sku)
#     #     serializer = SingleProductSerializer(queryset, many=True)
#     #     return Response(serializer.data)

#     # @action(methods=["get"], detail=True)
#     # def singleitem(self, request, pk=None):
#     #     queryset = ProductInventory.objects.filter(pk=pk)
#     #     serializer = SingleProductSerializer(queryset, many=True)
#     #     return Response(serializer.data)
