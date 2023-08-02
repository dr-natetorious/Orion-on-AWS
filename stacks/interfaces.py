from aws_cdk import(
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_dynamodb as ddb,
)

class INetworkConstruct:
    @property
    def vpc(self)->ec2.IVpc:
        raise NotImplementedError()
