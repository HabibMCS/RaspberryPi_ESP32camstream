import requests
from io import BytesIO
import cv2
import numpy as np
import threading

def process_stream(ip_addr, width, height):
    stream_url = f'http://{ip_addr}:81/stream'
    res = requests.get(stream_url, stream=True)
    for chunk in res.iter_content(chunk_size=100000):
        if len(chunk) > 100:
            try:
                start_time = time.time()
                img_data = BytesIO(chunk)
                cv_img = cv2.imdecode(np.frombuffer(img_data.read(), np.uint8), 1)
                cv_resized_img = cv2.resize(cv_img, (width, height), interpolation=cv2.INTER_AREA)
                results = classify_image(interpreter, cv_resized_img)
                elapsed_ms = (time.time() - start_time) * 1000
                label_id, prob = results[0]
                cv2.putText(cv_img, f'{labels[label_id]}', (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
                cv2.putText(cv_img, f'{prob}', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
                cv2.imshow(f"ESP32CAM {ip_addr}", cv_img)
                cv2.waitKey(1)
                print(f'elapsed_ms: {elapsed_ms}')
            except Exception as e:
                print(e)
                continue

ip_addr1 = '192.168.X.XXX'
ip_addr2 = '192.168.X.XXX'

width, height = 640, 480

thread1 = threading.Thread(target=process_stream, args=(ip_addr1, width, height))
thread2 = threading.Thread(target=process_stream, args=(ip_addr2, width, height))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
