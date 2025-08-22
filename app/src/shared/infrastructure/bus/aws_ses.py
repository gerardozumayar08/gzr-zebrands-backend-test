import boto3
from botocore.exceptions import BotoCoreError, ClientError

from app.src.shared.domain.bus.email import EmailSchema
from app.src.shared.settings import Settings


class SESNotifier:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = boto3.client("ses", region_name=self.settings.aws_region)

    def __call__(self, data_email: EmailSchema):
        try:
            # response = self.client.send_email(
            #     Source=data_email.sender,
            #     Destination={"ToAddresses": [data_email.destination]},
            #     Message={
            #         "Subject": {"Data": data_email.subject},
            #         "Body": {"Text": {"Data": data_email.message}},
            #     },
            # )
            # return response

            print("Envio de notificacion")
            print(data_email)

        except (BotoCoreError, ClientError) as e:
            raise ValueError(f"Error sending email via SES: {e}")
