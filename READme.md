# SmartFaces
<div style="display:flex">
<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" style="height:50px">
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/flutter.png?raw=true" alt="Flutter" style="height:50px; margin-left:12px">
</div>

---

## Backend
**Django, Django-Rest-Framework, SQL**

Built Restframework **API** to integrate easily with any other frontend Technologies

### Endpoints

Admin Dashboard `/admin` 

#### Accounts endpoint

- Signup
`POST accounts/signup/`
- Login and receive authorization Token
`POST acconts/login/`
- Logout
`POST accounts/logout/`
- User Details
`GET accounts/me/`
- Face Registration for new user
`POST accounts/facereg/`

#### Main Logic endpoints

- create Organization
`POST api/createorg/`
- get user created organization
  `GET api/myorgs/`
- get user joined organization
  `GET api/allmyorgs/`
- Teachers join organization
  `POST api/tjoin/[teacher-code]/`
- Student join organization
  `POST api/sjoin/[student-code]/`
- List classes
  `GET api/listclass/[org-code]/`
- Teachers create class
  `POST api/createclass/`
- Mark student attendance 
  `POST api/markpresent/`
- List present students in a class
  `GET api/classdetail/`
- Check if user has HOD permission
  `GET ishod/[org-code]`

---

## FrontEnd
**Flutter**

App is built using Flutter to support Android and iOS devices

### Screen Shots
<div style="display: flex; flex-wrap:wrap; justify-content: space-between">
<div>
<h5>Login</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/login.png?raw=true" alt="login" style="width:45%">
</div>
<div>
<h5>Signup</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/signup.png?raw=true" alt="login" style="width:45%">
</div>
<div>
<h5>Face Registration</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/FaceRegister.png?raw=true" alt="login" style="width:45%">
</div>
<div>
<h5>Mark present</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/marking-present.png?raw=true" alt="login" style="width:45%">
</div>
<div>
<h5>Current Ongoing classes</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/Current-ongoing-classes.png?raw=true" alt="login" style="width:45%">
</div>
<div>
<h5>Present Students View</h5>
<img src="https://github.com/teshank2137/smartAtendence/blob/master/media/present-students-teacher-view.png?raw=true" alt="login" style="width:45%">
</div>

</div>
