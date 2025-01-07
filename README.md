# python-web-calculator
Simple Python calculator app for deploy and test with infra

1. Create a dockerfile


2. Build an image
`docker build -t python-project .`

3. Run the image
`docker run -p 9000:8080 python-project`

4. Tag the image
`docker tag python-project username/repo-name:tagname`

5. Upload the image to Dockerhub
`docker push username/repo-name:tagname`