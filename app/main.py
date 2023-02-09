def lambda_handler(event, context):
    body = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Elad's Lambda | Terraform</title>
                <style>
                    * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                    }
                    body {
                        height: 100vh;
                        width: 100%;
                        background-color: #b0b0f2;
                        display: flex;
                        flex-direction: column;
                        gap: 10px;
                        padding-top: 100px;
                        align-items: center;
            
                    }
                    h2 {
                        font-size: 3rem;
                        color: rgb(54, 53, 53);
                        background-color: rgba(0, 0, 255, 0.473);
                        width: 350px;
                        border-radius: 20px;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1>This lambda website was deployed by:</h1>
                <h2>Elad Harel</h2>
                <p>Using terraform to deploy the aws lambda and s3 bucket</p>
            </body>
            </html>
    '''
    return {
        'statusCode': 200,
        'body': body,
        'headers': {
            'Content-Type': 'text/html',
        }
    }