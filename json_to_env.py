import json
import clipboard
import sys

def process_json_data(json_data):
    if isinstance(json_data, dict):
        output_data = ''
        for key, value in json_data.items():
            output_data += f"{key}={str(value)}\n"
        return output_data
    else:
        raise ValueError("Input data must be a JSON object")

def main():
    json_secret = sys.argv[1]
    data = json.loads(json_secret)
    env_secrets = process_json_data(data)
    env_secrets = env_secrets.rstrip('\n')
    print('**************************************************')
    print(env_secrets)
    print('**************************************************')
    clipboard.copy(env_secrets)

if __name__ == "__main__":
    main()
