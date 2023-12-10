wget -q https://raw.githubusercontent.com/aws-samples/eks-workshop-v2/stable/lab/cfn/eks-workshop-ide-cfn.yaml -O eks-workshop-ide-cfn.yaml


aws cloudformation deploy --stack-name eks-workshop-ide \
    --template-file ./eks-workshop-ide-cfn.yaml \
    --parameter-overrides RepositoryRef=stable \
    --capabilities CAPABILITY_NAMED_IAM


aws cloudformation describe-stacks --stack-name eks-workshop-ide \
    --query 'Stacks[0].Outputs[?OutputKey==`Cloud9Url`].OutputValue' --output text


aws sts get-caller-identity


export EKS_CLUSTER_NAME=eks-workshop

curl -fsSL https://raw.githubusercontent.com/aws-samples/eks-workshop-v2/stable/cluster/eksctl/cluster.yaml | \
envsubst | eksctl create cluster -f -

use-cluster $EKS_CLUSTER_NAME


prepare-environment introduction/getting-started


kubectl apply -k ~/environment/eks-workshop/base-application/catalog


# Delete environment
aws cloudformation delete-stack --stack-name eks-workshop-ide