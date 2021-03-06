from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a feneric/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'unhandled Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent_succeeded
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)   

    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent_failed
        """
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200) 
