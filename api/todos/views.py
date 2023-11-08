from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
from django.dispatch import Signal
from rest_framework import generics
from .models import Todo, Back
from .serializers import TodoSerializer, BackSerializer
from rest_framework import generics
from .models import Back
from .serializers import BackSerializer
from rest_framework.response import Response
from rest_framework import status
from .logic import stock, choose

# Create your views here.

# Initialize some lists and variables for storing filter data
filter = []
number = []
id = []

# Define a view for deleting data by its ID
class DeleteDataById(generics.GenericAPIView):
    #why the fuck do we have 2 delete functions ?? Like here and line 37
    def delete(self, request, pk):
        try:
            # Try to retrieve the item by its ID
            item = Back.objects.get(pk=pk)
            item.delete()
            return Response({'message': f'Data with ID {pk} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Back.DoesNotExist:
            return Response({'message': f'Data with ID {pk} not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'An error occurred while deleting data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Function to delete data by its ID 
def delete(todo_id):
    todelete = Todo.objects.get(pk=todo_id)
    todelete.delete()

# Define a custom signal
post_request_signal = Signal()

# Connect a signal handler (here POST) to the custom signal
def my_function(sender, request, **kwargs):


    # Retrieve the data
    ids = []  
    todos = Todo.objects.all()
    for todo in todos:
        ids.append(todo.pk)
        title = todo.title
        desc = todo.description
        print(desc)
        
        # Reset the description attribute to an empty string
        number.append(desc)
        filter.append(title)
        
        


    if len(ids) > 0:
        for todo_id in ids:
            delete(todo_id)
        print("Deleted")
    
    # Your logic here

    name, average = choose(filter, number)
    print (name)
    print (average)

    # POST the new numbers to get them back in the front end 
    print("POST request received")
    url = "http://localhost:8000/api/back/"
    data = {
        #stock is calculated in alphavantage_api and imported to get the values back 
        "number": average,
        "description": name
    }
    response = requests.post(url, data=data)
    number.clear()
    filter.clear()

    if response.status_code == 200:
        # POST request succeeded
        print("POST request successful")
        print("Response:", response.json())
        
    else:
        # POST request failed
        print("POST request failed")
        print("Status code:", response.status_code)

# When a post request is signaled, it executes my_function
post_request_signal.connect(my_function)

# Define a view for listing and creating Todo objects
class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def refresh_data(self):
        self.queryset = Todo.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        # Send the post_request_signal after creating a new object
        post_request_signal.send(sender=None, request=self.request)

# Class that renders at /api/Id to see a specific element
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Can't remember why it's here exactly
def my_view(request):
    if request.method == 'POST':
        # Allows deleting any other post that did not get deleted
        post_request_signal.send(sender=None, request=request)
    else:
        # Handle other HTTP methods (GET, PUT, etc.)
        return HttpResponse("Only POST requests allowed")

# Send back the data
class DataBack(generics.ListCreateAPIView):
    queryset = Back.objects.all()
    serializer_class = BackSerializer
