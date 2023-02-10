# Terraform Deploy S3+Lambda on AWS with Jenkins 
<img src="./assets/images/title.jpg" width="900" height="400" />


In this project I used Terraform to deploy lambda+s3 bucket in AWS while using jenkins for the CI/CD

## Prerequisites
* Account in AWS
* Jenkins with terraform version 1.3.7+ installed on it and access to github account with the project files and 
* Terraform 'tfvars' file that contains all the variables needed for the setup(access key and secret key)
* Big cup of coffee 😉☕

## Jenkins:
1. Log in to your Jenkins server
2. Connect your Jenkins to your Github account using a private key(Github should have the public key) - This step can be skipped if the repo is public - [How to connect Github to Jenkins video](https://www.google.com/search?q=add+github+repository+to+jenkins&rlz=1C1TIGY_enIL721IL721&sxsrf=AJOqlzUv2b5Ha8EGuOo412ZIrwy0G9fe_Q:1675952999207&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiy9LW504j9AhXJcKQEHXSAB5wQ_AUoAXoECAIQAw&biw=1536&bih=722&dpr=1.25#fpstate=ive&vld=cid:2b5124f4,vid:jSm0YZ-NQAc)
3. Create a new Jenkins Pipeline linked to your GitHub repository

