from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import CustomUser,Saree
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import Group
import json
customer_group,created = Group.objects.get_or_create(name = 'customer')
wholesaler_group,created = Group.objects.get_or_create(name = 'wholesaler')

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user) 
            return redirect('wholesaler_dashboard')  
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login') 
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'password and confirm password must be same!')
            return redirect('register') 
        
        # Create the user
        user = CustomUser.objects.create_user(email=email, username=username, phone_no=phone_number, address=address, password=password)
        if role == 'wholesaler':
            user.groups.add(wholesaler_group)
        if role == 'customer':
            user.groups.add(customer_group)    
        user.save()
        messages.success(request,'Registration  Successful!')
        return redirect('login')  

    return render(request,'register.html')

def wholesaler(request):
    return render(request,'wholesaler.html')

def saree(request):
    if request.method == 'POST':
        saree_name = request.POST.get('sariname')
        sample_image = request.FILES.get('sample_image')
        design_no = request.POST.get('design_no')
        fieldIndex = request.POST.get('field_index')
        if fieldIndex == None:
            fieldIndex=1
        # Process dynamic material fields
        material_data = {}
        for i in range(1, int(fieldIndex)+1):  # Get values from all dynamic fields
            material_type = request.POST.get(f'field{i}_material_type')
            quantity = request.POST.get(f'field{i}_quantity')
            if material_type and quantity:
                material_data[material_type] = int(quantity)

        # Store image
        if sample_image:
            fs = FileSystemStorage()
            image_path = fs.save(sample_image.name, sample_image)

        # Create Saree object
        saree = Saree.objects.create(
            saree_name=saree_name,
            sample_image=image_path if sample_image else None,
            material=str(material_data),  # Store material as a JSON string
            design_no=design_no
        )
        saree.save()
      
        messages.success(request,"Saree Added Successfully.")
        return redirect('saree')  # Redirect to list view (replace with your view name)

    sarees = Saree.objects.all()
    return render(request, 'saree.html', {'sarees': sarees})    

def update_saree(request, saree_id):
    if request.method == 'POST':
        # Retrieve the saree object
        saree = Saree.objects.get(pk=saree_id)
        
        # Update saree data
        saree.saree_name = request.POST.get('sariname')
        sample_image = request.FILES.get('sample_image')
        if sample_image:
            fs = FileSystemStorage()
            image_path = fs.save(sample_image.name, sample_image)
            saree.sample_image = image_path
        saree.design_no = request.POST.get('design_no')
        
        # Process dynamic material fields
        material_data = {}
        for key in request.POST.keys():
            if key.startswith('field') and '_material_type' in key:
                field_index = key.split('_')[0][5:]
                material_type = request.POST.get(f'field{field_index}_material_type')
                quantity = request.POST.get(f'field{field_index}_quantity')
                if material_type and quantity:
                    material_data[material_type] = int(quantity)
        saree.material = str(material_data)

        saree.save()
      
        messages.success(request, "Saree Updated Successfully.")
        return redirect('saree')  # Redirect to list view (replace with your view name)
    else:
        saree = Saree.objects.get(pk=saree_id)
        return render(request, 'update_saree_modal.html', {'saree': saree})

def logout_view(request):
    logout(request)
    return redirect('login')