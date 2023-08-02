
import builtins
import aws_cdk as cdk
from typing import List
from stacks.interfaces import INetworkConstruct
from constructs import Construct

from aws_cdk import(
  aws_iam as iam,
  aws_ec2 as ec2,
  aws_secretsmanager as sm,
  aws_redshiftserverless as rsl,
)

class RedshiftConstruct(Construct):
  def __init__(self, scope: Construct, id: builtins.str, network:INetworkConstruct) -> None:
    super().__init__(scope, id)

    self.default_iam_role = iam.Role(self,'DefaultRole',
      assumed_by= iam.ServicePrincipal(service='redshift'),
      description='Default role for Orion-On-AWS Redshift cluster',
      managed_policies=[
        iam.ManagedPolicy.from_aws_managed_policy_name('AmazonRedshiftAllCommandsFullAccess')
      ])

    # self.admin_password_secret = sm.Secret(self,'AdminPassword',
    #   description='Password for the Orion on AWS Redshift cluster',
    #   generate_secret_string= sm.SecretStringGenerator(
    #     password_length=32,
    #     exclude_punctuation=True,
    #     include_space=False,
    #     require_each_included_type=True
    #   ))

    self.namespace = rsl.CfnNamespace(self,'Namespace',
      namespace_name='orion-on-aws',
      admin_username='admin',
      db_name='dev',
      admin_user_password='K3lck3k5lcz1k2',
      default_iam_role_arn= self.default_iam_role.role_arn,
      iam_roles=[
        self.default_iam_role.role_arn
      ])

    self.security_group = ec2.SecurityGroup(self,'DefaultSecurityGroup',
      vpc = network.vpc,
      description='Default Security Group for '+ RedshiftConstruct.__name__)

     
    subnets_ids = network.vpc.select_subnets(subnet_group_name='Default').subnet_ids

    self.workgroup = rsl.CfnWorkgroup(self,'DefaultWorkgroup',
      workgroup_name='orion-on-aws-default',
      base_capacity=8,
      publicly_accessible=False,
      enhanced_vpc_routing=True,
      namespace_name=self.namespace.namespace_name,
      security_group_ids=[
        self.security_group.security_group_id
      ],
      subnet_ids=subnets_ids)

class AnalyticsConstruct(Construct):
  def __init__(self, scope: Construct, id: builtins.str, network:INetworkConstruct) -> None:
    super().__init__(scope, id)

    self.redshift_cluster = RedshiftConstruct(self,'Redshift', network=network)
    