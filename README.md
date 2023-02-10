# Terraform Deploy S3+Lambda on AWS with Jenkins 
<img src="./assets/images/title.jpg" width="700" height="400" />


In this project I used Terraform to deploy lambda+s3 bucket in AWS while using jenkins for the CI/CD

## Prerequisites
* Account in AWS
* Jenkins with terraform version 1.3.7+ installed on it and access to github account with the project files and 
* Terraform 'tfvars' file that contains all the variables needed for the setup(access key and secret key)
* Big cup of coffee 😉☕

## Jenkins:
1. Log in to your Jenkins server
2. Connect your Jenkins to your Github account using a private key(Github should have the public key) - This step can be skipped if the repo is public
3. Create a new Jenkins Pipeline linked to your GitHub repository

