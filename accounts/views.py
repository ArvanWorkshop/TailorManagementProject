from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


################################## User Authintication ###############################

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form': form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

################################## Admin Dashboard ###############################

@login_required(login_url='login')
@admin_only
def home(request):
	customers = Customer.objects.all()
	total_customers = customers.count()
	orders = Order.objects.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	complete = orders.filter(status='Complete Order').count()
	pending = orders.filter(status='Pending').count()
	cuttingmaster = orders.filter(status='CuttingMaster').count()
	sewingmaster = orders.filter(status='SewingMaster').count()

	processing = pending + cuttingmaster + sewingmaster
	cuttingmasters = CuttingMaster.objects.all()

	context = {
		'orders': orders, 'customers': customers,
		'total_orders': total_orders, 'delivered': delivered,
		'pending': pending, 'cuttingmaster': cuttingmaster,
		'processing': processing, 'complete':complete
		}
	return render(request, 'accounts/dashboard.html', context)


def customers(request):
	customers = Customer.objects.all()
	total_customers = customers.count()

	context = {
		'customers': customers,
		'total_customers': total_customers,
	}
	return render(request, 'accounts/customers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)


	orders = customer.order_set.all()
	order_count = orders.count()



	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

def createCustomer(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('home')

	context = {'form': form}
	return render(request, 'accounts/create_customer.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employs(request):
	cuttingmasters = CuttingMaster.objects.all()
	sewingmasters = SewingMaster.objects.all()
	subemploys = SubEmploy.objects.all()

	total_cuttingmaster = cuttingmasters.count()
	total_sewingmaster = sewingmasters.count()
	total_subemploy = subemploys.count()
	context = {
		'cuttingmasters': cuttingmasters,
		'sewingmasters' : sewingmasters,
		'subemploys' : subemploys,
		'total_cuttingmaster': total_cuttingmaster,
		'total_sewingmaster': total_sewingmaster,
		'total_subemploy': total_subemploy
	}
	return render(request, 'accounts/employs.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCuttingmaster(request):
	form = CuttingMasterForm()
	if request.method == "POST":
		form = CuttingMasterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('employs')
	context = {
		'form':form
	}
	return render(request, 'accounts/CuttingMaster/createcuttingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def cuttingmaster(request, pk_cutting):
	cuttingmaster = CuttingMaster.objects.get(id=pk_cutting)
	form = CuttingMasterForm(instance=cuttingmaster)

	if request.method == "POST":
		form = CuttingMasterForm(request.POST, request.FILES, instance=cuttingmaster)
		if form.is_valid():
			form.save()

	context = {
		'cuttingmaster':cuttingmaster,
		'form': form
	}
	return render(request, 'accounts/CuttingMaster/cuttingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteCuttingmaster(request, pk_cutting):
	cuttingmaster = CuttingMaster.objects.get(id=pk_cutting)
	if request.method == "POST":
		cuttingmaster.delete()
		return redirect('employs')

	context = {'item':cuttingmaster}
	return render(request, 'accounts/CuttingMaster/delete_cuttingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createSewingmaster(request):
	form = SewingMasterForm()
	if request.method == "POST":
		form = SewingMasterForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('employs')
	context = {
		'form':form
	}
	return render(request, 'accounts/SewingMaster/create_sewingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def sewingmaster(request, pk_sewing):
	sewingmaster = SewingMaster.objects.get(id=pk_sewing)
	form = SewingMasterForm(instance=sewingmaster)

	if request.method == "POST":
		form = SewingMasterForm(request.POST, request.FILES, instance=sewingmaster)
		if form.is_valid():
			form.save()

	context = {
		'sewingmaster':sewingmaster,
		'form': form,
	}
	return render(request, 'accounts/SewingMaster/sewingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteSewingmaster(request, pk_sewing):
	sewingmaster = SewingMaster.objects.get(id=pk_sewing)
	if request.method == "POST":
		sewingmaster.delete()
		return redirect('employs')

	context = {'item':sewingmaster}
	return render(request, 'accounts/SewingMaster/delete_sewingmaster.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createSubemploy(request):
	form = SubEmpolyForm()
	if request.method == "POST":
		form = SubEmpolyForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('employs')
	context = {
		'form':form
	}
	return render(request, 'accounts/SubEmploys/create_subemploy.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def subemploy(request, pk_subem):
	subemploy = SubEmploy.objects.get(id=pk_subem)
	form = SubEmpolyForm(instance=subemploy)

	if request.method == "POST":
		form = SubEmpolyForm(request.POST, request.FILES, instance=subemploy)
		if form.is_valid():
			form.save()


	context = {
		'subemploy':subemploy,
		'form': form,
	}
	return render(request, 'accounts/SubEmploys/subemploy.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteSubemploy(request, pk_subem):
	subemploy = SubEmploy.objects.get(id=pk_subem)
	if request.method == "POST":
		subemploy.delete()
		return redirect('employs')

	context = {'item':subemploy}
	return render(request, 'accounts/SubEmploys/delete_subemploy.html', context)




################################## Customer user Pages ###############################

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()

	total_orders = orders.count()
	complete = orders.filter(status='Complete Order').count()
	pending = orders.filter(status='Pending').count()
	cuttingmaster = orders.filter(status='CuttingMaster').count()
	sewingmaster = orders.filter(status='SewingMaster').count()

	processing = pending + cuttingmaster + sewingmaster

	print('ORDERS:', orders)

	context = {'orders':orders, 'total_orders':total_orders,
	'complete':complete,'processing':processing}
	return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()

	context = {
		'form':form,
		'customer':customer
	}
	return render(request, 'accounts/account_settings.html', context)


################################## Product ###############################

def createProduct(request):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('products')
	context = {
		'form':form
	}

	return render(request, 'accounts/Products/create_Product.html', context)


@login_required(login_url='login')
def viewProduct(request, pk):
	product = Product.objects.get(id=pk)
	context = {
		'product':product,
	}
	return render(request, 'accounts/Products/view_product.html', context)


@login_required(login_url='login')
def updateProduct(request, pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)

	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			form.save()

	context = {
		'product':product,
		'form': form
	}
	return render(request, 'accounts/Products/update_product.html', context)

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	context = {
		'products': products,
	}

	return render(request, 'accounts/Products/products.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteProduct(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == "POST":
		product.delete()
		return redirect('products')

	context = {'item':product}
	return render(request, 'accounts/Products/delete_product.html', context)


################################## Order Product ###############################


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status',), extra=10)
	customer = Customer.objects.get(id=pk)

	print(customer)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#print(Order.objects)

	#orders = Order.objects.all()
	#cuttingmaster = orders.filter(status='CuttingMaster')

	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			a = Order.objects.last()
			#b = a.filter(status="CuttingMaster")
			print(a)

			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def viewOrder(request, pk):
	order = Order.objects.get(id=pk)
	context ={'item': order}
	return render(request, 'accounts/order_view.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)




