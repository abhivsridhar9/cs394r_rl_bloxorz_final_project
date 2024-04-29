from pynput.keyboard import Key, Controller
import argparse
from time import sleep

def parse():
    parser = argparse.ArgumentParser(description="Agent Arguments")
    parser.add_argument("--mode", default="single_level", type=str)
    parser.add_argument("--input_file", default="./results/level-1.res", type=str)
    args = parser.parse_args()
    return args

def act(a, kb):
    if a == '0':
        print('RIGHT')
        kb.press(Key.right)
        sleep(0.1)
        kb.release(Key.right)
    elif a == '1':
        print('UP')
        kb.press(Key.up)
        sleep(0.1)
        kb.release(Key.up)
    elif a == '2':
        print('LEFT')
        kb.press(Key.left)
        sleep(0.1)
        kb.release(Key.left)
    elif a == '3':
        print('DOWN')
        kb.press(Key.down)
        sleep(0.1)
        kb.release(Key.down)
    elif a == '4':
        kb.press(Key.space)
        sleep(0.1)
        kb.release(Key.space)

if __name__ == "__main__":
    args = parse()

    print("Args: ", args)

    kb = Controller()
    input("Make sure Bloxorz open and the desired start level is active. Press enter to continue...")
    input("After pressing enter again, you will have 5 seconds to set the focus to Bloxorz by clicking on the game window...")
    sleep(5)

    if args.mode == "single_level":
        with open(args.input_file) as f:
            a = f.readline()[0]
            while(a != ''):
                act(a[0], kb)
                a = f.readline()
                sleep(1)

    elif args.mode == "by_level":
        for level in range(1, 11):
            pass
    
    elif args.mode == "by_playthrough":
        pass

