from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def admin_login(request):
    return render(request, 'admin_login.html')


def admin_login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin_dashboard/")
        else:
            return redirect("/admin_login/")


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def supplier_request(request):
    return render(request, "supplier_request.html")


def save_supplier_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        licence_number = request.POST.get("licence number")
        proof = request.FILES["proof"]
        data = tbl_supplier_request()
        data.name = name
        data.email = email
        data.mobile = mobile
        data.address = address
        data.licence_number = licence_number
        data.proof = proof
        data.save()
        return redirect("/")


def view_supplier_request(request):
    d = tbl_supplier_request.objects.all()
    return render(request, "view_supplier_request.html", {"d": d})


def approve_request(request, id):
    f = tbl_supplier_request.objects.get(id=id)
    return render(request, "approve_request.html", {"f": f})


def save_approve_request(request, id):
    f = tbl_supplier_request.objects.get(id=id)
    f.password = request.POST.get("password")
    f.status = "True"
    f.save()
    return redirect("/view_supplier_request/")


def reject_request(request, id):
    f = tbl_supplier_request.objects.get(id=id)
    f.status = "False"
    f.save()
    return redirect("/view_supplier_request/")


def user_login(request):
    return render(request, "user_login.html")


def user_registration(request):
    return render(request, "user_registration.html")


def user_login_check(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if tbl_supplier_request.objects.filter(email=email, password=password, status=True).exists():
            log_obj = tbl_supplier_request.objects.get(email=email, password=password, status=True)
            request.session["supplier_id"] = log_obj.id
            return redirect("/supplier_dashboard/")
        elif tbl_registration.objects.filter(email=email, password=password).exists():
            log_obj = tbl_registration.objects.get(email=email, password=password)
            request.session["userid"] = log_obj.id
            return redirect("/user_dashboard/")
        else:
            return HttpResponse("Invalid data")


def supplier_dashboard(request):
    return render(request, "supplier_dashboard.html")


def add_material_category(request):
    return render(request, "add_material_category.html")


def category_save(request):
    if request.method == "POST":
        supplier_id = request.session["supplier_id"]
        category = request.POST.get("category")
        g = tbl_material_category()
        g.category = category
        g.supplier_id = supplier_id
        g.save()
        return redirect("/add_material_category/")


def view_material_category(request):
    supplier_id = request.session["supplier_id"]
    c = tbl_material_category.objects.filter(supplier=supplier_id)
    return render(request, "view_material_category.html", {"c": c})


def add_material(request):
    supplier_id = request.session["supplier_id"]
    f = tbl_material_category.objects.filter(supplier=supplier_id)
    return render(request, "add_material.html", {"f": f})


def material_save(request):
    if request.method == "POST":
        g = tbl_material()
        supplier_id = request.session["supplier_id"]
        g.supplier_id = supplier_id
        g.category_id = request.POST.get("category")
        g.material = request.POST.get("material")
        g.material_Durability = request.POST.get("durability")
        g.material_density = request.POST.get("density")
        g.material_Water_absorption = request.POST.get("water_absorption")
        g.strength = request.POST.get("strength")
        g.Hardness = request.POST.get("hardness")
        g.Elasticity = request.POST.get("elasticity")
        g.Thermal_capacity = request.POST.get("thermal_capacity")
        g.price = request.POST.get("price")
        g.save()
        return redirect("/add_material/")


def save_registration(request):
    if request.method == "POST":
        d = tbl_registration()
        d.name = request.POST.get("name")
        d.email = request.POST.get("email")
        d.mobile = request.POST.get("mobile")
        d.password = request.POST.get("password")
        d.save()
        return redirect("/user_login/")


def user_dashboard(request):
    return render(request, "user_dashboard.html")


def upload_plan(request):
    return render(request, "upload_plan.html")


def send_plan(request):
    if request.method == "POST":
        d = tbl_uploaded_plan()
        userid = request.session["userid"]
        d.user_id = userid
        d.plan = request.FILES["plan"]
        d.save()
        return redirect("/user_dashboard/")


def design_plan(request):
    return render(request, "design_plan.html")


def save_design_plan(request):
    if request.method == "POST":
        gg = tbl_design_plan()
        userid = request.session["userid"]
        gg.user_id = userid
        gg.building_type = request.POST.get("building_type")
        gg.beds = request.POST.get("beds")
        gg.bays = request.POST.get("bays")
        gg.baths = request.POST.get("baths")
        gg.width = request.POST.get("width")
        gg.depth = request.POST.get("depth")
        gg.sq_ft = request.POST.get("sq_ft")
        im = request.FILES["image"]
        fs = FileSystemStorage()
        i = fs.save(im.name, im)
        u = fs.url(i)
        gg.Image = u
        gg.save()
        return redirect("/design_plan/")


def admin_view_plan_details(request):
    bb = tbl_design_plan.objects.all()
    return render(request, "admin_view_plan_details.html", {"bb": bb})


def admin_view_uploaded_plan(request):
    bb = tbl_uploaded_plan.objects.all()
    return render(request, "admin_view_uploaded_plan.html", {"bb": bb})


def send_plan_to_user(request, id):
    ff = tbl_design_plan.objects.get(id=id)
    return render(request, "send_plan_to_user.html", {"ff": ff})


def save_send_plan_user(request, id):
    ff = tbl_design_plan.objects.get(id=id)
    ff.plan = request.FILES["plan"]
    ff.save()
    return redirect("/admin_dashboard/")


def uploaded_cost_estimation(request, id):
    data = tbl_uploaded_plan.objects.get(id=id)
    return render(request, "uploaded_cost_estimation.html", {"data": data})


def save_cost_uploaded(request, id):
    data = tbl_uploaded_plan.objects.get(id=id)
    data.price = request.POST.get("cost")
    data.save()
    return redirect("/admin_view_uploaded_plan/")


def uploaded_plan_cost_user(request):
    userid = request.session["userid"]
    data = tbl_uploaded_plan.objects.filter(user=userid)
    return render(request, "uploaded_plan_cost_user.html", {"data": data})


def approve_uploaded_cost(request, id):
    d = tbl_uploaded_plan.objects.get(id=id)
    d.status = "Approved"
    d.save()
    c = final_cost_uploaded()
    c.cost = d.price
    c.plan = d.plan
    c.user_id = d.user.id
    c.save()
    return redirect("/payment_method/")


def reject_uploaded_cost(request):
    d = tbl_uploaded_plan.objects.get(id=id)
    d.status = "Reject"
    d.save()
    return redirect("/uploaded_plan_cost_user/")


def designed_plan_view(request):
    userid = request.session["userid"]
    f = tbl_design_plan.objects.filter(user=userid)
    return render(request, "designed_plan_view.html", {"f": f})


def admin_view_design_plan_details(request):
    data = tbl_design_plan.objects.all()
    return render(request, "admin_view_design_plan_details.html", {"data": data})


from django.http import FileResponse, HttpResponse
import os


def view_user_designed_plan(request, id):
    data = tbl_design_plan.objects.get(id=id)
    filepath = os.path.join('media', data.plan.name)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def approve_designed_cost(request,id):
    f=tbl_design_plan.objects.get(id=id)
    f.status = "Approved"
    f.save()
    return redirect("/designed_plan_view/")


def admin_set_designed_cost(request):
    data=tbl_design_plan.objects.filter(status="Approved")
    return render(request,"admin_set_designed_cost.html",{"data":data})

def admin_send_designed_cost(request,id):
    data = tbl_design_plan.objects.get(id=id)
    return render(request, "admin_send_designed_cost.html", {"data": data})


def save_design_cost_uploaded(request,id):
    data = tbl_design_plan.objects.get(id=id)
    data.price = request.POST.get("cost")
    data.save()
    return redirect("/admin_set_designed_cost/")


def designed_plan_cost(request):
    userid=request.session["userid"]
    data=tbl_design_plan.objects.filter(user=userid)
    return render(request,"designed_plan_cost.html",{"data":data})

def designed_plan_payment(request,id):
    data=tbl_design_plan.objects.get(id=id)
    return render(request,"designed_plan_payment.html",{"data":data})


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")



def services(request):
    return render(request,"services.html")


def user_view_suppliers(request):
    data=tbl_supplier_request.objects.filter(status="True")
    return render(request,"user_view_suppliers.html",{"data":data})


def user_view_materials(request,id):
    data=tbl_material.objects.filter(supplier=id)
    return render(request,"user_view_materials.html",{"data":data})


def view_material(request):
    supplier_id=request.session["supplier_id"]
    data=tbl_material.objects.filter(supplier_id=supplier_id)
    return render(request,"view_material.html",{"data":data})


def Send_Order(request,id):
    data=tbl_material.objects.get(id=id)

    return render(request,"send_order.html",{"data":data})

def save_order_request(request,id):
    if request.method=="POST":
        mat=tbl_material_orders()
        data=tbl_material.objects.get(id=id)
        mat.consumer_id=request.session["userid"]
        mat.supplier_id=data.supplier.id
        mat.material_id=id
        mat.customer_name=request.POST.get("name")
        mat.customer_email=request.POST.get("email")
        mat.customer_mobile=request.POST.get("mobile")
        mat.flat=request.POST.get("flat")
        mat.area=request.POST.get("area")
        mat.landmark=request.POST.get("landmark")
        mat.pincode=request.POST.get("pincode")
        mat.city=request.POST.get("city")
        mat.state=request.POST.get("state")
        mat.instructions=request.POST.get("instructions")
        q=request.POST.get("quantity")
        p=data.price
        tp=int(q) * int(p)
        mat.total_price=tp
        print(tp)
        mat.quantity=q
        mat.status="Order Requested"
        mat.save()
        return redirect("/user_dashboard/")


def my_orders(request):
    today=date.today()
    data=tbl_material_orders.objects.filter(consumer=request.session["userid"],status="Order Approved")
    return render(request,"my_orders.html",{"data":data,"today":today})


def my_rejected_orders(request):
    data = tbl_material_orders.objects.filter(consumer=request.session["userid"], status="Order Rejected")
    return render(request, "my_rejected_orders.html", {"data": data})

from datetime import date
def my_completed_orders(request):
    today=date.today()
    data = tbl_material_orders.objects.filter(consumer=request.session["userid"],status="Order Approved")
    return render(request, "my_completed_orders.html", {"data": data,"today":today})

def send_feedback(request,id):
    data=tbl_material_orders.objects.get(id=id)
    return render(request,"send_feedback.html",{"data": data})

def save_feedback(request,id):
    if request.method=="POST":
        data=tbl_material_orders.objects.get(id=id)
        data1=tbl_feedback()
        data1.order_id=id
        data1.user_id=request.session["userid"]
        data1.supplier_id=data.supplier.id
        data1.material_id=data.material.material
        data1.feedback=request.POST.get("feedback")
        data1.save()
        return redirect("/my_completed_orders/")

def user_view_feedback(request):
    data=tbl_feedback.objects.filter(user=request.session["userid"])
    return render(request,"user_view_feedback.html",{"data":data})

def supplier_requested_order(request):
    data=tbl_material_orders.objects.filter(supplier=request.session["supplier_id"],status="Order Requested")
    print(data)
    return render(request,"supplier_requested_order.html",{"data":data})

def supplier_approve_form(request,id):
    data=tbl_material_orders.objects.get(id=id)
    return render(request,"supplier_approve_form.html",{"data":data})

def save_approve_form(request,id):
    if request.method=="POST":
        data=tbl_material_orders.objects.get(id=id)
        data.delivery_date=request.POST.get("delivery_date")
        data.status="Order Approved"
        data.save()
        return redirect("/supplier_view_approved/")


def supplier_view_approved(request):
    data = tbl_material_orders.objects.filter(supplier=request.session["supplier_id"], status="Order Approved")
    return render(request, "supplier_view_approved.html", {"data": data})

def supplier_reject_form(request,id):
    data = tbl_material_orders.objects.get(id=id)
    return render(request, "supplier_reject_form.html", {"data": data})

def save_reject_form(request,id):
    if request.method=="POST":
        data=tbl_material_orders.objects.get(id=id)
        data.rejected_reason=request.POST.get("rejected_reason")
        data.status="Order Rejected"
        data.save()
        return redirect("/supplier_view_rejected/")

def supplier_view_rejected(request):
    data = tbl_material_orders.objects.filter(supplier=request.session["userid"], status="Order Rejected")
    return render(request, "supplier_view_rejected.html", {"data": data})

def supplier_view_feedback(request):
    data=tbl_feedback.objects.filter(supplier=request.session["supplier_id"])
    return render(request,"supplier_view_feedback.html",{"data":data})


def admin_view_orders(request):
    data=tbl_material_orders.objects.all()
    today=date.today()
    return render(request,"admin_view_orders.html",{"data":data,"today":today})


def admin_view_consumers(request):
    data=tbl_registration.objects.all()
    return render(request,"admin_view_consumers.html",{"data":data})

def admin_view_feedbacks(request):
    data=tbl_feedback.objects.all()
    return render(request,"admin_view_feedbacks.html",{"data":data})

def pay_online(request,id):
    data=tbl_material_orders.objects.get(id=id)
    return render(request,"pay_online.html",{"data":data})


def pay_online_status(request,id):
    data=tbl_material_orders.objects.get(id=id)
    data.payment_mode="Online Payment"
    data.save()
    messages.success(request,"Payment Completed Successfully")
    return redirect("/user_dashboard/")
def delete_request(request,id):
    a=tbl_supplier_request.objects.get(id=id)
    a.delete()
    return redirect("/view_supplier_request/")


