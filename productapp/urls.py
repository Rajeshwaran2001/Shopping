from django.urls import path
from . import views

urlpatterns = [
 path('',views.home,name='home'),
 path('listcategory',views.listCategory,name='listcategory' ),
 path('insertcategory/',views.insertCategory,name='insertcategory'),
 path('insertcategory/<int:id>',views.insertCategory,name='editcategory'),
 path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),
 path('listproduct',views.listProduct,name='listproduct' ),
 path('insertproduct/',views.insertProduct,name='insertproduct'),
 path('insertproduct/<int:id>',views.insertProduct,name='editproduct'),
 path('deleteproduct/<int:id>',views.deleteProduct,name='deleteproduct'),

]
