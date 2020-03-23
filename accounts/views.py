from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import OrderForm
from .filters import OrderFilter



def home(request):
	customers = Customer.objects.all()
	total_customers = customers.count()

	orders = Order.objects.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	cuttingmaster = orders.filter(status='CuttingMaster').count()

	cuttingmasters = CuttingMaster.objects.all()
	print(cuttingmasters)

	context = {'orders': orders, 'customers': customers,
			   'total_orders': total_orders, 'delivered': delivered,
			   'pending': pending, 'cuttingmaster': cuttingmaster}

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	a =20
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products':products})



def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()



	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'accounts/customer.html',context)

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

def cuttingmaster(request, pk_cutting):
	cuttingmaster = CuttingMaster.objects.get(id=pk_cutting)

	context = {
		'cuttingmaster':cuttingmaster
	}
	return render(request, 'accounts/cuttingmaster.html', context)

def sewingmaster(request, pk_sewing):
	sewingmaster = SewingMaster.objects.get(id=pk_sewing)

	context = {
		'sewingmaster':sewingmaster
	}
	return render(request, 'accounts/sewingmaster.html', context)

def subemploy(request, pk_subem):
	subemploy = SubEmploy.objects.get(id=pk_subem)

	context = {
		'subemploy':subemploy
	}
	return render(request, 'accounts/subemploy.html', context)


def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
	customer = Customer.objects.get(id=pk)
	print(customer)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	print(Order.objects)
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

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)




