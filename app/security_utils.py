import re
import logging

class SecureLogger:

    def __init__(self,name):
        self.logger = logging.getLogger(name)

    def mask(self,message):

        patterns = [
            r'password',
            r'api_key',
            r'token',
            r'secret'
        ]

        for p in patterns:
            message = re.sub(
                p + r'.*',
                p + '=***MASKED***',
                message,
                flags=re.IGNORECASE
            )

        return message

    def info(self,message):

        safe_message=self.mask(message)
        self.logger.info(safe_message)


def mask_secret(secret):

    if len(secret)<=8:
        return "***MASKED***"

    return (
        secret[:4]
        +"*"*(len(secret)-8)
        +secret[-4:]
    )