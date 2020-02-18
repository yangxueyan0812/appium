import yaml


def openfile():
    with open("../data.yml", 'r', encoding='UTF-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        print(type(data))
        print(data)


if __name__ == '__main__':
    openfile()
