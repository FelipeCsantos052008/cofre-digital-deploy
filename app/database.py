from security_utils import (
    SecureLogger,
    mask_secret
)

secure_logger = SecureLogger(__name__)

def connect_database(
    host,
    user,
    password,
    database
):

    secure_logger.info(
        f"Conectando em {host}"
    )

    connection = (
        f"postgres://{user}:"
        f"{mask_secret(password)}"
        f"@{host}/{database}"
    )

    secure_logger.info(connection)

    return {
        "status":"connected"
    }