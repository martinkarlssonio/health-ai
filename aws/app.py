#!/usr/bin/env python3
import cdk_nag
from aws_cdk import Aspects
import aws_cdk as cdk
from health_ai_cdk import HealthAiCdkStack

app = cdk.App()
aws_bedrock_langchain_stack = HealthAiCdkStack(app, "HealthAiCdk",)

Aspects.of(app).add(cdk_nag.AwsSolutionsChecks(reports=True, verbose=True))

app.synth()
