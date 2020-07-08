# Django Docker image extended with oracle database and restful API
`python/django`

## Build the docker imagecd
- stable
```
docker build --tag artifactory.renhsc.com:5000/bride/django-ddmi-libs:3.0.2 .
```
- try-out version
```
docker build --tag artifactory.renhsc.com:5000/bride/django-ddmi-libs:3.0.3 .
```

## Push the image to Artifactory
```
docker push artifactory.renhsc.com:5000/bride/django-ddmi-libs:3.0.2
```
```
docker push artifactory.renhsc.com:5000/bride/django-ddmi-libs:3.0.3
```


## Try out built docker image loally
```
docker run -p 5656:5656 -it <image_id> /bin/bash
```
Then under the root of docker container, run
``` 
python manage.py runserver 0.0.0.0:5656
```