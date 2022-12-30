### Create a project
```
django-admin startproject studybud
```


### Create a app
```
python manage.py startapp base
```

Add the `base.apps.BaseConfig` to the `INSTALLED_APPS` in **settings.py**

### Templates
- Create a **template** folder to the root directory
- Modify the `TEMPLATES` session in the **settings.py**
``` (settings.py)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Note: we add `BASE_DIR / 'templates'` inside the `'DIRS'` list.

- To include a `html` page to another one: e.g. to include the **navbar.html** inside the **homepage.html**
``` (homepage.html)
{% include 'navbar.html' %}

<h1>Home Template</h1>
```

- Parent-Child templates
  - Add the following code to the **parent** template:
  ```
  {% block content %}

  {% endblock %}
  ```

  - Add `{% extends '<parent>.html' %}` on the top of the **child** template, and wrap the child content inside:
  ```
  {% block content %}
  <!-- all child template content -->
  {% endblock content %}
  ```

### Passing variables
[Templates | Django](https://docs.djangoproject.com/en/3.2/topics/templates/)

### Models
- Everytime creates a model, run:
  ```
  # To create the table
  python manage.py makemigrations

  # To migrate changes
  python manage.py migrate
  ```
- `Models` by default, has an ID generator, starts at 1 and increments in the database as the instance goes on.
  - can be overwritten


### Database & Admin Panel
#### Create a superuser
```
python manage.py createsuperuser
admin
cGFzc3dvcmQ=
```

#### Use the Admin Panel
- In **admin.py**, add:
```
from . import <model_name>

admin.site.register(<model_name>)
```

- Model manager
``` (see pic: Querysets List)
<model_name>.objects.all()
<model_name>.objects.get()
```

- OneToMany relationship

- **User**
[default user model](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/)
user1: dXNlcjE=


## CRUD

- Create a form template and put the following inside the content block
```
<div>
  <form method="POST" action="" >
    {% csrf_token %}

    <input type="submit" value="Submit">
  </form>
</div>>
```
  - `action`: if not specified, it will send back to the same url.

### ModelForm
A classed based model form.

- Create a ModelForm in **forms.py** from the model (Meta)
- Import the Model to the **views.py**

#### Ordering in the database
- Add `ordering`
  - Could add directly to the `Model`
  ```
  # Descending order: the newest one will be the last
  class Meta:
    ordering = ['updated', 'created']
  ```

  ```
  # Descending order: the newest one will be the last
  class Meta:
    ordering = ['-updated', '-created']
  ```

#### Back to the previous page
In the tempalte: 
``` delete.html
<a href="{{request.META.HTTP_REFERER}}">Go Back</a>
```

### Search 

#### Search by different attributes
- Add `from django.db.models import Q` to the **views.py**
- e.g.
  ```
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  rooms = Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) | 
    Q(description__icontains=q)
    ) 
  # '__name': the double underscore is to the attribute of the parent
  # '__icontains': this makes if there isn't any room related with this topic, rooms will be all instance
    # 'i' is to make case insensitve, other options like start with, end with, etc
  # 'Q' makes it possible to search by different values
  ```
#### Count

### Authentication
- User login form
- User registration
- logout functionality

#### Django Default User Authentication
**By default**, Django has by session based authentication.
#### How it works? 

In the admin panel (http://127.0.0.1:8000/admin/), in the backend, there is a database table called **Session**, (in the INSTALLED_APPS in **settings.py**, we have `'django.contrib.sessions'`). When the user logged in, the session token be created, and it stores the information about the user. So once the user is authenticated, we know who this user is, all the information about him.

Go to the browser **inspect elemment**, under **Application* -> Storage  -> Cookies*. When the session has be created, it stores in the browser. As we nevigate through pages in our website, we don't have to login, that session has been stored. On each request, it will be sent to the backend, and check if this user is someone allow to be here, if is authenticated, and what are the permissions do they have, etc.


#### Build Customized User Authentication
- Create **login_retister.html**, add the following inside the block content
  - Django has built-in login form and built-in registration form, we want to build our own.
  ```
  {% block content %}
  <div>
    <form method="POST" action="">
      {% csrf_token %}

      <label>Username:</label>
      <input type="text" name="username" placeholder="Enter Username" />

      <label>Password:</label>
      <input type="password" name="password" placeholder="Enter Password" />

      <input type="submit" name="login" />
    </form>
  </div>
  {% endblock content %}
  ```
- Create a view function
  - _Note: don't call it **login** since there is a built-in function with the same name._
  - steps:
    - 1. check if the user exist
    - 2. if exist, check if authenticate, return the user object
    - 3. if authenticate, redirect the user
    - 4. 
  - (step 1) need to import `from django.contrib.auth.models import User`
  - Use [Django flash messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/#using-messages-in-views-and-templates)
    - these messages will be stored in the session, only one browser refresh.
    - syntax in **views.py**:
    ```
    from django.contrib import messages
    messages.add_message(request, messages.INFO, 'Hello world.')
    ```
    - in template **main.html** before block content (which means if there is any flash messages, it will appear here)
    ```
    {% if messages %}
    <ul class="messages">
        {% for message in messages %}
        <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    ```
    - (step 2-4) import `from django.contrib.auth import authenticate, login, logout` in **views.py**
    
#### Restricted Pages
Restrict users based on their status.
There are many ways to do this, we will use a simple decorator to do this here.

- Add a decorator above a view we want to restrict. import `from django.contrib.auth.decorators import login_required`, we want to restrict the 'createRoom' here.
```
# redirect the user to the 'login' page if user doesn't authenticated or hasn't login
@login_required(login_url='login')
def createRoom(request):
```
- Restrict `updateRoom` view by checking if the user is the room host in **views.py**:
```
@login_required(login_url='login')
def updateRoom(request, pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room) # pass in the instance value
  
  if request.user != room.host:
    return HttpResponse('You are not allow to update this room.')
  
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save() # if valid, save the model into database
      return redirect('home')
    
  context = {'form': form}
  return render(request, 'base/room_form.html', context)
```


### User Registration
- import `from django.contrib.auth.forms import UserCreationForm` 


############## 3:01:37









### Customizing User Model
Create a `Profile` model, oneToOne relationship with the built-in `User` model.

- In **models.py**, import `from django.contrib.auth.models import User, AbstractUser` and create a `User` class:
```
class User(AbstractUser):
  pass
```

- In **settings.py**, add the following, which tells Django to use our `User`:
```
Auth_User_MODEL = 'base.User'
```




