import gc
import json
from os import name
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from libs.processor import Processor

COUNT_PROCESSOR = 1
global active_processors
active_processors = []
global processors
processors = []
stop = False


def call_back(future):
    res, processor = future.result()
    # if res['status']:
    #     print(f"                        {processor}  {res} done.")
    # else:
    #     print(f"                        {processor} {res} error.")
    processors.append(processor)


if __name__ == '__main__':
    try:
        loop = True
        process_pool = []
        index = 0
        busy = False
        # with ThreadPoolExecutor() as exe:
        #     processor_pool = {
        #         exe.submit(Processor, i): i
        #         for i in range(COUNT_PROCESSOR)
        #     }
        #     for future in as_completed(processor_pool):
        #         processors.append(future.result())

        # print('Done Initializing!')
        processor = Processor(1)
        names = ['booksmandala']
        total = len(names)
        for name in names:
            print(name)
            processor.process(name)
        # with ThreadPoolExecutor() as exe:
        #     for index, name in enumerate(names):
        #         if busy:
        #             while busy:
        #                 if len(processors) > 0:
        #                     busy = False
        #         processor = processors.pop()
        #         future = exe.submit(processor.process, name)
        #         future.add_done_callback(call_back)
        #         if len(processors) <= 0:
        #             busy = True
        #         print(f"{round(index * 100 / total, 2)}% Done")
        gc.collect()
    except Exception as exp:
        print(exp)
        gc.collect()
