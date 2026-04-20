# Github-Actions-CI-CD-pipeline

###### Implementing the CI/CD pipeline with Github Actions by replacing Jenkins on AWS 


#### Full Architecture 

<img width="1440" height="680" alt="image" src="https://github.com/user-attachments/assets/986981c8-89ca-41b2-926e-0cf2907d8886" />

---

Step: 1 Create the Flask app locally
___
Create project folder on your local machine

      cmd: mkdir github-actions-cicd
      
      cmd: cd github-actions-cicd
      
Create the app file app.py

      github-actions-cicd/app.py
      
Create requirements.txt

      github-actions-cicd/requirements.txt
      
Create a simple test file

      github-actions-cicd/test_app.py

Create Dockerfile

      github-actions-cicd/Dockerfile
      
Create .gitignore

      github-actions-cicd/.gitignore
      
Step: 2 Create GitHub repo and push code


Step: 3 Create AWS ECR repository

            AWS Console → Elastic Container Registry → Create repository
            
            Visibility:      Private
            
            Repository name: github-actions-cicd
            
            Click: Create repository

            Copy the repository URI — looks like:
            
            123456789.dkr.ecr.ap-south-1.amazonaws.com/github-actions-cicd

            

Step: 4 Create IAM user for GitHub Actions

GitHub Actions needs AWS credentials to push images to ECR and deploy to EC2

            AWS Console → IAM → Users → Create user
              Username: github-actions-user

            → Attach policies directly → attach these two:

            1. AmazonEC2ContainerRegistryFullAccess

            2. AmazonEC2FullAccess

            → Create user → Security credentials tab

            → Create access key → Application running outside AWS

            → COPY both values immediately:
            

Step: 5 Add secrets to GitHub repository

            GitHub repo → Settings → Secrets and variables → Actions

            → New repository secret — add all 4:

            AWS Access and Secret Key

            AWS Region and ECR_REPOSITORY

Step: 6

Step: 7

Step: 8

Step: 9

Step: 10

Step: 11
