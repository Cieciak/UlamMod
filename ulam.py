import os, configparser

def replace_patterns(text: str, patterns: dict[str, str]) -> str:
    for key in patterns:
        text = text.replace(f'__{key}__', patterns[key])

    return text

COMMAND = 'uwsgi --socket __host__:__host__ --wsgi-file __module__ --callable __factory__ --processes 4 --threads 2'

if __name__ == '__main__':

    configuration = configparser.ConfigParser()
    configuration.read('./.config')

    profile = configuration['setting']['profile']
    print(f'App is using \'{profile}\' profile')
    print(replace_patterns(COMMAND, configuration[profile]))