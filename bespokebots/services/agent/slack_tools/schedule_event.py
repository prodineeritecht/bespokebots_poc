"""Block Kit UI for scheduling an event."""

def generate_available_slots(slots):
    """Generate the available slots for the user to select from.
    
    Args:
        slots (list): A list of available slots to schedule an event.
        
    Returns:
        list: A list of blocks to be used in the slack message.
    """
    blocks = []

    for i, slot in enumerate(slots, start=1):
        text = f"*Date*: {slot['date']}\n*Start*: {slot['start_time']}\n*End*: {slot['end_time']}"
        block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text,
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Schedule Event",
                    "emoji": True,
                },
                "value": str(i),  # this can be used to identify which slot was selected
                "action_id": "schedule_event_button",
            },
        }
        blocks.append(block)

    return blocks



def generate_schedule_event_modal():
    modal = {
        "type": "modal",
        "callback_id": "schedule_event_modal",
        "title": {
            "type": "plain_text",
            "text": "Schedule Event",
            "emoji": True,
        },
        "submit": {
            "type": "plain_text",
            "text": "Create Event",
            "emoji": True,
        },
        "blocks": [
            {
                "type": "input",
                "block_id": "event_title",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "title",
                },
                "label": {
                    "type": "plain_text",
                    "text": "Event Title",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "block_id": "event_description",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "description",
                },
                "label": {
                    "type": "plain_text",
                    "text": "Event Description",
                    "emoji": True,
                },
            },
        ],
    }

    return modal

