#!/usr/bin/env python3

import aws_cdk as cdk
from constructs import Construct
from stacks.baseinfra import NetworkConstruct
from stacks.analytics import AnalyticsConstruct
from stacks.portal import AdminPortalConstruct

class OrionOnAWSStack(cdk.Stack):
  def __init__(self, scope: Construct, id:str, **kwargs):
    super().__init__(scope,id, **kwargs)

    network = NetworkConstruct(self,'Networking')
    analytics = AnalyticsConstruct(self,'Analytics', network=network)
    portal = AdminPortalConstruct(self,'AdminPortal', network=network)

class OrionOnAWSApp(cdk.App):
  def __init__(self, **kwargs)->None:
    super().__init__(**kwargs)

    env = cdk.Environment(account='995765563608', region='us-west-2')
    OrionOnAWSStack(self,'Orion-on-AWS', env=env)

app = OrionOnAWSApp()
app.synth()
