from flask import Flask, request, render_template
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import logging

app = Flask(__name__)

# Set up logging to log SMS details to a file
logging.basicConfig(filename='sms_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

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
        
        # Send the SMS using AWS SNS
        response = sns_client.publish(
            PhoneNumber=phone_number,
            Message=message,
            MessageAttributes=message_attributes
        )
        
        # Log the SMS details after successfully sending
        log_message = f"Phone: {phone_number}, Message: '{message}', Sender ID: {sender_id}"
        logging.info(log_message)

        return "SMS sent successfully!"
    
    except (NoCredentialsError, PartialCredentialsError):
        return "Error: AWS credentials are not properly configured."
    except Exception as e:
        logging.error(f"Failed to send SMS: {e}")
        return f"Error: {str(e)}"

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

