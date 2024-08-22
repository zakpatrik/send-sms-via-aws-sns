from flask import Flask, request, render_template
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

app = Flask(__name__)

def send_sms(phone_number, message, sender_id, origination_number=None):
    try:
        sns_client = boto3.client("sns")
        
        message_attributes = {
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': sender_id
            }
        }

        if origination_number:
            message_attributes['AWS.MM.SMS.OriginationNumber'] = {
                'DataType': 'String',
                'StringValue': origination_number
            }
        
        response = sns_client.publish(
            PhoneNumber=phone_number,
            Message=message,
            MessageAttributes=message_attributes
        )
        
        return "SMS sent successfully!"
    except (NoCredentialsError, PartialCredentialsError):
        return "Error: AWS credentials are not properly configured."
    except Exception as e:
        return f"Something went wrong: {str(e)}"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send_sms", methods=["POST"])
def send_sms_route():
    phone_number = request.form["phone_number"]
    message = request.form["message"]
    sender_id = request.form["sender_id"]
    origination_number = request.form.get("origination_number")

    result = send_sms(phone_number, message, sender_id, origination_number)
    return result

if __name__ == "__main__":
    app.run(debug=True)
