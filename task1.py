from queue import Queue
import time
import random

# Створити чергу заявок
queue = Queue()

# клас заявки
class Application():
  rec_id=0
  def __init__(self):
    self.id = Application.rec_id
    Application.rec_id+=1

# функція імітації генерації заявки та додавання до черги
def generate_request():
    new_application = Application()
    print(f"\033[91mNew application with id={new_application.id} created\033[0m")
    queue.put(new_application)

# функція імітації обробки заявки і видалення з черги
def process_request():
    if not queue.empty():
        application =queue.get()
        print(f"\033[92mApplication with id={application.id} processed\033[0m")
        time.sleep(1.2)
    else:
        print('\033[96mThe queue is empty\033[0m')


def main():
    try:
        while True:
            # створення заявок
            if random.choice([True, False]):
                for _ in range(random.randint(1,2)):
                    generate_request()
            # обробка заявки
            process_request()
            # часова затримка для імітації надходження заявок
            time.sleep(random.uniform(0.8, 1.6))

    except KeyboardInterrupt:
        print("\033[93mThe server stopped by the admin!\033[0m")
if __name__=="__main__":
    main()