from datetime import date, datetime

from django.db import models

# Create your models here.
class tbl_supplier_request(models.Model):
    name=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)
    email=models.EmailField(max_length=200,null=True)
    address = models.TextField(max_length=200, null=True)
    licence_number = models.CharField(max_length=200, null=True)
    proof = models.FileField(upload_to="media",null=True)
    password=models.CharField(max_length=100,null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)


class tbl_material_category(models.Model):
    supplier=models.ForeignKey(tbl_supplier_request,on_delete=models.CASCADE,null=True)
    category=models.CharField(max_length=100,null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)


class tbl_material(models.Model):
    category=models.ForeignKey(tbl_material_category,on_delete=models.CASCADE,null=True)
    supplier=models.ForeignKey(tbl_supplier_request,on_delete=models.CASCADE,null=True)
    material=models.CharField(max_length=200,null=True)
    material_Durability=models.CharField(max_length=200,null=True)
    material_density = models.CharField(max_length=100,null=True)
    material_Water_absorption  = models.CharField(max_length=200,null=True)
    strength=models.CharField(max_length=100,null=True)
    Hardness=models.CharField(max_length=100,null=True)
    Elasticity=models.CharField(max_length=200,null=True)
    Thermal_capacity = models.CharField(max_length=200,null=True)
    price=models.IntegerField(null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)

class tbl_registration(models.Model):
    name=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=100,null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)


class tbl_uploaded_plan(models.Model):
    user=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    plan=models.FileField(null=True,upload_to="media")
    price=models.IntegerField(null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)


class tbl_design_plan(models.Model):
    user=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    plan=models.FileField(upload_to="media",null=True)
    price=models.IntegerField(null=True)
    building_type=models.CharField(max_length=100,null=True)
    sq_ft=models.CharField(max_length=100,null=True)
    bays=models.CharField(max_length=100,null=True)
    beds=models.CharField(max_length=100,null=True)
    baths=models.CharField(max_length=100,null=True)
    width=models.CharField(max_length=100,null=True)
    depth=models.CharField(max_length=100,null=True)
    Image=models.ImageField(upload_to="media",null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)


class final_cost_uploaded(models.Model):
    user=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    plan=models.FileField(upload_to="media",null=True)
    cost=models.IntegerField(null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)

class final_cost_designed(models.Model):
    user=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    plan=models.FileField(upload_to="media",null=True)
    cost=models.IntegerField(null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)



class tbl_material_orders(models.Model):
    consumer=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    supplier=models.ForeignKey(tbl_supplier_request,on_delete=models.CASCADE,null=True)
    material=models.ForeignKey(tbl_material,on_delete=models.CASCADE,null=True)
    customer_name=models.CharField(max_length=100,null=True)
    customer_mobile=models.IntegerField(null=True)
    customer_email=models.EmailField(null=True)
    pincode=models.IntegerField(null=True)
    flat=models.CharField(max_length=200,null=True)
    area=models.CharField(max_length=200,null=True)
    landmark=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    instructions=models.TextField(max_length=1000,null=True)
    total_price=models.IntegerField(null=True)
    reject_reason=models.TextField(max_length=700,null=True)
    delivery_date=models.DateField(max_length=200,null=True)
    quantity=models.IntegerField(null=True)
    payment_mode=models.CharField(max_length=100,null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True,default="Not Assigned")

class tbl_feedback(models.Model):
    order=models.ForeignKey(tbl_material_orders,on_delete=models.CASCADE,null=True)
    supplier=models.ForeignKey(tbl_supplier_request,on_delete=models.CASCADE,null=True)
    material=models.ForeignKey(tbl_material,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_registration,on_delete=models.CASCADE,null=True)
    feedback=models.TextField(max_length=1000,null=True)
    dt=models.DateField(null=True,auto_now_add=True)
    tm=models.TimeField(null=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True)

