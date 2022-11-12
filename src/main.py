import dota2gsi


def handle_state(_, state: dict):
    # Use nested gets to safely extract data from the state
    hero_name: str = state.get("hero", {}).get("name", "")
    health_percent: float = state.get("hero", {}).get("health_percent", 0)
    max_health: int = state.get("hero", {}).get("max_health", 1)
    # If the attributes exist, print them
    if not health_percent or not max_health:
        return

    health: int = int(max_health * health_percent / 100)
    print(f'{hero_name}"s current health: {health}/{max_health}')


server = dota2gsi.Server()
server.on_update(handle_state)
server.start()
