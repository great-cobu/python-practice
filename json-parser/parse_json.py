import json
import pathlib as pl


def main():
    pth = pl.Path('sample/colors.json')
    if not pth.exists():
        print(str(pth)+' not found.')
    with open(pth, 'r') as f:
        data = json.load(f)
        text = json.dumps(data, indent=4, sort_keys=True)
        print(text)


if __name__=='__main__':
    main()
