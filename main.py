from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
from PIL import Image

#ort_session = ort.InferenceSession("yolo11x.onnx")
model = YOLO("yolo11n.pt") 
app = FastAPI()



@app.get("/info")
def info():
    return '111'

@app.post('/predict2')
async def predict2(file: UploadFile = File(...)):
    img = Image.open(file.file)
    #image = cv2.cvtColor(np.frombuffer(file.read(), np.uint8), cv2.COLOR_RGB2BGR)
    results = model(img, save_txt = True)
    predictions = results[0]
    results[0].show()
    return {"111":predictions.boxes.conf.tolist()}
