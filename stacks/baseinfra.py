import builtins
from typing import List
from constructs import Construct
from stacks.interfaces import INetworkConstruct

from aws_cdk import(
    aws_ec2 as ec2,
)

class NetworkConstruct(Construct, INetworkConstruct):
  
  @property
  def vpc(self)->ec2.IVpc:
    return self.__vpc

  @vpc.setter
  def vpc(self, value)->ec2.IVpc:
    self.__vpc =value

  @property
  def open_security_group(self)->ec2.ISecurityGroup:
    return self.__open_security_group

  @open_security_group.setter
  def open_security_group(self,value)->None:
    self.__open_security_group = value
  
  def __init__(self, scope: Construct, id: builtins.str) -> None:
    super().__init__(scope, id)
    self.gateways=dict()
    self.interfaces=dict()

    self.vpc = ec2.Vpc(self,'Vpc',
      ip_addresses= ec2.IpAddresses.cidr(cidr_block='10.0.0.0/16'),
      #availability_zones=['us-east-1a', 'us-east-1b', 'us-east-1c'],
      subnet_configuration=[        
        ec2.SubnetConfiguration(name='Public', subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24, map_public_ip_on_launch=True),        
        ec2.SubnetConfiguration(name='Default', subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
      ])

    self.open_security_group = ec2.SecurityGroup(self,'OpenSecurityGroup',
      vpc= self.vpc,
      allow_all_outbound=True,
      allow_all_ipv6_outbound=True,
      description='Default No SG')

    self.add_gateways()
    self.add_ssm_support()

  def add_gateways(self):
    for svc in ['s3', 'dynamodb']:
      self.gateways[svc] = ec2.GatewayVpcEndpoint(
        self, svc,
        vpc=self.vpc,
        service=ec2.GatewayVpcEndpointAwsService(
          name=svc))
    return self

  def add_rekognition_support(self):
    return self.add_interfaces(services=[
      'rekognition'
    ])

  def add_textract_support(self):
    return self.add_interfaces(services=[
      'textract'
    ])

  def add_kms_support(self):
    return self.add_interfaces(services=[
      'kms'
    ])

  def add_ssm_support(self):
    return self.add_interfaces(services=[
      'ssm', 'ec2messages', 'ec2','ssmmessages','logs'
    ])

  def add_lambda_support(self):
    return self.add_interfaces(services=[
      'elasticfilesystem', 'lambda', 'states',
      'ecr.api', 'ecr.dkr'
    ])

  def add_apigateway_support(self):
    return self.add_interfaces(services=[
      'execute-api'
    ])

  def add_storage_gateway(self):
    return self.add_interfaces(services=[
      'storagegateway'
    ])

  def add_everything(self):
    return self.add_interfaces(services=[
      'ssm', 'ec2messages', 'ec2',
      'ssmmessages', 'kms', 'elasticloadbalancing',
      'elasticfilesystem', 'lambda', 'states',
      'events', 'execute-api', 'kinesis-streams',
      'kinesis-firehose', 'logs', 'sns', 'sqs',
      'secretsmanager', 'config', 'ecr.api', 'ecr.dkr',
      'storagegateway'
    ])

  def add_interfaces(self, services:List[str]):
    for svc in services:
      if not svc in self.interfaces:
        self.interfaces[svc] = ec2.InterfaceVpcEndpoint(
          self, svc,
          vpc=self.vpc,
          service=ec2.InterfaceVpcEndpointAwsService(name=svc),
          open=True,
          private_dns_enabled=True,
          lookup_supported_azs=True,
          security_groups=[self.open_security_group])