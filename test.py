from time import sleep
import multiprocessing

def watcher(var):
    while True:
        print(f'watcher: {var.value}')
        sleep(0.3)

def modifier(var):
    for i in range(5):
        var.value += 1
        print(f'modifier: modified {var.value}')
        sleep(1)
    print(f'modifier: done')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    var = manager.Value('var', 0)
    p1 = multiprocessing.Process(target=modifier, args=(var,))
    p2 = multiprocessing.Process(target=watcher, daemon=True, args=(var,))
    p1.start()
    p2.start()
    p1.join()