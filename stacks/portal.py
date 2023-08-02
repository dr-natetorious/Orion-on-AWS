from os import path
import builtins
import aws_cdk as cdk
from typing import List
from stacks.interfaces import INetworkConstruct
from constructs import Construct

from aws_cdk import(
  aws_s3 as s3,
  aws_cloudfront as cf,
  aws_logs as logs,
  aws_cloudfront_origins as cfo,
  aws_s3_deployment as s3d,
)

WEBAPP_OUTDIR = path.join(path.dirname(__file__),'../src/webapp')

class FrontendConstruct(Construct):
  def __init__(self, scope: Construct, id: builtins.str, network:INetworkConstruct) -> None:
    super().__init__(scope, id)

    self.bucket = s3.Bucket(self,'AppStatic',
      auto_delete_objects=True,
      access_control= s3.BucketAccessControl.PRIVATE,
      removal_policy= cdk.RemovalPolicy.DESTROY)
      
    s3d.BucketDeployment(self,'Deployment',
      destination_bucket=self.bucket,
      log_retention= logs.RetentionDays.ONE_MONTH,
      sources=[
        s3d.Source.asset(WEBAPP_OUTDIR)
      ])

    # origin_identity = cf.OriginAccessIdentity(self,'OriginAccessIdentity',
    #   'Orion on AWS CloudFront Origin Identity')

    self.cloud_front = cf.Distribution(self,'Distribution',
      default_behavior= cf.BehaviorOptions(
        origin= cfo.S3Origin(self.bucket),
        compress=True))
    
class AdminPortalConstruct(Construct):
  def __init__(self, scope: Construct, id: builtins.str, network:INetworkConstruct) -> None:
    super().__init__(scope, id)

    self.front_end = FrontendConstruct(self,'Frontend', network=network)
    