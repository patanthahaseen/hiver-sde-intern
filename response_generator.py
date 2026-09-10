# Response templates for each customer intent

responses = {
    "delivery_issue":
        "I'm sorry you're having trouble with your delivery. "
        "Please check your order tracking for the latest delivery update. "
        "If your package is marked as delivered but you haven't received it, "
        "please check around your delivery location and with household members or neighbors. "
        "If you still cannot find it, please contact Amazon customer support for further assistance.",

    "order_status":
        "I'd be happy to help you check your order status. "
        "Please check your Amazon order tracking for the latest information, "
        "including the current shipment status and expected delivery date.",

    "return_refund":
        "I'm sorry you're having an issue with your order. "
        "Please check your order details to see whether the item is eligible for a return or refund. "
        "If you've already returned the item, please check the refund status in your order details.",

    "payment_billing":
        "I'm sorry you're having an issue with your payment or billing. "
        "Please check your order and payment details to confirm the charge. "
        "If you believe you were charged incorrectly or more than once, "
        "please contact Amazon customer support so the charge can be investigated.",

    "account_login":
        "I'm sorry you're having trouble accessing your Amazon account. "
        "Please use the account recovery option to reset your password. "
        "If you still cannot access your account, please contact Amazon customer support for further assistance.",

    "prime_membership":
        "I'd be happy to help with your Amazon Prime membership. "
        "Please open your Prime membership settings to review, manage, or cancel your membership. "
        "You can also check your membership details and renewal information there.",

    "digital_content":
        "I'm sorry you're having trouble with your digital content. "
        "Please check your internet connection and make sure your Amazon app or device is updated. "
        "You can also try restarting the app or device. "
        "If the issue continues, please contact Amazon customer support for further assistance.",

    "product_issue":
        "I'm sorry you're having trouble with your product or device. "
        "Please check the product setup and troubleshooting instructions. "
        "If the issue continues, please contact Amazon customer support for further assistance."
}
def generate_response(intent):
    return responses.get(
        intent,
        "I'm sorry you're experiencing an issue. Please provide more details so we can help."
    )