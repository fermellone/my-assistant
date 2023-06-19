lights_status = True


def lights_switcher(args: dict) -> str:
    """Turn the lights on if they are off and vice versa"""
    global lights_status
    lights_status = args.get("new_status")

    return "Lights are on" if lights_status else "Lights are off"


function_descriptions = [
    {
        "name": "lights_switcher",
        "description": "Switch the state of the lights",
        "parameters": {
            "type": "object",
            "properties": {
                "new_status": {
                    "type": "boolean",
                    "description": "The new state of the lights (on/off)",
                }
            },
        },
    }
]

available_functions = {
    "lights_switcher": lights_switcher,
}
