import sys
import requests
from bs4 import BeautifulSoup

URL = "https://gtfobins.github.io"


def read(path: str):
    with open(path, "r") as file:
        command_paths = file.readlines()
        commands = []
        for command_path in command_paths:
            command = command_path.replace("\n", "")
            command = command.split("/")
            command = command[len(command) - 1]
            commands.append(command)
        return commands


def search(commands):
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")
    tr_tags = soup.find_all("tr")
    for tr_tag in tr_tags:
        for command in commands:
            td_tags = tr_tag.find_all("td")
            if td_tags:
                a_tag = td_tags[0].find("a")
                if not a_tag == None:
                    if command == a_tag.get_text():
                        print("\n------------------------------")
                        print("command: ", command)
                        li_tags = td_tags[1].find("ul").find_all("li")
                        print("topics:")
                        for li_tag in li_tags:
                            topic_a_tag = li_tag.find("a")
                            topic = topic_a_tag.get_text()
                            path = topic_a_tag["href"]
                            print("  topic: ", topic)
                            print("  url: ", URL + path)


def main():
    if len(sys.argv) < 3:
        print("python main.py [type] [args]")
        print("[type] = file / imdt")
        print("[args] = </path/to/file> / command command command ...")
        return

    arg_type = sys.argv[1]

    if arg_type == "file":
        path = sys.argv[2]
        commands = read(path)
        search(commands)

    if arg_type == "imdt":
        commands = sys.argv[2:]
        search(commands)

    pass


if __name__ == "__main__":
    main()
