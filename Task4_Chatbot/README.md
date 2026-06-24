# Task 4: AI-Powered Chatbot for Bus Ticket Booking

## Project Overview
This project is an AI-powered chatbot developed using Python and Flask for a cloud internship task. The chatbot helps users interact with an online bus ticket booking system through a website interface.

The chatbot uses a retrieval-based conversational model with predefined patterns and multi-step conversation flow to simulate real customer support.

## Objective
- Design an AI-powered chatbot using Python
- Enable instant responses to website user queries
- Support commercial use cases such as ticket booking
- Improve customer interaction and reduce manual support workload
- Provide a scalable chatbot solution for online services

## Technologies Used
- Python 3
- Flask
- HTML
- CSS
- JavaScript
- VS Code

## Features
- Website-based chatbot interface
- Instant user query response
- Multi-step conversation support
- Bus ticket booking simulation
- Smart conversation memory
- Interactive chat UI
- Customer support automation

## Working
The chatbot follows a structured conversation flow:

1. Greets the user
2. Asks whether the user wants to book a ticket
3. Collects source city
4. Collects destination city
5. Collects travel date
6. Confirms booking with ticket details

### Example Conversation
User: Hi  
Bot: Welcome to SmartBus! Do you want to book a ticket?

User: Yes  
Bot: Please enter source city.

User: Chennai  
Bot: Enter destination city.

User: Salem  
Bot: Enter travel date.

User: 28 June  
Bot: Booking confirmed! Route: Chennai → Salem | Ticket Price: Rs.450

## Project Structure
```bash
Task4_Chatbot/
│
├── app.py
├── chatbot.py
├── templates/
│   └── index.html
└── README.md
```

## How to Run
1. Install Python
2. Install Flask

```bash
pip install flask
```

3. Run application

```bash
python app.py
```

4. Open browser and visit:

```text
http://127.0.0.1:5000
```

## Testing and Optimization
The chatbot was tested using multiple booking scenarios to ensure:
- Fast response time
- Correct conversation flow
- Accurate booking confirmation
- Improved user engagement

## Future Improvements
- Database integration
- Online payment support
- Real-time bus availability
- AI/NLP enhancement
- Cloud deployment

## Conclusion
This project demonstrates how AI-powered chatbots can improve customer support and automate ticket booking systems through a cloud-based web application.
