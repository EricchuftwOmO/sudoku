# Infrastructure

AWS CDK (Python) stack that deploys the Sudoku game to AWS.

## Architecture

- **Amazon S3** — Private bucket hosting the static files
- **Amazon CloudFront** — CDN distribution with Origin Access Control (OAC) serving content over HTTPS

## Prerequisites

- Python 3.12+
- AWS CDK CLI (`npm install -g aws-cdk`)
- AWS credentials configured (`aws configure`)

## Setup

```bash
cd infra
pip install -r requirements.txt
```

## Deploy

```bash
cdk bootstrap   # first time only
cdk deploy
```

The output will print the CloudFront URL where the app is accessible.

## Destroy

```bash
cdk destroy
```

This removes all resources including the S3 bucket and its contents.
