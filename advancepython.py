import time
# import threading
import concurrent.futures

start = time.perf_counter()

def do_something(second):
    print(f"Sleeping for {second} Second(s)")
    time.sleep(second)
    return "Done Sleeping..."
    
    
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    futures = [executor.submit(do_something,second) for second in secs]
    
    for future in futures:
        print(future.result())
    
    # ***************** TESTING LEARNING CODE ****************
    # future = executor.submit(do_something,1)
    # future1 = executor.submit(do_something,1)
    # result = future.result()
    # result1 = future.result()
    # print(result)
    # print(result1)
    
# ***************************************************
    
    
    
# threads = []
    
# for _ in range(10):
#     t = threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)
    
# for thread in threads:
#     thread.join()
    
finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} second(s)")