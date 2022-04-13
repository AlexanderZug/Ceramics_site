import app
from flask_mail import Message
from dataclasses import dataclass
from typing import ClassVar

from person_data import TRY_EMAIL


@dataclass
class Mail:
    """Class for sending email."""

    name: str
    email: str
    message: str
    MSG: ClassVar[Message]

    def send_message(self) -> None:
        """Sending a message."""
        self.MSG = Message("Message from site", recipients=[TRY_EMAIL])
        self.MSG.body = (f"You got a new message from {self.name}, "
                         f"e-mail: {self.email} "
                         f", message text: {self.message}")
        app.mail.send(self.MSG)