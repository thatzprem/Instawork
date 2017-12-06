# Instawork
A ​team-member ​management application.

The project configured to user MySQL DB

You may run the requirements.txt file or refer the same for the additional packages to be installed.

The API documentation for the app is available on this postman URL
https://documenter.getpostman.com/view/43395/instawork/7EK6BdW

Create Member:
curl --request GET \
  --url http://127.0.0.1:8000/team/member
  
Update Member:
curl --request PATCH \
  --url http://127.0.0.1:8000/team/member/2/ \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form first_name=New
  
Get Members:
curl --request GET \
  --url http://127.0.0.1:8000/team/member
  
Delete Member:
curl --request DELETE \
  --url http://127.0.0.1:8000/team/member/1 \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --form first_name=New  
