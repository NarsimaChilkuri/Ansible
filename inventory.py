import json

def get_inventory_data():
    return {
        "db_and_web_servers":{
            "hosts":["db_and_web_server1"],
            "vars":{
                "ansible_ssh_pass":"Passw0rd",
                "ansible_host":"172.17.0.4"
                }
            }
        }
def read_cli_args():
    global args:
    parser = argparse.ArgumentParser()
    parser.add_argument('--list',action='store_true')
    parser.add_argument('--host',action='store')
    args = parser.parse_args()

if __name__ == "__main__":
    global args
    read_cli_args()
    inventory_data = get_inventory_data()
    if args and args.list:
        print(json.dumps(inventory_data))
    elif args.host:
       print(json.dumps({'_meta':{'hostvars':{}{}}}))

