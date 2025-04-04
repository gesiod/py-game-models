from venv import create

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild
import json


def main() -> None:
    with open("players.json", "r") as file:
        data = json.load(file)
        # print(data)

    for name in data:
        player_data = data[name]
        player = Player.objects.create(
            nickname = name,
            email = (player_data["email"] if player_data["email"] else None),
            bio = (player_data["bio"] if player_data["bio"] else None)
        )

        race = player_data.get("race")
        if race:
            player.race = Race.objects.get_or_create(
                name = race["name"],
                description = race["description"]
            )
            skills = race.get["skills"]
            if skills:
                for skill in skills:
                    Skill.objects.create(
                        name = skill["name"],
                        bonus = skill["bonus"],
                        race = player.race
                    )


        guild = player_data.get("guild")
        if guild:
            player.guild = Guild.objects.get_or_create(
                name = guild["name"],
                description = guild["description"]
            )

        print(data[name])



if __name__ == "__main__":
    main()
