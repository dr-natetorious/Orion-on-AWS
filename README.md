# Orion-on-AWS

CDK automation for setting up Orion Advisors analytics.

```sh
virtualenv .env
.env/scripts/activate.ps1
pip3 install -r requirements.txt
```

## How do I bootstrap my account

```sh
cdk bootstrap aws://$AWS_ACCOUNT_ID/$AWS_REGION
```

## How do I launch the deployer

```sh
docker-deploy/debug.bat
```

## How do I deploy everything

```sh
cdk deploy -a /files/app.py --require-approval never
```
