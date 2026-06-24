booking_state = {
    "step": "start",
    "source": "",
    "destination": "",
    "date": ""
}

def get_response(message):
    msg = message.lower().strip()

    if booking_state["step"] == "start":
        if msg in ["hi", "hello", "hey"]:
            return "Welcome to SmartBus! Do you want to book a ticket? (yes/no)"

        elif msg == "yes":
            booking_state["step"] = "source"
            return "Please enter source city."

        elif msg == "no":
            return "Okay. Ask me anytime if you need help."

        else:
            return "Say hi to begin conversation."

    elif booking_state["step"] == "source":
        booking_state["source"] = message
        booking_state["step"] = "destination"
        return "Enter destination city."

    elif booking_state["step"] == "destination":
        booking_state["destination"] = message
        booking_state["step"] = "date"
        return "Enter travel date."

    elif booking_state["step"] == "date":
        booking_state["date"] = message

        source = booking_state["source"]
        destination = booking_state["destination"]
        date = booking_state["date"]

        booking_state["step"] = "start"

        return (
            f"Booking confirmed!\n"
            f"Route: {source} → {destination}\n"
            f"Date: {date}\n"
            f"Ticket Price: Rs.450"
        )
