CHATBOT_RULES = [
    {
        'keywords': ['no internet', 'not working', 'offline', 'no connection', 'internet down', 'cannot connect'],
        'category': 'No Internet Connection',
        'priority': 'High',
        'steps': [
            'Check whether the router power light is on.',
            'Check the fibre/LAN cable and make sure it is properly connected.',
            'Restart the router and wait for 2 to 3 minutes.',
            'Confirm that your internet bill is paid and active.',
        ],
        'response': 'This seems like a No Internet Connection issue.'
    },
    {
        'keywords': ['slow', 'speed', 'buffering', 'lag', 'loading', 'very slow'],
        'category': 'Slow Internet Speed',
        'priority': 'Medium',
        'steps': [
            'Restart your router before testing speed again.',
            'Move closer to the Wi-Fi router and test from one device.',
            'Disconnect extra devices that may be using bandwidth.',
            'Pause large downloads or streaming and test again.',
        ],
        'response': 'This seems like a Slow Internet Speed issue.'
    },
    {
        'keywords': ['router', 'red light', 'blinking', 'power light', 'wan light', 'wifi light'],
        'category': 'Router Problem',
        'priority': 'High',
        'steps': [
            'Check whether the router adapter is connected properly.',
            'Check whether the power, WLAN and WAN lights are stable.',
            'Restart the router once and wait for the lights to stabilise.',
            'If the red light continues, report it with a router photo or description.',
        ],
        'response': 'This seems like a Router Problem.'
    },
    {
        'keywords': ['disconnect', 'disconnecting', 'unstable', 'dropping', 'keeps dropping'],
        'category': 'Frequent Disconnection',
        'priority': 'High',
        'steps': [
            'Check whether the cable is loose or damaged.',
            'Keep the router in an open area away from heat.',
            'Check whether the issue happens on all devices or only one.',
            'Restart the router and record the time when disconnection happens.',
        ],
        'response': 'This seems like a Frequent Disconnection issue.'
    },
    {
        'keywords': ['bill', 'billing', 'payment', 'paid', 'recharge', 'blocked', 'invoice'],
        'category': 'Billing Issue',
        'priority': 'Medium',
        'steps': [
            'Check whether you used the correct customer ID while paying.',
            'Keep your payment receipt or transaction ID ready.',
            'Wait for the normal payment update time if you paid recently.',
            'Submit a billing complaint if the service is still blocked.',
        ],
        'response': 'This seems like a Billing Issue.'
    },
    {
        'keywords': ['installation', 'new connection', 'setup', 'install delay'],
        'category': 'Installation Delay',
        'priority': 'Medium',
        'steps': [
            'Confirm your installation appointment date and time.',
            'Make sure your phone number is reachable for the technician.',
            'Check whether required documents or payment are complete.',
            'Submit a complaint if the installation date has passed.',
        ],
        'response': 'This seems like an Installation Delay issue.'
    },
    {
        'keywords': ['upgrade', 'package', 'plan', 'speed package', 'new plan'],
        'category': 'Package Upgrade Issue',
        'priority': 'Medium',
        'steps': [
            'Check whether the package upgrade activation time has passed.',
            'Restart the router after package activation.',
            'Test speed using one nearby device.',
            'Submit a complaint if the upgraded speed is not active.',
        ],
        'response': 'This seems like a Package Upgrade Issue.'
    },
    {
        'keywords': ['technician', 'visit', 'not arrived', 'did not come', 'engineer'],
        'category': 'Technician Visit Delay',
        'priority': 'Medium',
        'steps': [
            'Confirm the promised visit date and time.',
            'Keep your complaint or account number ready.',
            'Check whether the ISP tried to contact you.',
            'Submit a technician delay complaint if the visit was missed.',
        ],
        'response': 'This seems like a Technician Visit Delay issue.'
    },
    {
        'keywords': ['staff', 'rude', 'support', 'no response', 'customer care', 'service center'],
        'category': 'Customer Support Issue',
        'priority': 'Low',
        'steps': [
            'Note the date and time of the support interaction.',
            'Mention the staff name if you know it.',
            'Explain the issue clearly and politely in the complaint form.',
        ],
        'response': 'This seems like a Customer Support Issue.'
    },
]


def get_chatbot_reply(message: str) -> dict:
    text = (message or '').lower().strip()

    if not text:
        return {
            'reply': 'Please type your internet issue, for example: “my internet is slow” or “my router light is red”.',
            'category': '',
            'priority': '',
            'steps': [],
        }

    if any(word in text for word in ['track', 'status', 'reference number', 'complaint number']):
        return {
            'reply': 'To track a complaint, open the Track Complaint page and enter your reference number, for example ISP-2026-AB12CD.',
            'category': 'Track Complaint',
            'priority': '',
            'steps': ['Keep your complaint reference number ready.', 'Enter it exactly as shown after submission.'],
        }

    if any(word in text for word in ['submit', 'complain', 'complaint form', 'raise complaint']):
        return {
            'reply': 'You can submit a complaint from the Submit Complaint page. Include your customer ID, address, issue category and a clear description.',
            'category': 'General Complaint Guidance',
            'priority': '',
            'steps': ['Open Submit Complaint.', 'Fill in required details.', 'Save the reference number after submission.'],
        }

    for rule in CHATBOT_RULES:
        if any(keyword in text for keyword in rule['keywords']):
            steps_text = ' '.join([f'{i+1}. {step}' for i, step in enumerate(rule['steps'])])
            reply = (
                f"{rule['response']} Try these minor checks first: {steps_text} "
                f"If the issue continues, submit a complaint under {rule['category']} with {rule['priority']} priority."
            )
            return {
                'reply': reply,
                'category': rule['category'],
                'priority': rule['priority'],
                'steps': rule['steps'],
            }

    return {
        'reply': 'I could not identify the exact issue. Please describe whether it is about no internet, slow speed, router, billing, installation, package upgrade, technician delay or customer support. You can also submit it under Other.',
        'category': 'Other',
        'priority': 'Medium',
        'steps': ['Describe the issue with clear details.', 'Mention your customer ID and area.', 'Submit a complaint under Other if no category fits.'],
    }
