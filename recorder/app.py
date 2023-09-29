# from flask import Flask, Response
# import cv2

# app = Flask(__name__)

# # IP address and credentials of the IP camera
# ip_address = '10.207.121.100'
# username = '38828495'
# password = '123'

# def generate_frames():
#     cap = cv2.VideoCapture(f"rtsp://{username}:{password}@{ip_address}:554/")
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         else:
#             _, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, Response
import cv2

app = Flask(__name__)

def generate_frames():
    cap = cv2.VideoCapture(0)  # Use 0 as the device index for the default USB webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
