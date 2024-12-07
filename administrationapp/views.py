from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def projecthomepage2(request):
    return render(request, 'administrationapp/ProjectHomePage.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'administrationapp/UserRegisterPage.html')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Staff  # Import the Staff model

def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password']

        # Check if passwords match
        if pass1 == pass2:
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'administrationapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'administrationapp/UserRegisterPage.html')
            else:
                # Create the user account
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    email=email
                )
                user.save()

                # If the username length is 4, save to Staff model
                if len(username) == 4:
                    Staff.objects.create(username=username, email=email)

                messages.info(request, 'Account created successfully!')
                return render(request, 'administrationapp/ProjectHomePage.html')
 # Redirect after registration
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'administrationapp/UserRegisterPage.html')
    else:
        return render(request, 'administrationapp/UserRegisterPage.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def UserLoginPageCall(request):
    return render(request, 'administrationapp/UserLoginPage.html')

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Staff

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            # Check the length of the username
            if len(username) > 4:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as Patient!')
                return redirect('patientapp:PatientHomePage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as Staff!')
                return redirect('staffapp:StaffHomePage')  # Replace with your faculty homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'administrationapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'administrationapp/UserLoginPage.html')
    else:
        return render(request, 'administrationapp/UserLoginPage.html')



def logout(request):
    auth.logout(request)
    return redirect('projecthomepage2')

from .forms import PatientsForm
from .models import PatientList

def add_patient(request):
    if request.method == 'POST':
        form = PatientsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientsForm()
    return render(request, 'patientapp/add_patient.html',{'form':form})
def patient_list(request):
    patients = PatientList.objects.all()
    return render(request, 'staffapp/Patient_List.html', {'patients': patients})

from django.shortcuts import render
from .models import PatientList
import datetime
def patient_list2(request):
    today = datetime.date.today()  # Get today's date
    patients = PatientList.objects.filter(Date=today)  # Filter patients with today's date
    return render(request, 'staffapp/appointment.html', {'patients': patients})


from django.shortcuts import render, get_object_or_404, redirect
from .models import PatientList  # Your model name


def delete_patient(request, id):
    patient = get_object_or_404(PatientList, id=id)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')  # Redirect to the list view after deletion

    return render(request, 'staffapp/confirm_delete.html', {'patient': patient})

def appointment(request):
    patients = PatientList.objects.all()
    return render(request, 'staffapp/Patient_List.html', {'patients': patients})

def FAQs(request):
    return render(request,'administrationapp/FAQ.html')

#def medicine(request):
    #return render(request,'administrationapp/medicine.html')

def doctor(request):
    return render(request,'administrationapp/doctor.html')




from django.shortcuts import render
from django.contrib import messages

def medicine(request):
    if request.method == 'POST':
        # Retrieve the medicine name and quantity from the form
        medicine_name = request.POST.get('medicine')
        quantity = 0

        # Retrieve the quantity for the selected medicine
        if medicine_name == 'Paracetamol':
            quantity = int(request.POST.get('quantity_Paracetamol', 1))
        elif medicine_name == 'Ibuprofen':
            quantity = int(request.POST.get('quantity_Ibuprofen', 1))
        elif medicine_name == 'Amoxicillin':
            quantity = int(request.POST.get('quantity_Amoxicillin', 1))

        if medicine_name and quantity > 0:
            # Add success message
            messages.success(request, f'{quantity} units of {medicine_name} booked successfully!')

    return render(request, 'administrationapp/medicine.html')

def medicine_avail(request):
    return render(request,'administrationapp/avail_medicines.html')


from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Staff  # Import Staff model

def book_appointment(request):
    if request.method == 'POST':
        staff_username = request.POST['staff_username']
        patient_name = request.POST['patient_name']
        appointment_date = request.POST['appointment_date']

        try:
            # Get staff member from the database
            staff = Staff.objects.get(username=staff_username)

            # Send Email to the staff member
            send_mail(
                'New Appointment Request',
                f'You have a new appointment request from {patient_name} on {appointment_date}.',
                settings.DEFAULT_FROM_EMAIL,  # Ensure you have this in your settings
                [staff.email],
            )

            # Show success message
            messages.success(request, 'Appointment request sent successfully!')

            # Redirect to the same page after submission
            return redirect('book_appointment')

        except Staff.DoesNotExist:
            # If the staff member does not exist, show an error message
            messages.error(request, 'Staff member not found. Please try again.')
            return redirect('book_appointment')

    # Fetch all staff members for the dropdown list
    staff_members = Staff.objects.all()
    return render(request, 'administrationapp/book_appointment.html', {'staff_members': staff_members})


from django.shortcuts import render


import re

def get_response(user_input):
    # List of responses
    responses = {
        'hello': "Hi! How can I assist you today?",
        'lose weight': "To lose weight, focus on creating a calorie deficit through a combination of diet and exercise. Aim for gradual weight loss, and consult with a healthcare professional before starting a weight loss plan.",
        'paracetamol benefits': "Paracetamol is commonly used to relieve pain and reduce fever. It's effective for mild to moderate pain, like headaches or muscle aches.",
        'stress management': "To manage stress, try mindfulness techniques, regular exercise, relaxation exercises, and getting enough sleep. It also helps to talk to someone about your feelings.",
        'healthy diet': "A healthy diet includes a variety of fruits and vegetables, whole grains, lean proteins, and healthy fats. Avoid processed foods and limit sugar intake.",
        'mental health': "Mental health refers to your emotional, psychological, and social well-being. It impacts how you think, feel, and act. Practicing self-care and seeking support when needed is essential.",
        'diabetes symptoms': "Common symptoms of diabetes include frequent urination, increased thirst, fatigue, unexplained weight loss, and blurry vision. If you notice these symptoms, it's important to visit a healthcare provider for testing.",
        'heart disease prevention': "Prevent heart disease by eating a balanced diet, exercising regularly, quitting smoking, limiting alcohol, and managing stress.",
        'sleep improvement': "To improve your sleep quality, establish a regular bedtime routine, create a dark and cool sleep environment, and limit caffeine and screen time before bed.",
        'cholesterol': "Cholesterol is a fatty substance in your blood. While your body needs some cholesterol to function, too much can increase your risk of heart disease.",
        'hydration': "Aim to drink around 2 liters (8 cups) of water a day, but this may vary depending on your activity level and environment."
    }

    # Preprocess user input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Check if any keyword matches the user input using regex
    for key, response in responses.items():
        if re.search(key, user_input):
            return response

    return "Sorry, I couldn't understand that. Please try again."



# Chatbot view to handle user input
def chatbot_view(request):
    bot_response = ''
    user_input = ''

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input:
            bot_response = get_response(user_input)
        else:
            bot_response = "Please type a message."

    return render(request, 'administrationapp/chat.html', {'bot_response': bot_response, 'user_input': user_input})
