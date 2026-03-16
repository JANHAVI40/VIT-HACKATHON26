from plyer import notification

def send_alert(ip, stage):

    notification.notify(
        title="Security Alert",
        message=f"Attacker {ip} detected: {stage}",
        timeout=5
    )