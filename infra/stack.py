from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    CfnOutput,
    RemovalPolicy,
)
from constructs import Construct


class SudokuStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, "SudokuBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        distribution = cloudfront.Distribution(
            self, "SudokuDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="sudoku.html",
        )

        s3deploy.BucketDeployment(
            self, "DeploySite",
            sources=[s3deploy.Source.asset("../", exclude=["infra/*", "README.md"])],
            destination_bucket=bucket,
            distribution=distribution,
        )

        CfnOutput(self, "URL", value=f"https://{distribution.distribution_domain_name}")
