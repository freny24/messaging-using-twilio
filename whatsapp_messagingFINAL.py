from twilio.rest import Client

def msg_mom_and_dad(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'AC18170be6b5d1423ba76b17782df65645'
    auth_token = '38612c651444379e4c5275c625bd3b74'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Mom':'+917021440218'}


    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
                body = 'good morning {} !'.format(key),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' +917984433806,

            )

        print(msg_loved_ones.sid)