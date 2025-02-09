import pandas as pd
from data import cars, space_missions, mythology, computer_viruses


def get_keys(dictionary, parent_key="", show_nested_structure=True):
    keys = []
    for key, value in dictionary.items():
        full_key = f"{parent_key}.{key}" if (show_nested_structure and parent_key) else str(key)
        keys.append(full_key)
        if isinstance(value, dict):
            keys.extend(get_keys(value, full_key, show_nested_structure))
    return keys


def print_tables(data_dicts):
    for name, data in data_dicts.items():
        keys = get_keys(data, show_nested_structure=False)
        max_length = max(len(k) for k in keys)

        print(f"\nTable: {name}")
        print("=" * (max_length + 4))
        df = pd.DataFrame({"Nested Keys": keys})
        print(df, '\n')


if __name__ == '__main__':
    datasets = {
        "🚗 Cars": cars,
        "🚀 Space Missions": space_missions,
        "🏛️  Mythology": mythology,
        "🦠 Computer Viruses": computer_viruses
    }
    print_tables(datasets)