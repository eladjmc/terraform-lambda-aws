resource "aws_iam_role" "app_deploy_role" {
  name = var.deployRoleName
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_lambda_function" "app_lambda" {
  s3_key        = aws_s3_object.app_item.key
  s3_bucket     = aws_s3_bucket.app_storing_bucket.bucket
  role          = aws_iam_role.app_deploy_role.arn
  handler       = "${var.lambdaFileName}.${var.lambdaFileFunction}"
  runtime       = var.awsLambdaRuntime
  function_name = var.lambdaName
}


