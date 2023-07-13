# BespokeBots

BespokeBots is a Python-based project that integrates various services (such as Slack, Google Calendar, and Todoist) to assist users in their day-to-day tasks, providing an automated personalized concierge. The platform uses OpenAI's GPT-4 model to understand and respond to user requests in a human-like manner. The project is designed with a plugin-based architecture, allowing easy addition of new integrations as needed.

## Getting Started

### Prerequisites

The following tools are required to run this project:

- Docker
- Python 3.11
- Postman (for API testing)

### Environment Variables

You'll need to set several environment variables to run the project, including:

- OPENAI_API_KEY
- BESPOKE_BOTS_SLACK_BOT_TOKEN
- BESPOKE_BOTS_SLACK_SIGNING_SECRET
- SERPAPI_API_KEY
- TODOIST_API_KEY

### Building and Running the Project

1. Clone the repository to your local machine.
2. Navigate to the project's root directory in your terminal.
3. Set up your environment variables. You may want to create a `.env` file and use `source .env` to load the variables into your shell.
4. Use Docker Compose to build and run the project:
   ```bash
   docker-compose build
   docker-compose up
   ```

## Using the Project
Once the server is running, you can interact with it through the provided Slack workspace, issuing commands that the bot will respond to. You can also use Postman to test the various API endpoints available in the project.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.


