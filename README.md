# DynamoDB tests

### Overview

* This repository contains my tests of Amazon DynamoDB in local environment - as demonstration of possibilities and code in python and go lang.
* Amazon DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS).
* It is a key-value and document-oriented database that provides fast and flexible storage and retrieval of data.
* All components run in docker, it is not necessary to install locally anything, even `aws` client.
* To use it you need only `docker` and `docker compose`
* All operations are included into `Makefile` and are invoked using `make` command

#### Environment

* DynamoDB and aws client images will be automatically downloaded when you start them for the first time.
* DynamoDB container runs in terminal interactive mode you can directly see logs and other output
* Also aws client container runs in terminal interactive mode so you can use command line commands.
* Necessary directories are checked and eventually created by Makefile itself.
* I recommend to download also DynamoDB noSQL workbench tool to interact with DynamoDB in container
  * This tool contains some example data models with data, you can import them using this tool into your local DynamoDB database.
* 


#### Read about DynamoDB

* [Downloadable version of Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker)
* [LinkedIn - setup a local DynamoDB and NoSQL Workbench](https://www.linkedin.com/pulse/setup-local-dynamodb-docker-nosql-workbench-corinne-roosen/?trk=public_profile_article_view)
* [Sample application on GitHub to test locally DynamoDB](https://github.com/aws-samples/aws-sam-java-rest)

#### Notes

* basic command to run dynamoDB locally in docker is
  ```
  docker run -p 8000:8000 amazon/dynamodb-local
  ```

#### Install

* [Docker compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)
* [NoSQL Workbench for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.install.html)
  * initial settings after installation:
    ```
    Setting NoSQLWorkbenchUser Credentials as:

    AWS profile : NoSQLWorkbenchUser
    Access key ID : AccessKeyID
    Secret access key : SecretAccessKey
    Default Region : us-east-2
    Output format : json
    ```
