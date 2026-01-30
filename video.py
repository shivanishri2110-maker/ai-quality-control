from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
cap = cv2.VideoCapture(0)

# Load your YOLO model
model = YOLO("yolov8n.pt")

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Run YOLO detection
            results = model(frame)[0]  # detect objects
            # Draw bounding boxes on the frame
            for r in results.boxes:
                x1, y1, x2, y2 = map(int, r.xyxy[0])
                conf = float(r.conf[0])
                cls = int(r.cls[0])
                label = f"{model.names[cls]} {conf:.2f}"
                # Draw rectangle + label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

            # encode as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('ux4.html')

if __name__ == "__main__":
    app.run(debug=True)
